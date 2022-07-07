from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django import forms

from users.models import Customer


class RegisterBuyerForm(forms.ModelForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=12, widget= forms.TextInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(required=True)
    #the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', "profile_picture")

class RegisterSellerForm(forms.ModelForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(required=True)
    name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    geolocation_longitude = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    geolocation_latitude = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    #the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'phone',
                  "profile_picture", "name", 
                  'address', 'phone', 'quantity',
                  "geolocation_longitude", "geolocation_latitude",
                  )


class EditUserForms(forms.ModelForm):
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))

#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class PictureForms(forms.ModelForm):
    profile_picture = forms.ImageField(required=True)
    phone = forms.CharField(max_length=12, widget= forms.TextInput(attrs={'class': 'form-control'}))


#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = Customer
        fields = ('profile_picture', 'phone')


class PasswordChangeForms(PasswordChangeForm):
    old_password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
