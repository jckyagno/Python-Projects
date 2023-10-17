from django .forms import ModelForm
from .models import AddFan



class AddFanForm(ModelForm):
    class Meta:
        model = AddFan
        fields = '__all__'
