from django.db import models


# Create your models here.
class Enter(models.Model):
    name = models.CharField(max_length=50, null=True, default='')
    team = models.CharField(max_length=50, null=True, default='')
    age = models.IntegerField(blank=True, null=True, default='')

    Entries = models.Manager()

    def __str__(self):
        return self.team


class Player(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    allstars = models.IntegerField()
    team = models.CharField(max_length=30)

    objects = models.Manager()

    #display data with name
    def __str__(self):
        return self.name
