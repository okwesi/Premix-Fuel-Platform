from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    geolocation_latitude = models.CharField(max_length=50)
    geolocation_longitude = models.CharField(max_length=50)
    quantity = models.IntegerField()
    seller = models.OneToOneField('users.Seller', on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    
    