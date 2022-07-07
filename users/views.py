import profile
from tokenize import group
from django.contrib.auth.views import PasswordChangeView

from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse_lazy  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from orders.models import Orders
from stations.models import Station
from users.forms import EditUserForms, PasswordChangeForms, PictureForms, RegisterBuyerForm, RegisterSellerForm
from users.models import Customer, Seller
from django.utils.encoding import force_bytes, force_text  
from django.core.mail import EmailMessage, send_mail 
 
# # Create your views here.


def open_dashboard(request):
    
    stations = Station.objects.all()
    customers = User.objects.filter(groups__name__in=['customer'])
    sellers = User.objects.filter(groups__name__in=['seller'])
    stations_count = stations.count()
    customers_count = customers.count()
    orders = Orders.objects.all()
    orders_count = orders.count()
    context = {
        "stations": stations,
        'customers': customers,
        'sellers': sellers,
        'stations_count': stations_count,
        'customers_count': customers_count,
        'orders_count': orders_count,
        "orders" : orders
    }
    for order in orders:
        print(order.order_id)

    return render(request, 'admin/dashboard.html', context)
   

def generate_random_numbers():
        return User.objects.make_random_password(length=6, allowed_chars='123456789')




def register_customer(request):
    """function for creating forms to add users then sends a verification link to the email of the user"""
    if request.method == 'POST':
        form = RegisterBuyerForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            #save form in the memory not in database
            password = User.objects.make_random_password()
            user = form.save(commit=False)                        
            user.set_password(password)        
            user = form.save()                        
            #adds a group to the user
            user_group = Group.objects.get(name='customer')
            user.groups.add(user_group)
            
            Customer.objects.create(
                user=user,
                profile_picture = request.FILES['profile_picture']
                )

            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('users/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                "user_password" :  password,
                "username" : form.cleaned_data.get('username'),
                "user_group" : "customer"
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()   
            return redirect('home')
    else:  
        form = RegisterBuyerForm() 
    
    customer_id = "CR-" + generate_random_numbers()
    return render(request, 'customer/register_customer.html', {'form': form, 'customer_id': customer_id})






def register_seller(request):
    """function for creating forms to add users then sends a verification link to the email of the user"""
    if request.method == 'POST':
        form = RegisterSellerForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            #save form in the memory not in database
            password = User.objects.make_random_password()
            user = form.save(commit=False)                        
            user.set_password(password)        
            user = form.save()                        
            #adds a group to the user
            user_group = Group.objects.get(name='seller')
            user.groups.add(user_group)
            
            seller = Seller.objects.create(
                user=user,
                profile_picture = request.FILES['profile_picture']
                )
            
            Station.objects.create(
				seller = seller,
				name = form.cleaned_data.get('name'),
				address = form.cleaned_data.get('address'),
				phone = form.cleaned_data.get('phone'),
				quantity = form.cleaned_data.get('quantity'),
				geolocation_latitude = form.cleaned_data.get('geolocation_latitude'),
				geolocation_longitude = form.cleaned_data.get('geolocation_longitude')
			)

            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('users/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                "user_password" :  password,
                "username" : form.cleaned_data.get('username'),
                "user_group" : "seller"


            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()   
            return redirect('home')
    else:
        seller_id = "SR-" + generate_random_numbers()  
        form = RegisterSellerForm() 
    return render(request, 'seller/register_seller.html', {'form': form, 'seller_id': seller_id})






def login_buyer(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})




def customer_detail(request, customer_id):
    customer = User.objects.get(id=customer_id)
    return render(request, 'customer/customer_detail.html', {'customer': customer})
    
def update_customer(request, customer_id):
    user = User.objects.get(id=customer_id)
    customer =  Customer.objects.get(user=user)
    user_forms = EditUserForms(instance=user)
    customer_forms = PictureForms(instance=customer)
    if request.method == 'POST':
        user_forms = EditUserForms(request.POST, instance=user)
        customer_forms = PictureForms(request.POST, request.FILES, instance=customer)
        if user_forms.is_valid() and customer_forms.is_valid:
            user_forms.save()            
            customer_forms.save()
            return redirect('admin-dashboard')

    
    
    return render(request, 'customer/update_user.html', {'user_forms': user_forms, 'customer': customer, 'customer_forms':customer_forms})




class PasswordChange(PasswordChangeView):
    """class for creating forms for users to change their passwords....
    currently not in use since this class is also provided by the allauth model"""
    form_class = PasswordChangeForms
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('home')
 