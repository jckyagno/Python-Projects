from django import forms
from django.forms import ModelForm
from .models import AddPokemon, CreateUser


# creates Create User Form based on Create User Model
class CreateUserForm(ModelForm):
    class Meta:
        model = CreateUser
        fields = '__all__'

    #def clean_trainer(self):
        #data = self.cleaned_data['trainer_name']
       # if {trainer_name} in data:
           # raise ValidationError("There is already a trainer with that name. Please choose another one!")
       # return data


#creates Pokemon Form based on Pokemon Model
class AddPokemonForm(ModelForm):
    class Meta:
        model = AddPokemon
        fields = '__all__'
#Creatinng a form to add an article
form = AddPokemonForm()



class TrainerProfileForm(forms.Form):
    trainer_name = forms.CharField(label="Trainer Profile", max_length=100)
