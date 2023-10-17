from django.db import models

# choices for islands and type of activity
islands = [('Hokkaido', 'Hokkaido'), ('Honshu', 'Honshu'), ('Kyushu', 'Kyushu'),
           ('Shikoku', 'Shikoku'), ('Okinawa', 'Okinawa')]
addTypes = [('Restaurant', 'Restaurant'), ('Sightseeing', 'Sightseeing'), ('Festival', 'Festival'), ('Other', 'Other')]


class AddEntry(models.Model):
    name_of_Place = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    island = models.CharField(max_length=8, choices=islands)
    activity_Type = models.CharField(max_length=15, choices=addTypes)
    description = models.TextField(max_length=500)
    addDate = models.DateTimeField(auto_now_add=True)

    AddEntries = models.Manager()

    def __str__(self):
        return self.name_of_Place
