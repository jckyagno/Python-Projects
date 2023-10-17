from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    release_date = models.DateField()
    age_rating = models.CharField(max_length=50)

    Games = models.Manager()
    def __str__(self):
        return self.title + ' ' + self.description + ' ' + self.release_date + ' ' + self.age_rating