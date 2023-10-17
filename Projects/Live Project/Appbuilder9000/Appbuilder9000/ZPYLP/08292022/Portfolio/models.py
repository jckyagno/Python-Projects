from django.db import models
from django.forms import TextInput, EmailInput


TYPE_Topic = [
    ('Professional Inquiry', 'Professional Inquiry'),
    ('Questions', 'Questions'),
    ('Collaboration', 'Collaboration'),
    ('Other', 'Other'),
]


class ContactForm(models.Model):
    Name = models.CharField(max_length=60, default="Please enter your full name")
    Topic = models.CharField(max_length=30, choices=TYPE_Topic, default="Professional Inquiry")
    Email = models.EmailField(max_length=254)
    Message = models.CharField(max_length=500, default='Anything else you\'d like to say?')

    ContactForm = models.Manager()

    def __str__(self):
        return self.Name

class WeatherInfo(models.Model):
    Temperature = models.CharField(max_length=15)
    Condition = models.CharField(max_length=30)
    Time = models.DateTimeField(auto_now_add=True)
    City = models.CharField(max_length=30)

    WeatherInfo = models.Manager()

    def __str__(self):
        return self.date