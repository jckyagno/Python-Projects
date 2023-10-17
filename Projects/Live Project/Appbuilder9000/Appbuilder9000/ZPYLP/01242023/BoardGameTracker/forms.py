from django.forms import ModelForm
from .models import BoardGames


class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGames
        fields = '__all__'
