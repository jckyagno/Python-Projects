from django import forms
from django.forms import ModelForm
from .models import Vampire

class VampireForm(ModelForm):
    class Meta:
        model = Vampire
        fields = ['vampire_name', 'date_spotted', 'where_spotted', 'evidence']