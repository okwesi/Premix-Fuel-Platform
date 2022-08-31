from django.contrib import admin
from .models import Price

# Register your models here.
class PriceAdmin(admin.ModelAdmin):
  list_display = ['id','price',"time_created"]

admin.site.register(Price,PriceAdmin)



