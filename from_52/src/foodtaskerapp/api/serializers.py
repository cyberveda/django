from rest_framework import serializers

from ..models import Restaurant, Meal, Customer, OrderDetails, Order


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "title", "phone", "address", "image")


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "restaurant_id", "short_description", "image", "price")


class OrderCustomerSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Customer
        fields = ("id", "name", "avatar", "phone", "address")


class OrderDriverSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Customer
        fields = ("id", "name", "avatar", "phone", "address")


class OrderRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "title", "phone", "address")


class OrderMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "price")


class OrderDetailsSerializer(serializers.ModelSerializer):
    meal = OrderMealSerializer

    class Meta:
        model = OrderDetails
        fields = ("id", "meal", "quantity", "sub_total")


class OrderSerializer(serializers.ModelSerializer):
    customer = OrderCustomerSerializer()
    driver = OrderDriverSerializer()
    restaurant = OrderRestaurantSerializer()
    order_details = OrderDetailsSerializer(many=True)
    status = serializers.ReadOnlyField(source="get_status_display")

    class Meta:
        model = Order
        fields = ("id", "customer", "restaurant", "driver", "order_details", "total", "status", "address")
