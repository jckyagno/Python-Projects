from django .forms import ModelForm
from .models import AddMusic
from django import forms


class AddMusicForm(ModelForm):
    class Meta:
        model = AddMusic
        fields = '__all__'
