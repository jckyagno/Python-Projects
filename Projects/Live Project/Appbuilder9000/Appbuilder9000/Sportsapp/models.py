from django.db import models

# Create your models here.

class player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    goals_scored = models.IntegerField()

    # Defines the model Manager for Player
    players = models.Manager()

    # Allows references to a specific account to returned as the players name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Update model
UpdateTypes = [('Addscore', 'Addscore'), ('Subtractscore', 'Subtractscore')]
class update(models.Model):
    date = models.DateField
    full_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=UpdateTypes)
    reason = models.CharField(max_length=100)




