from django.db import models
from .models import GitFiddle
from django import forms
from django.forms import ModelForm

class GuitarForm(ModelForm):
    class Meta:
        model = GitFiddle
        fields = ['list_name', 'brand', 'strings', 'acoustic', 'frets', 'price']