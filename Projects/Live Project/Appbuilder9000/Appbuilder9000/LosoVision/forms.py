from django.forms import ModelForm
from django import forms
from .models import Patient_Entry


class Patient_EntryForm(ModelForm):
    class Meta:
        model = Patient_Entry
        fields = ['firstName', 'lastName', 'dateOfBirth', 'readingRx']
