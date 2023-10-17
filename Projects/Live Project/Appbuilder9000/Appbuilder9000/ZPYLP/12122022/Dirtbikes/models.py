from django.db import models

# Create your models here.


class Entry(models.Model):
    Year = models.IntegerField(max_length=50, default="", null=False)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)

    Entries = models.Manager()

    def __str__(self):
        return self.Make
