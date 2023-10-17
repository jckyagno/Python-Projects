from django.forms import ModelForm
from .models import Itinerary


class EntryForm(ModelForm):
    class Meta:
        model = Itinerary
        fields = ['restaurant_name', 'address', 'restaurant_rating', 'dish_of_choice', 'price_of_dish', 'beverages']
