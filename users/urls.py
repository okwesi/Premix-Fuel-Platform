from django.urls import include, path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path("login", login_buyer, name="login-custom"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/dashboard', open_dashboard, name="admin-dashboard"),
    path('admin/register-customer', register_customer, name="register-customer"),
    path('admin/register-seller', register_seller, name="register-seller"),
    path('customer-detail/<int:customer_id>', customer_detail, name="customer-detail"),
    path('update-customer/<int:customer_id>', update_customer, name="update-customer"),
]









