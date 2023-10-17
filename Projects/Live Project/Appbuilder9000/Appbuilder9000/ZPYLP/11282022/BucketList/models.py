from django.db import models

# Create your models here.

COMPLETED_CHOICES = {
    ('Yes','Yes'),
    ('No','No'),
}
class Item(models.Model):
    Activity = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Completed = models.CharField(max_length=60, choices=COMPLETED_CHOICES, default='No')



    Items = models.Manager()

    def __str__(self):
        return self.Activity

