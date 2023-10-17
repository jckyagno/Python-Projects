from django.db import models


# Model
class Crew(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=60, null=True)
    age = models.IntegerField()

    # Defines the model Manager for entry
    Entry = models.Manager()

    # Allows references to a specific rower be returned as the Rowers name not the primary key
    def __str__(self):
        return self.first_name + '' + self.last_name

class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date
