from django.forms import ModelForm
from .models import Sneaker

class sneakerForm(ModelForm):
	class Meta:
		model = Sneaker
		fields = '__all__'