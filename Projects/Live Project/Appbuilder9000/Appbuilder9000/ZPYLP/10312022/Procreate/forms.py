from django.forms import ModelForm
from django import forms
from .models import Procreate


class ProcreateForm(ModelForm):

    class Meta:
        model = Procreate
        fields = ['social_media','artist_name', 'description','image']