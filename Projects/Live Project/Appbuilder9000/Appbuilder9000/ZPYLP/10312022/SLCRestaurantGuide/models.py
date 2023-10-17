from django.db import models


# Create your models here.
# Model for Itinerary(what restaurant, dish, price, etc..)
class Itinerary(models.Model):
    # choices for beverages
    BEV_CHOICES = (
        ('water', 'water'),
        ('fountain drinks', 'fountain drinks'),
        ('beer', 'beer'),
        ('wine', 'wine'),
        ('liquor', 'liquor'),
        ('smoothy', 'smoothy')
    )
    restaurant_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    restaurant_rating = models.DecimalField(max_digits=2, decimal_places=1)
    dish_of_choice = models.CharField(max_length=30)
    price_of_dish = models.DecimalField(max_digits=7, decimal_places=2)
    beverages = models.CharField(max_length=30, choices=BEV_CHOICES)

    # Creates Model Manager
    objects = models.Manager()

    # Returns a string value of the given restaurant_name and its address
    def __str__(self):
        return self.restaurant_name + '|' + self.address
