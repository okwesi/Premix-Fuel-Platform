from django.contrib import admin

from stations.models import Station

# Register your models here.
class StationAdmin(admin.ModelAdmin):
  list_display = ['id','name',"address", "quantity"]

admin.site.register(Station,StationAdmin)
