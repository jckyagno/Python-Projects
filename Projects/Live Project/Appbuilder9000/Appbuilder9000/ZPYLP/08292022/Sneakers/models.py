from django.db import models

# Create your models here.
class Sneaker(models.Model):
    year = models.IntegerField()
    brand = models.CharField(max_length=30, blank=True, null=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)

    sneaker = models.Manager()

    def __str__(self):
        return self.name



