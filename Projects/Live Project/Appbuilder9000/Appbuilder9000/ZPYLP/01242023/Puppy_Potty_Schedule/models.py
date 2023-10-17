from django.db import models


# Create your models here.
Potty_Day = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

Potty_Type = [
    ('Number 1', 'Number 1'),
    ('Number 2', 'Number 2'),
]

# instantiating my model
class Schedule(models.Model):
    potty_day = models.CharField(max_length=10, choices=Potty_Day)
    potty_time = models.CharField(max_length=30, null=False)
    potty_type = models.CharField(max_length=10, choices=Potty_Type)
    potty_color = models.CharField(max_length=30, null=False)
    potty_description = models.CharField(max_length=40, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.potty_type



