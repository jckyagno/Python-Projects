from django.db import models
from django import forms

# Create your models here.
class Release(models.Model):
    title = models.CharField(max_length=250)
    format = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    country = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    pf_rating = models.FloatField(null=True, blank=True)
    cover_image = models.URLField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stage_name = models.CharField(max_length=100)
    releases = models.ManyToManyField(Release)

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name