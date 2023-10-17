from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Creating model for review, includes name, date, title, review score, and description/review text
# game_score uses PositiveIntegerField to ensure positive numbers only, and validators ensure number from 1 to 10


class Review(models.Model):
    game_title = models.CharField(max_length=50)
    game_score = models.PositiveIntegerField(default=1)
    review_text = models.TextField(default='')
    reviewer_name = models.CharField(max_length=50)
    date_reviewed = models.DateField()

    # Object manager
    Reviews = models.Manager()

    # Displays game title and reviewer name
    def __str__(self):
        return str(self.game_title) + " review by " + str(self.reviewer_name)
