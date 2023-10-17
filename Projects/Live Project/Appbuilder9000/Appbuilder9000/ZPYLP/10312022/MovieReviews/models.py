from django.db import models
from django import forms
# Create your models here.
# class movie created, with a title field, rating field (as integer), and review field (text up to 240 char)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(max_length=240, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.model


class Weather(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    Weather = models.Manager()

    def __str__(self):
        return self.date