from django.forms import ModelForm
from .models import FieldOfView


class cameraForm(ModelForm):
    class Meta:
        model = FieldOfView
        fields = '__all__'
