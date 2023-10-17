from django.forms import ModelForm, DateInput
from .models import Snowmobile, Weather


class SnowmobileForm(ModelForm):
    class Meta:
        model = Snowmobile
        fields = ['make', 'model', 'dateManufactured', 'description']
        widgets = {
            'dateManufactured': DateInput(format='%m/%d/%Y', attrs={'placeholder': 'Select a date'})
        }


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"
