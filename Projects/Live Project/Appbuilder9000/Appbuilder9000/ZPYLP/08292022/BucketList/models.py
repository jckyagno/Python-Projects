from django.db import models
from django.forms import ModelForm

# User choices for month
MONTH_CHOICES = {
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
}

# Created a class for bucketlist items
class bucketItem(models.Model):
    month = models.CharField(max_length=30, choices=MONTH_CHOICES)
    activity = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    required_items = models.CharField(max_length=30)

    # creates model manager
    objects = models.Manager()

    def __str__(self):
        return self.activity









