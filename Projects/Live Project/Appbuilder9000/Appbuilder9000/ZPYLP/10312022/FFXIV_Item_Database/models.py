from django.db import models
import datetime

from django.db.models import CharField

COLLECTION_FOCUS = [
    ('Gathering', 'Gathering'),
    ('Crafting', 'Crafting'),
    ('Raid Gear', 'Raid Gear'),
    ('Adventurer Island', 'Adventurer Island'),
    ('Housing', 'Housing'),
    ('Glamour', 'Glamour'),
    ('Questing', 'Questing'),
]


class ItemInfo(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Icon = models.CharField(max_length=255, null=False)
    Name = models.CharField(max_length=255, null=False)
    Url = models.CharField(max_length=255, null=False)

    items = models.Manager()

    def __str__(self):
        return self.Name


class Collection(models.Model):
    collection_name = models.CharField(max_length=50, null=False)
    collection_description = models.CharField(max_length=255, null=False)
    collection_created_author = models.CharField(max_length=50, null=False)
    collection_focus = models.CharField(max_length=50, choices=COLLECTION_FOCUS, null=False)

    collections = models.Manager()

    def __str__(self):
        return self.collection_name


