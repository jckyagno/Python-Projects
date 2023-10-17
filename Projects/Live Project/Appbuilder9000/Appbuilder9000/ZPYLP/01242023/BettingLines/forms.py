from django.forms import ModelForm
from django.db import models
from .models import Bet

class BettingForm(ModelForm):
    class Meta:
        model = Bet
        fields = '__all__'
