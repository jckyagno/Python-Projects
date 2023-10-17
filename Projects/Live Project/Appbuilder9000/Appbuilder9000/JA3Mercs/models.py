from django.db import models
from django import forms


# Choices for training property.
TRAINING_CHOICES = {
    ('Mechanical','Mechanical'),
    ('Marksmanship','Marksmanship'),
    ('All-Rounder','All-Rounder'),
    ('Explosives','Explosives'),
    ('Medical','Medical'),
    ('Leadership','Leadership'),
}




class Merc(models.Model):
    image = models.CharField(max_length=255, default="", blank=True)
    fname = models.CharField(max_length=60, default="", blank=True, null=False)
    lname = models.CharField(max_length=60, default="", blank=True, null=False)
    callsign = models.CharField(max_length=60, default="", blank=True, null=False)
    training = models.CharField(max_length=60, default="", blank=True, null=False, choices=TRAINING_CHOICES)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default="", blank=True, null=False)
    description = models.CharField(max_length=300, default="", blank=True, null=False)



    objects = models.Manager()

    def __str__(self):
        return self.callsign