from django.forms import ModelForm
from .models import Sitcom, WeatherMoment


class SitcomForm(ModelForm):
    class Meta:
        model = Sitcom
        fields = ['title', 'network', 'numberOfSeasons', 'description']


class WeatherMomentForm(ModelForm):
    class Meta:
        model = WeatherMoment
        fields = "__all__"
