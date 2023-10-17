from django.db import models
import datetime


# Create your models here.
class Trails(models.Model):
    trail_system = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, null=True)
    date = models.DateField("Date", default=datetime.date.today)
    notes = models.TextField(max_length=500, null=True)
    ridden = models.BooleanField(default=False)

    #  renames the instances of the model with their trail system and country
    def __str__(self):
        return f"{self.trail_system}, {self.country}"
    #  model manager named trails
    trails = models.Manager()
