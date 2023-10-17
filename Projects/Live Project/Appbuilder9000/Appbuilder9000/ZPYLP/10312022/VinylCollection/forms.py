from django.forms import ModelForm
from .models import Release, Artist
from django import forms

class ReleaseForm(ModelForm):
    release_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2030)))
    class Meta:
        model = Release
        fields = '__all__'

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'