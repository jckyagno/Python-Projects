from django.forms import ModelForm
from .models import PlayerModel


class PlayerForm(ModelForm):
    class Meta:
        model = PlayerModel
        fields = ['first_name' , 'last_name', 'player_points', 'player_assists']


