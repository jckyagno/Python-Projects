from django import forms
from .models import Trails


class TrailsForm(forms.ModelForm):
    class Meta:
        model = Trails
        fields = "__all__"
