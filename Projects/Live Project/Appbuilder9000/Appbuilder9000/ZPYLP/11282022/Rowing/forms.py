from django.forms import ModelForm
from django import forms
from .models import Crew, WeatherMoment

# This creates the forms
class EntryForm(ModelForm):
    class Meta:
        model = Crew
        fields = ['first_name', 'last_name', 'position', 'age']

class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"
