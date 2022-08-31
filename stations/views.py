from datetime import datetime
from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Orders
from stations.forms import UpdateStationForm
from .models import Station, FuelQuantity
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


@login_required(login_url="login")
def get_stations(request):
    stations = Station.objects.all()
    return render(request, 'admin/dashboard.html', {'stations': stations})


# station detail
@login_required(login_url="login")
def station_detail(request, id, name):
    station = Station.objects.get(id=id, name=name)
    sales = Station.objects.raw(f"select  id,sum(price) as 'total_amount', count(*) as 'total_purchase'  from orders_orders where station_id ='{station.id}'  and ordered_time >= date('now','start of month') and paid=true")
    orders = Orders.objects.filter(station_id=station.id)
    fuelquantity = FuelQuantity.objects.filter(station_id=station.id)
    return render(request, 'stations/station_detail.html', {'station': station, 'sales':sales, "orders":orders,"fuelquantity":fuelquantity})


# search station 
@login_required(login_url="login")
def get_station_detail_by_name(request, name):
    fuelquantity = FuelQuantity.objects.filter(station_id=station.id)
    station = Station.objects.get(name=name)
    orders = Orders.objects.filter(station_id=station.id)
    return render(request, 'stations/station_detail.html', {'station': station, "orders":orders, "fuelquantity":fuelquantity})


@login_required(login_url="login")
def update_station(request, station_id):
    station = Station.objects.get(id=station_id)
    update_form = UpdateStationForm(request.POST or None,instance=station)
    if update_form.is_valid():
        update_form.save()
        return redirect("admin-dashboard")
    
    return render(request, 'stations/update_station.html', {'update_form': update_form})
 
@login_required(login_url="login")
def update_quantity(request, station_id):
    station = Station.objects.get(id=station_id)
    if request.method == "POST":
        new_quantity = float(request.POST.get('quantity'))
        FuelQuantity.objects.create(quantity=new_quantity, station=station, time_updated=datetime.now())
        station.quantity = float(station.quantity) + new_quantity
        station.save()
    messages.success(request, "Fuel Quantity Updated!!!", extra_tags='alert alert-success alert-dismissible fade show')
    return HttpResponseRedirect(reverse('station-detail', kwargs={'id': station.id, 'name':station.name}))



@login_required(login_url="login")
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
    return JsonResponse({"data":data}) 

