from django.db import models

class Vehicle(models.Model):
    vehicle_make = models.CharField(max_length=30)
    vehicle_model = models.CharField(max_length=30)
    vehicle_year = models.IntegerField(blank=True, default='')
    vehicle_color = models.CharField(max_length=15)

    vehicles = models.Manager()

    def __str__(self):
        return self.vehicle_model


