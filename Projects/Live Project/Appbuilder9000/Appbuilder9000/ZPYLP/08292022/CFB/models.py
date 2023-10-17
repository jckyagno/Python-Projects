from django.db import models


class AddFan(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    email = models.CharField(max_length=50, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name