from django.db import models


class Plant(models.Model):
    plant_name = models.CharField(max_length=80)
    sunlight_needs = models.CharField(max_length=80)
    water_needs = models.CharField(max_length=80)
    location = models.CharField(max_length=7)

    objects = models.Manager()

    def __str__(self):
        return self.plant_name
