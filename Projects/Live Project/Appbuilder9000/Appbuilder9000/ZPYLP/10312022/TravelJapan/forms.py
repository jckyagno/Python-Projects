from django.forms import ModelForm
from .models import AddEntry


class AddEntryForm(ModelForm):
    class Meta:
        model = AddEntry
        fields = "__all__"
