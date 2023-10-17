from django.db import models

# Create your models here.
ART_CATEGORYS = [
        ('AB', 'Abstract'),
        ('CL', 'Classical'),
        ('CT', 'Cartoon'),
        ('SM', 'Semi-Realistic'),
    ]

class onlineartists_add(models.Model):
    artist_name = models.CharField(max_length=30)
    artist_link = models.CharField(max_length=30)
    artist_genre = models.CharField(max_length=30, choices=ART_CATEGORYS)


    objects = models.Manager()
    def __str__(self):
        return self.artist_link
