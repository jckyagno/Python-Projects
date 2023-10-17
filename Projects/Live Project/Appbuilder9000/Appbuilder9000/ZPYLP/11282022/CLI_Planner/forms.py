from django.forms import ModelForm
from .models import Event
from .widgets import DatePicker

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'start_date', 'end_date', 'description']

        widgets = {
            'start_date' : DatePicker(),
            'end_date' : DatePicker(),
        }
