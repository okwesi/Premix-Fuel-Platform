from django import forms

from stations.models import Station

class UpdateStationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    geolocation_longitude = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    geolocation_latitude = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Station
        fields = ('name', 'address', 'phone', 'quantity', 'geolocation_longitude', 'geolocation_latitude')