from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Seller

admin.site.register(Customer)
admin.site.register(Seller)