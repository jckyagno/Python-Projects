from .models import AddBook
from django import forms

# Creates Add Book form based on Add Book model
class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'