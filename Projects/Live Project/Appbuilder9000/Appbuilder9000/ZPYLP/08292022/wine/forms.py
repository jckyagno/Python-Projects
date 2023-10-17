from django.forms import ModelForm
from django import forms
from .models import Wines

class WinesForm(ModelForm):
    class Meta:
        model = Wines
        fields = '__all__'
