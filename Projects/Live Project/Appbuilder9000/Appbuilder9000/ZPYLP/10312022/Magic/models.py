from django.db import models

# Create your models here.


class Deck(models.Model):
    commander = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    key_pieces = models.TextField(max_length=1000)
    image = models.CharField(max_length=1000)

    Deck = models.Manager()

    def __str__(self):
        return self.commander

class Comment(models.Model):
    deck = models.ForeignKey(Deck, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

