from django.contrib.auth.models import User
from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    price = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Gh₵ ', 'readonly':'True'}))
    quantity = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'in gallons'}))

    class Meta:
        model = Orders
        fields = ( 'quantity', 'price')