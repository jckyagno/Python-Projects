from django.db import models

# Create your models here.

from django.db import models

CRYPTO_SENTIMENT = [
    ('Bullish', 'Bullish'),
    ('Bearish', 'Bearish'),
    ('Neutral', 'Neutral'),
]


# instantiating my model
class Review(models.Model):
    user = models.CharField(max_length=50, null=False)
    crypto = models.CharField(max_length=50, null=False)
    ticker = models.CharField(max_length=10, null=False)
    price = models.DecimalField(default=0.00, max_digits=1000000, decimal_places=2, null=False)
    body = models.TextField(max_length=1000, null=False)
    rating = models.CharField(max_length=10, choices=CRYPTO_SENTIMENT, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.user
