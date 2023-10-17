from django.forms import ModelForm
from .models import Jobs
from django import forms

# Creates a widget that makes an input type for a form a field where you can select a date
class DateInput(forms.DateInput):
    input_type = 'date'

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        # Applies the widget made above (DateInput) to the form field date_added
        widgets = {
            'date_added': DateInput()
        }