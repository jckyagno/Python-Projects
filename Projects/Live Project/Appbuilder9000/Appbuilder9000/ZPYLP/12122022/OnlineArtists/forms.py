from django.forms import ModelForm
from .models import onlineartists_add


class OnlineArtistsForm(ModelForm):

    class Meta:
        model = onlineartists_add
        fields = '__all__'