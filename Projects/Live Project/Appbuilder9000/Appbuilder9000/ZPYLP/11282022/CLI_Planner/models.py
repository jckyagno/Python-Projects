from django.db import models
from django.db.models import Manager
from django.http import HttpResponse
from django.views.generic import TemplateView


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.event_name