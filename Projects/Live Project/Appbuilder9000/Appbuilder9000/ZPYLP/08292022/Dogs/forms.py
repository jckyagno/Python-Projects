from django.forms import ModelForm
from .models import Dogs


class DogsForm(ModelForm):
    class Meta:
        model = Dogs # use the Dogs model
        fields = '__all__'