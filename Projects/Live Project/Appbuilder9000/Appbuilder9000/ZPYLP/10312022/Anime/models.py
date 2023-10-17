from django.db import models
from django.db.models import Manager


class Ani(models.Model):
    TYPE_CHOICES = {
        ('Movie', 'Movie'),
        ('OVA', 'OVA'),
        ('ONA', 'ONA'),
        ('TV Series', 'TV Series'),
        ('Other', 'Other'),
    }

    GENRE_CHOICES = {
        ('Action / Adventure', 'Action / Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama / Mystery', 'Drama / Mystery'),
        ('Horror / Suspense', 'Horror / Suspense'),
        ('Romance / Slice of Life', 'Romance / Slice of Life'),
        ('Fantasy / Sci-Fi / Supernatural', 'Fantasy / Sci-Fi / Supernatural'),
        ('Sports', 'Sports'),
    }

    RATE_CHOICES = {
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    }

    title = models.CharField(max_length=150, default="", blank=False, null=False, unique=True)
    type = models.CharField(max_length=60, default="", choices=TYPE_CHOICES)
    genre = models.CharField(max_length=60, default="", choices=GENRE_CHOICES)
    rating = models.CharField(max_length=1, default="", choices=RATE_CHOICES, help_text="5 = Highest")
    review = models.CharField(max_length=500, default="", blank=True)
    image = models.CharField(max_length=255, default="", blank=True)

    animes = models.Manager()

    def __str__(self):
        return self.title
