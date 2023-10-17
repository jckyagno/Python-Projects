#imports
from django.db import models

# Models;


class Destination(models.Model):
    Country = models.CharField(max_length=35)
    Region = models.CharField(max_length=35)
    Description = models.CharField(max_length=50)

    # Model Manager;
    objects = models.Manager()

    # str() Method;
    def __str__(self):
        return self.Country


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date