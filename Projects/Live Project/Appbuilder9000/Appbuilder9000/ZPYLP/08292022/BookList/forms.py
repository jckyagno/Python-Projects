from django.forms import ModelForm
from .models import BookEntry

class EntryForm(ModelForm):
    class Meta:
        model = BookEntry
        fields = '__all__'


