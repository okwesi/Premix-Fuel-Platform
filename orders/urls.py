from django.urls import  path

from .views import *


urlpatterns = [
    # path("station/", order_station, name="order-station"),
    path("station/", StationListView.as_view(), name="order-station"),
    path("oil/<int:station_id>", order_oil, name="order-oil"),
    path('pay/<str:order_id>', pay, name='pay'),
    path('paid/<str:order_id>/<int:reference_id>', paid, name='paid'),
    path("seller/orders/", seller_orders, name="seller-orders"),
    path("seller/<str:order_id>", seller_order_detail, name="seller-order-detail"),
    path("delivered/<str:order_id>", delivered, name="delivered"),
    path("received/<str:order_id>", received, name="received"),
    
    
    path("customer/orders/", customer_orders, name="customer-orders"),
    path("customer/<str:order_id>", customer_order_detail, name="customer-order-detail"),
]
