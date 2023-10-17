from django.db import models

# Choices for whether game has been played
PLAYED_CHOICES = {
    ('Yes', 'Yes'),
    ('No', 'No'),
}


# Model for adding board games to tracker
class BoardGames(models.Model):
    Game_Name = models.CharField(max_length=255, default="", null=False)
    Minimum_Players = models.IntegerField(default="", blank=True, null=False)
    Maximum_Players = models.IntegerField(default="", blank=True, null=False)
    Game_Type = models.CharField(max_length=255, default="", null=False)
    Estimated_Play_Time = models.CharField(max_length=255, default="", null=False)
    Have_We_Played = models.CharField(max_length=20, default="", choices=PLAYED_CHOICES)

    objects = models.Manager()

    # Display objects as the Game Name in string format
    def __str__(self):
        return self.Game_Name



