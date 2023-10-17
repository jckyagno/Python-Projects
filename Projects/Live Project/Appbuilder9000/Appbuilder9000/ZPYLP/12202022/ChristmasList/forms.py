from django.forms import ModelForm
from django import forms
from .models import Gift, ChristmasJoke

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = '__all__'

class ChristmasJokeForm(ModelForm):
    class Meta:
        model = ChristmasJoke
        fields = "__all__"