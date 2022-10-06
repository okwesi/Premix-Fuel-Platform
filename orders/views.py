from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from orders.forms import OrderForm
from stations.models import Station
from .models import Orders, Price
from pypaystack import Transaction, Customer, Plan
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

#get all orders
def get_orders(request):
    orders = Orders.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})

# get an order
def get_order_detail(request, id):
    order = Orders.objects.get(id=id)
    return render(request, 'orders/order_detail.html', {'order': order})



# search order through JSON

def search_order(request):
    data = []
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text is not None:
            orders = Orders.objects.filter(order_id__icontains=search_text)
            for order in orders:
                order_data = {
                    "id" : order.id,
                    "order_id": order.order_id,
                    "order_date": order.order_date,
                    "order_status": order.order_status,
                    "order_total": order.order_total,
                }
                data.append(order_data)
            
    return JsonResponse({'data': data}, safe=False)



# user orders
def customer_orders(request):
    orders = Orders.objects.filter(customer=request.user.customer, paid=True).order_by("-ordered_time")
    price = Price.objects.all().order_by("-time_created").first()
    return render(request, 'customer/customer_orders.html', {'orders': orders, 'price': price})

def customer_order_detail(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    price = Price.objects.all().order_by("-time_created").first()

    return render(request, 'customer/customer_order_detail.html', {'order': order, 'price': price})


# seller orders
def seller_orders(request):
    unprocessed_orders = Orders.objects.filter(station=request.user.seller.station, delivered=False, received=False, paid=True).order_by("-ordered_time")
    processed_orders = Orders.objects.filter(station=request.user.seller.station, delivered=True, received=True, paid=True).order_by("-ordered_time")
    
    station = Station.objects.get(id=request.user.seller.station.id)
    oil_quantity = station.quantity
    return render(request, 'seller/orders.html', {'unprocessed_orders': unprocessed_orders, 'processed_orders': processed_orders, 'oil_quantity': oil_quantity})


def seller_order_detail(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    return render(request, 'seller/order_detail.html', {'order': order})





def order_oil(request, station_id):    
    order_form = OrderForm()
    price = Price.objects.all().order_by("-time_created").first()
    station = Station.objects.get(id=station_id)
    full_name = request.user.first_name + " " + request.user.last_name
    get_initials(fullname=full_name)
    order_id = get_initials(fullname=full_name) +"-"+ generate_random_numbers()
    if request.method == 'POST':
        if order_form.is_valid:
            delivery_box = request.POST.get("box")
            if delivery_box:
                delivery = True
            order = Orders.objects.create(
                order_id = order_id,
                customer = request.user.customer,
                station = station,
                quantity = request.POST['quantity'],
                price = request.POST['price'], 
                delivery = delivery           
            )
           
        return redirect('pay', order_id=order.order_id)
    else:
        return render(request, 'customer/buy.html', 
                      {'order_form': order_form, 'order_id': order_id, 'price': price, 'station': station})
        
        
        

def get_initials(fullname):
  xs = (fullname)
  name_list = xs.split()

  initials = ""

  for name in name_list:  # go through each name
    initials += name[0].upper()  # append the initial

  return initials

def generate_random_numbers():
        return User.objects.make_random_password(length=6, allowed_chars='123456789')




def pay(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    price = Price.objects.all().order_by("-time_created").first()

    return render(request, 'customer/pay.html', {'order': order, 'price': price})

def paid(request, order_id, reference_id):
    order = Orders.objects.get(order_id=order_id)
    station = Station.objects.get(id=order.station.id)
    transaction = Transaction(authorization_key="sk_test_38b5f48935d447f62045a3a37654d63040fdc70d")
    response  = transaction.verify(reference_id)
    if response[3].get('status') == "success":
        station.quantity = int(station.quantity) - int(order.quantity)
        station.save()
        order.paid = True
        order.save()
        messages.success(request, response[2], extra_tags='alert alert-success alert-dismissible fade show')
        return HttpResponseRedirect(reverse('customer-order-detail', kwargs={'order_id': order.order_id,}))
    else:
        messages.success(request, response[2], extra_tags='alert alert-success alert-dismissible fade show')
        return HttpResponseRedirect(reverse('pay', kwargs={'id': order_id,}))
    # return redirect("order-station")

def received(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    order.received = True
    order.received_time = datetime.now()
    order.save()
    return redirect('customer-orders')

def delivered(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    order.delivered = True
    order.delivered_time = datetime.now()
    order.save()
    return redirect('seller-orders')


def order_station(request):
    stations = Station.objects.all()
    price = Price.objects.all().order_by("-time_created").first()

    return render(request, 'customer/order_station.html', {'stations': stations, 'price': price})

from django.views.generic import  ListView

class StationListView(ListView):
    model = Station
    template_name = 'customer/order_station.html'
    context_object_name = "stations"
    paginate_by = 20
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price"] = Price.objects.all().order_by("-time_created").first()
        return context



# def get_orders(request):
#     orders = Orders.objects.all()
#     return render(request, 'admin/all_order.html', {"order":orders})




