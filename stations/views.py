from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from stations.forms import UpdateStationForm
from .models import Station
# Create your views here.


@login_required(login_url="login")
def get_stations(request):
    stations = Station.objects.all()
    return render(request, 'admin/dashboard.html', {'stations': stations})


# station detail
def station_detail(request, id):
    station = Station.objects.get(id=id)
    return render(request, 'stations/station_detail.html', {'station': station})


# search station 
def get_station_detail_by_name(request, name):
    station = Station.objects.get(name=name)
    return render(request, 'stations/station_detail.html', {'station': station})


def update_station(request, station_id):
    station = Station.objects.get(id=station_id)
    update_form = UpdateStationForm(request.POST or None,instance=station)
    if update_form.is_valid():
        update_form.save()
        return redirect("admin-dashboard")
    
    return render(request, 'stations/update_station.html', {'update_form': update_form})
 
def get_stations_coordinates(request):
    stations  = Station.objects.all()
    data = []
    station_data = []
    for station in stations:
        station_data = {
            "name" : station.name + "   Qty:" + str(station.quantity),
            "geolocation_latitude": station.geolocation_latitude,
            "geolocation_longitude" : station.geolocation_longitude,
        }        
        data.append(station_data)
    print(data)
    return JsonResponse({"data":data}) 

