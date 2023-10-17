from django.forms import ModelForm
from .models import Beast, Monster
from django import forms


class BeastForm(ModelForm):
    class Meta:
        model = Beast
        fields = ['name', 'title', 'skin', 'species', 'power', 'sentient', ]
        labels = {
            'name': 'Name',
            'title': 'Title',
            'skin': 'Skin',
            'species': 'Species',
            'power': 'Power',
            'sentient': 'Is Sentient?',
        }
        widgets = {

        }


class BeastEditForm(ModelForm):
    class Meta:
        model = Beast
        fields = "__all__"
        labels = {
            'name': 'Name',
            'title': 'Title',
            'skin': 'Skin',
            'species': 'Species',
            'power': 'Power',
            'sentient': 'Is Sentient?',
            'encounter': 'Date Discovered',
        }
        widgets = {
            'encounter': forms.SelectDateWidget
        }


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = "__all__"
