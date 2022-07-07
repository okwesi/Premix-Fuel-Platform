from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures/sellers', blank=True)

    def __str__(self):
        return str(self.user)
    

    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('show_profile', args=(str(self.pk)))
    


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures/buyers', blank=True)

    def __str__(self):
        return str(self.user)
    

    def get_absolute_url(self):
        """return the blog detail of the immediate blog posted"""
        return reverse('show_profile', args=(str(self.pk)))