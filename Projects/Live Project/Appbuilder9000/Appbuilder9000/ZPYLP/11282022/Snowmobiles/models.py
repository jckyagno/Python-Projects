from django.db import models
from django.db.models import Q
from datetime import date


class SnowmobileQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(make__icontains=query) |
                         Q(model__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class SnowmobileManager(models.Manager):
    def get_queryset(self):
        return SnowmobileQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Snowmobile(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    dateManufactured = models.DateField()
    description = models.TextField(max_length=300, default="", blank=True)

    objects = SnowmobileManager()

    def __str__(self):
        return self.model


class DealerQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(brand__icontains=query) |
                         Q(store_name__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class DealerManager(models.Manager):
    def get_queryset(self):
        return DealerQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Dealer(models.Model):
    brand = models.CharField(max_length=60)
    store_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)

    objects = DealerManager()

    def __str__(self):
        return self.store_name


class Weather(models.Model):
    temp = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.date
