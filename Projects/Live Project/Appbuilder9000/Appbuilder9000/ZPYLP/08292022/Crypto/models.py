from django.db import models

CRYPTO_RATING = [
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
]


# instantiating my model
class AddCrypto(models.Model):
    crypto_name = models.CharField(max_length=100, null=False)
    ticker_symbol = models.CharField(max_length=100, null=False)
    crypto_rating = models.CharField(max_length=20, choices=CRYPTO_RATING)

    objects = models.Manager()

    def __str__(self):
        return self.ticker_symbol
