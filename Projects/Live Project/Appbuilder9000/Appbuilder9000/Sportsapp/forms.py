from django.forms import ModelForm
from .models import player, update

# Create Player form based on Player Model
class PlayerForm(ModelForm):

    class Meta:
        model = player
        fields = '__all__'

# create Update form on Update Model
class UpdateForm(ModelForm):

    class Meta:
        model = update
        fields = '__all__'
