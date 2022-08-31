from django.urls import include, path

from .views import *


urlpatterns = [
    path("station-detail/<int:id>/<str:name>", station_detail, name="station-detail"),
    path('update-station/<int:station_id>', update_station, name="update-station"),
    path("get-stations-coordinates/", get_stations_coordinates, name="get-stations-cordinates"),
    path("update-quantity/<int:station_id>/", update_quantity, name="update-quanity")
]









