from django.forms import ModelForm
from django import forms
from .models import Evaluation


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = ['symbol', 'style', 'documents_set_1', 'documents_set_2', 'documents_set_3']
