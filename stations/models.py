from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    geolocation_latitude = models.CharField(max_length=50)
    geolocation_longitude = models.CharField(max_length=50)
    quantity = models.FloatField(default=0)
    seller = models.OneToOneField('users.Seller', on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)




class FuelQuantity(models.Model):
    quantity = models.FloatField()
    station = models.ForeignKey(Station, verbose_name="station", on_delete=models.CASCADE)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)