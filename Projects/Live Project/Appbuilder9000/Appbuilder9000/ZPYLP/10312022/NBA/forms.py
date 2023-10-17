from django.forms import ModelForm
from .models import Player, Enter
from django import forms


class EnterForm(ModelForm):
    class Meta:
        model = Enter
        fields = ['name', 'team']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
