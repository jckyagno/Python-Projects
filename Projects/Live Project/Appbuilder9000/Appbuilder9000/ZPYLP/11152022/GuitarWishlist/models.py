from django.db import models

# Create your models here.
class GitFiddle(models.Model):
    list_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    strings = models.IntegerField()
    acoustic = models.CharField(max_length=30)
    frets = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    objects = models.Manager()


    def __str__(self):
        return self.list_name
