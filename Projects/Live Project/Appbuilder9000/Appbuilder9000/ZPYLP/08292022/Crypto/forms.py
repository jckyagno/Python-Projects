from django .forms import ModelForm
from .models import AddCrypto
from django import forms


class AddCryptoForm(ModelForm):
    class Meta:
        model = AddCrypto
        fields = '__all__'
