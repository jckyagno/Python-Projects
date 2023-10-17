from django.db import models

ActivitiesType = {
    ('Beach', 'Beach'),
    ('Downtime', 'Downtime'),
    ('Eating Out', 'Eating out'),
    ('Exercise', 'Exercise'),
    ('Shopping', 'Shopping'),
    ('Sightseeing', 'Sightseeing'),
    ('Sports', 'Sports'),
    ('Walk/Hike', 'Walk/Hike'),
    ('Work', 'Work'),
}

# Creating models and what's allowed to be inputted/chosen
class Entry(models.Model):
    destination = models.CharField(max_length=30, default="")
    activity = models.CharField(max_length=50, default="", choices=ActivitiesType)
    activity_date_and_time = models.DateTimeField(default="")
    activity_details = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=7, decimal_places=2, default="", verbose_name="Cost/Budget in $")

    Entries = models.Manager()

    def __str__(self):
        return self.activity + " - " + self.activity_date_and_time

