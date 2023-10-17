from django.forms import ModelForm
from .models import Ani


class AniForm(ModelForm):
    class Meta:
        model = Ani
        fields = "__all__"
