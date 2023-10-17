from django.db import models

TYPE_CHOICES = {
    ('red','red'),
    ('blue','blue'),
    ('green','green'),
    ('yellow','yellow'),
    ('pink','pink'),
    ('purple','purple'),
    ('white','white'),
    ('black','black'),
    ('rainbow','rainbow'),
    ('N/A','N/A'),
}


class Gift(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name


class ChristmasJoke(models.Model):
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    Jokes = models.Manager()

    def __str__(self):
        return self.date


