from django.forms import ModelForm
from .models import Movie, Weather


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"