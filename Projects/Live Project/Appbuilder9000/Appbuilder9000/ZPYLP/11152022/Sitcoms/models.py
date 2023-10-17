from django.db import models


class Sitcom(models.Model):
    title = models.CharField(max_length=100, default="", blank=False, null=False)
    network = models.CharField(max_length=100, default="", blank=True, null=False)
    numberOfSeasons = models.CharField(max_length=3, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)

    Sitcoms = models.Manager()

    def __str__(self):
        return self.title


class SitcomCharacter(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    series = models.CharField(max_length=100, default="", blank=True, null=False)
    characterDescription = models.TextField(max_length=300, default="", blank=True)
    funQuotes = models.TextField(max_length=300, default="", blank=True)

    Characters = models.Manager()

    def __str__(self):
        return self.name


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date