from django.forms import ModelForm
from django import forms
from .models import Destination, WeatherMoment


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['Country', 'Region']


class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"