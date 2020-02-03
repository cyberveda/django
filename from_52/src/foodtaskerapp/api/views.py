import json

from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from log import setup_logger
from .serializers import RestaurantSerializer, MealSerializer, OrderSerializer
from ..models import Restaurant, Meal, Order, OrderDetails

logger = setup_logger()


class ApiGetRestaurantsList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = ()
    permission_classes = ()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'address', 'author__username')


class ApiGetMealsList(ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = ()
    permission_classes = ()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Meal.objects.filter(restaurant_id=restaurant_id).order_by("-id")

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'short_description')


def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many=True
    ).data

    return JsonResponse({"restaurants": restaurants})


def customer_get_meals(request, restaurant_id):
    meals = MealSerializer(
        Meal.objects.filter(restaurant_id=restaurant_id).order_by("-id"),
        many=True
    ).data

    return JsonResponse({"meals": meals})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def customer_add_order(request):
    """
    params:
        restaurant_id
        address
        order_details (json format) --> [{"meal_id":1, "quantity": 2}, {"meal_id":2, "quantity": 4}]
    :param request:
    :return:
        {"status": "success"}
    """

    logger.info(request)
    logger.info(request.user)
    logger.info(dir(request))
    logger.info(dir(request.user))
    customer = request.user.customer

    if request.method == 'POST':
        logger.info('in post')
        if Order.objects.filter(customer=customer).exclude(status=Order.DELIVERED):
            return JsonResponse({"status": "fail", "error": "Your last order must be completed"})

        # check address
        if not request.POST["address"]:
            return JsonResponse({"status": "failed", "error": "Address is required"})

        order_details = json.loads(request.POST["order_details"])

        order_total = 0
        for meal in order_details:
            order_total += Meal.objects.get(id=meal["meal_id"]).price * meal["quantity"]

        if len(order_details) > 0:
            # 1 --> create order
            order = Order.objects.create(
                customer=customer,
                restaurant_id=request.POST["restaurant_id"],
                total=order_total,
                status=Order.COOKING,
                address=request.POST["address"]

            )

            # 2 --> Create Order Details
            for meal in order_details:
                OrderDetails.objects.create(
                    order=order,
                    meal_id=meal["meal_id"],
                    quantity=meal["quantity"],
                    sub_total=Meal.objects.get(id=meal["meal_id"]).price * meal["quantity"]

                )

            return JsonResponse({"status": "success"})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def customer_get_latest_order(request):
    customer = request.user.customer
    order = OrderSerializer(Order.objects.filter(customer=customer).last()).data
    return JsonResponse({"order": order})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def customer_driver_location(request):
    customer = request.user.customer

    # Get driver's location related to this customer's current order.
    current_order = Order.objects.filter(customer=customer, status=Order.ONTHEWAY).last()
    location = current_order.driver.location

    return JsonResponse({"location": location})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def driver_get_ready_orders(request):
    orders = OrderSerializer(
        Order.objects.filter(status=Order.READY, driver=None).order_by("-id"),
        many=True
    ).data

    return JsonResponse({"orders": orders})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def driver_pick_order(request):
    if request.method == "POST":
        driver = request.user.driver

        # Check if driver can only pick up one order at the same time
        if Order.objects.filter(driver=driver).exclude(status=Order.ONTHEWAY):
            return JsonResponse({"status": "failed", "error": "You can only pick one order at the same time."})

        try:
            order = Order.objects.get(
                id=request.POST.get('order_id'),
                driver=None,
                status=Order.READY
            )
            order.driver = driver
            order.status = Order.ONTHEWAY
            order.picked_at = timezone.now()
            order.save()

            return JsonResponse({"status": "success"})

        except Order.DoesNotExist:
            return JsonResponse({"status": "failed", "error": "This order has been picked up by another."})

    return JsonResponse({})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
# GET params: access_token
def driver_get_latest_order(request):
    # Get token
    driver = request.user.driver

    order = OrderSerializer(
        Order.objects.filter(driver=driver).order_by("picked_at").last()
    ).data

    return JsonResponse({"order": order})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def driver_complete_order(request):
    # Get token
    driver = request.user.driver

    order = Order.objects.get(id=request.POST["order_id"], driver=driver)
    order.status = Order.DELIVERED
    order.save()

    return JsonResponse({"status": "success"})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def driver_get_revenue(request):
    driver = request.user.driver

    from datetime import timedelta

    revenue = {}
    today = timezone.now()
    current_weekdays = [today + timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]

    for day in current_weekdays:
        orders = Order.objects.filter(
            driver=driver,
            status=Order.DELIVERED,
            created_at__year=day.year,
            created_at__month=day.month,
            created_at__day=day.day
        )

        revenue[day.strftime("%a")] = sum(order.total for order in orders)

    return JsonResponse({"revenue": revenue})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def driver_update_location(request):
    if request.method == "POST":
        driver = request.user.driver

        # Set location string => database
        driver.location = request.POST["location"]
        driver.save()

        return JsonResponse({"status": "success"})
