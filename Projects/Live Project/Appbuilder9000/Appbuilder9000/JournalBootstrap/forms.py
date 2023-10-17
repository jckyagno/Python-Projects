from django.forms import ModelForm
from django import forms
from .models import JournalEntry


class JournalEntryForm(ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'body']