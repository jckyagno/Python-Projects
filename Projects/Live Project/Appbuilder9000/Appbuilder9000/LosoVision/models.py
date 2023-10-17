from django.db import models

# Create your models here.

# Patient information entry
class Patient_Entry(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    readingRx = models.CharField(max_length=5)

    Patient_Entries = models.Manager()
