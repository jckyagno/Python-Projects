from django import forms
from django.forms import ModelForm
from .models import Material


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['material_name', 'chemical_category', 'location', 'amount', 'chemical_description', 'hazards']

