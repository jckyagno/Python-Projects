from django.db import models
from datetime import date

Gender_options = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

class User(models.Model):
    Username = models.CharField(max_length = 40)
    Password = models.CharField(max_length = 40)
    Age = models.IntegerField(default='')
    Gender = models.CharField(default='', max_length=40, choices=Gender_options)
    Height = models.IntegerField(default='')
    Weight = models.IntegerField(default = '')
    BMI = models.FloatField()
    FatPercent = models.FloatField()
    Phase = models.CharField(max_length=40)
    Calories = models.IntegerField(default='')
    Protein = models.IntegerField(default='')

    Users = models.Manager()

    def __str__(self):
        return self.Username

class ChooseUser(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)