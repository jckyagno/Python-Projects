from django.db import models
<<<<<<< HEAD

class Games(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    release_date = models.DateField()
    age_rating = models.CharField(max_length=50)

    Games = models.Manager()
=======
>>>>>>> caccb1ced4cb3e830fd65288787b0cb1b272534c
