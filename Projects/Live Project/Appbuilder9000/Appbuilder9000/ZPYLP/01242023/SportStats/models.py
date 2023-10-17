from django.db import models



class PlayerModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    player_points = models.IntegerField(blank=True, default='')
    player_assists = models.IntegerField(blank=True, default='')

    PlayerModels = models.Manager()
    def __str__(self):
        return self.last_name