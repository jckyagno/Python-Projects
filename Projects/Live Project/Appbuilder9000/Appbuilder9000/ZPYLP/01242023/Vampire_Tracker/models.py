from django.db import models


class Vampire(models.Model):
    vampire_name = models.CharField(max_length=80)
    date_spotted = models.DateTimeField()
    where_spotted = models.CharField(max_length=20)
    evidence = models.CharField(max_length=1000)

    objects = models.Manager()

    def __str__(self):
        return self.vampire_name
