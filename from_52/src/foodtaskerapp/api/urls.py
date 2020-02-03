from django.urls import path
from django.conf.urls import url, include

from .views import customer_get_restaurants, customer_get_meals, customer_add_order, customer_get_latest_order, \
    customer_driver_location, driver_get_ready_orders, driver_pick_order, driver_get_latest_order, \
    driver_complete_order, driver_get_revenue, driver_update_location, ApiGetRestaurantsList, ApiGetMealsList

app_name = 'foodtaskerapp'

urlpatterns = [

    # APIs for CUSTOMERS
    # path('restaurants/', customer_get_restaurants),
    url(r'^meals/(?P<restaurant_id>\d+)/$', customer_get_meals),
    path('customer/restaurants/', ApiGetRestaurantsList.as_view()),
    url(r'^customer/meals/(?P<restaurant_id>\d+)/$', ApiGetMealsList.as_view()),
    path('customer/order/add/', customer_add_order),
    path('customer/order/latest/', customer_get_latest_order),
    url(r'^customer/driver/location/$', customer_driver_location),

    # APIs for DRIVERS
    url(r'^driver/orders/ready/$', driver_get_ready_orders),
    url(r'^driver/order/pick/$', driver_pick_order),
    url(r'^driver/order/latest/$', driver_get_latest_order),
    url(r'^driver/order/complete/$', driver_complete_order),
    url(r'^driver/revenue/$', driver_get_revenue),
    url(r'^driver/location/update/$', driver_update_location),
]
