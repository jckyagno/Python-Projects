from django.db import models

# create model to input information
class Information(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    date = models.DateField()
    description = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.fname


