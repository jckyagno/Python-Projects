from django.forms import ModelForm, Textarea
from .models import Fbeast


class FbeastForm(ModelForm):
    class Meta:
        model = Fbeast
        fields = '__all__'
        widgets = {
            'name': Textarea(attrs={'cols': 25, 'rows': 1}),
        }