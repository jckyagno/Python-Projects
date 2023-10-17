from django.forms import ModelForm, forms
from .models import ContactForm, WeatherInfo


class ConForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ConForm, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs\
            .update({
                'class': 'inputbox'
        })
        self.fields['Topic'].widget.attrs\
            .update({
                'class': 'inputbox',
                'value': '',
        })
        self.fields['Email'].widget.attrs\
            .update({
                'class': 'inputbox'
        })
        self.fields['Message'].widget.attrs\
            .update({
                'class': 'inputbox'
        })

class WeatherTemp(ModelForm):
    class Meta:
        model = WeatherInfo
        fields = "__all__"
