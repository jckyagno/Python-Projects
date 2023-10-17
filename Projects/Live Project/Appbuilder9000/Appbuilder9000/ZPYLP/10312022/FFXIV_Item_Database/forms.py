from django .forms import ModelForm
from .models import Collection
from django import forms


class CreateCollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
