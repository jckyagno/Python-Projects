from django.db import models

# Create your models here.
# Creating drop down options to organize categories

TYPE_CAMPING = {
    ('Tent Only', 'Tent Only'),
    ('Backpacking', 'Backpacking'),
    ('SUV/Truck/Van', 'SUV/Truck/Van'),
    ('RV/Trailer/Camper/5th Wheel', 'RV/Trailer/Camper/5th Wheel'),
}

TYPE_TERRAIN = {
    ('Mountain Range/Wilderness', 'Mountain Range/Wilderness'),
    ('Desert/Dry', 'Desert/Dry'),
    ('Beach/Body of Water', 'Beach/Body of Water'),
    ('Rainforest/Humid', 'Rainforest/Humid'),
}

TYPE_CATEGORY = {
    ('Tent/Campsite', 'Tent/Campsite'),
    ('Bedding/Sleeping', 'Bedding/Sleeping'),
    ('Kitchen/Cooking', 'Kitchen/Cooking'),
    ('Food', 'Food'),
    ('Vehicle', 'Vehicle'),
    ('Drinks', 'Drinks'),
    ('Seasonings/Oils/Condiments', 'Seasonings/Oils/Condiments'),
    ('Bathroom/Hygiene', 'Bathroom/Hygiene'),
    ('Health/Medical', 'Health/Medical'),
    ('Recreation', 'Recreation'),
    ('Miscellaneous', 'Miscellaneous'),
}


# Creates the models of classes and user input
class Entry(models.Model):
    destination = models.CharField(max_length=50, default="", blank=False, null=True)
    camping_style = models.CharField(max_length=50, default="", choices=TYPE_CAMPING)
    terrain_and_climate = models.CharField(max_length=50, default="", choices=TYPE_TERRAIN)
    category = models.CharField(max_length=50, default="", choices=TYPE_CATEGORY)
    item_or_task = models.CharField(max_length=75, default="", blank=True, null=False)

    Entries = models.Manager()

    def __str__(self):
        return self.destination


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date
