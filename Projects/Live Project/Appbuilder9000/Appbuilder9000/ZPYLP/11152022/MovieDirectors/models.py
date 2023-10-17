from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, default="", null=False)
    numberOfMovies = models.IntegerField()
    yearOfFirstMovie = models.IntegerField()
    primaryGenre = models.CharField(max_length=100, default="")
    deceased = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name
