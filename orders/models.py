from email.policy import default
from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    quantity = models.CharField(max_length=10)
    price = models.FloatField(max_length=10)
    received = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    ordered_time = models.DateTimeField(auto_now_add=True)
    delivered_time = models.DateTimeField(null=True, blank=True)
    received_time = models.DateTimeField(null=True, blank=True)
    station = models.ForeignKey('stations.Station', on_delete=models.CASCADE)
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)
    
class Price(models.Model):
    price = models.CharField(max_length=10)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
