from django.forms import ModelForm
from .models import Information

class BookForm(ModelForm):
    class Meta:
        model = Information
        fields = "__all__"
