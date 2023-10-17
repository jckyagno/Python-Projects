from django.forms import ModelForm
from .models import Recipe


# Produces the form to get the recipe data
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

