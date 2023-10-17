from django.db import models

# Create your models here.

stackChoices = {
    ('Full-Stack','Full-Stack'),
    ('Front-End','Front-End'),
    ('Back-End','Back-End'),
    ('Unknown','Unknown'),
}

isStartup = {
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Unknown', 'Unknown'),
}


class Jobs(models.Model):
    title = models.CharField(max_length=60, default="")
    company = models.CharField(max_length=30, default="")
    stack = models.CharField(max_length=15, choices=stackChoices)
    startup = models.CharField(max_length=8, choices=isStartup)
    location = models.CharField(max_length=30)
    exp_required = models.CharField(max_length=30)
    minimum_pay = models.CharField(max_length=30)
    maximum_pay = models.CharField(max_length=30)
    date_added = models.DateField()
    job_url = models.CharField(max_length=200, default="")

    objects = models.Manager()

    def __str__(self):
        return self.title

class Temp(models.Model):
    title = models.CharField(max_length=60, default="")
    company = models.CharField(max_length=30, default="")
    minimum_pay = models.CharField(max_length=30)
    maximum_pay = models.CharField(max_length=30)
    date_added = models.DateField()
    job_url = models.CharField(max_length=200, default="")

    objects = models.Manager()

    def __str__(self):
        return self.title