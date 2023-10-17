from django.forms import ModelForm
from django import forms
from .models import bucketItem


class BucketItemForm(ModelForm):
    class Meta:
        model = bucketItem
        fields = ['month', 'activity', 'location', 'required_items']
