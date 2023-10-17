from django.db import models

# Creates the model for the recipe
class Recipe(models.Model):
    title_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    number_of_ingredients = models.IntegerField()
    making_time = models.IntegerField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title_name


