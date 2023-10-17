from django import forms
from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm, forms.Form):
    activity_details = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))
    activity_date_and_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'placeholder':"YYYY-MM-DD HH:MM"}))

    class Meta:
        model = Entry
        fields = '__all__'

