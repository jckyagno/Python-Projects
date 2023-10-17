from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('Hero', 'Hero'),
    ('Villain', 'Villain'),
}


class Character(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100, default="", blank=True, null=False)
    description = models.TextField(max_length=100, default="", blank=True)
    image = models.CharField(max_length=255, default='', blank=True)

    Characters = models.Manager()

    def __str__(self):
        return self.name


class Comment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Quote(models.Model):
    quote = models.TextField(max_length=500)
    speaker = models.TextField(max_length=500)

    Quotes = models.Manager()

    def __str__(self):
        return 'Quote {}' .format(self.quote)

