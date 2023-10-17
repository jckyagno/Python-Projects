from django.forms import ModelForm
from django import forms
from .models import User, ChooseUser

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Password', 'Age', 'Gender', 'Height', 'Weight', ]

class ChooseUserForm(ModelForm):
    class Meta:
        model = ChooseUser
        fields = '__all__'