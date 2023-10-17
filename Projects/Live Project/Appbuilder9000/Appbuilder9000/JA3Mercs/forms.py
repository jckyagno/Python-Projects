from django.forms import ModelForm, Textarea
from .models import Merc
from django import forms


class MercForm(ModelForm):
    class Meta:
        model = Merc
        fields = ['fname','callsign','lname','training','salary','description']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }