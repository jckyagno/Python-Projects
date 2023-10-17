from django.db import models

Music_GENRE = [
    ('Blues', 'Blues'),
    ('Country', 'Country'),
    ('Easy Listening', 'Easy Listening '),
    ('Electronic', 'Electronic'),
    ('Hip hop', 'Hip hop'),
    ('Jazz', 'Jazz'),
    ('Pop', 'Pop'),
    ('R&B and Soul', 'R&B and Soul'),
    ('Rock', 'Rock'),
    ('Metal', 'Metal'),
    ('Punk', 'Punk'),
    ('African', 'African'),
    ('Eastern Europe', 'Eastern Europe'),
    ('Asian', 'Asian'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Caribbean and Caribbean-influenced', 'Caribbean and Caribbean-influenced'),
    ('Latin', 'Latin'),
    ('Religious', 'Religious'),
    ('Traditional Folk', 'Traditional Folk'),
    ('Other', 'Other'),


]

Music_RATING = [
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
]


# instantiating my model
class AddMusic(models.Model):
    music_genre = models.CharField(max_length=20, choices=Music_GENRE)
    music_title = models.CharField(max_length=100, null=False)
    music_Composer = models.CharField(max_length=100, null=False)
    music_description = models.CharField(max_length=100, null=False)
    Music_RATING = models.CharField(max_length=20, choices=Music_RATING)

    objects = models.Manager()

    def __str__(self):
        return self.music_title


class FavoriteMusic(models.Model):
    Title = models.CharField(max_length=100, null=False)
    Composer = models.CharField(max_length=100, null=False)
    Rating = models.CharField(max_length=100, null=False)
    Source = models.CharField(max_length=100, null=False)

    Favorite_Music = models.Manager()

    def __str__(self):
        return self.Title
# Create your models here.
