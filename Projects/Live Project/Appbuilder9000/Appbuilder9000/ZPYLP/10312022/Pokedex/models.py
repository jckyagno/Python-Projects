from django.db import models
from .game import *


class CreateUser(models.Model):
    first_name = models.CharField(max_length=99,  default=" ")
    trainer_name = models.CharField(max_length=25, blank=True, default="", null=False) #+clean() to validate?
    starter_pokemon = models.CharField(max_length=25, blank=False)
    nickname = models.CharField(max_length=25, blank=True, default="N/A")
    level = models.PositiveSmallIntegerField(default="From level 1 to 100")
    nature = models.CharField(choices=NATURE, default=1, max_length=25)
    game = models.CharField(choices=BASE_GAME, default=1, max_length=64)

    CreateUser = models.Manager()

    def __str__(self):
        return self.trainer_name


class AddPokemon(models.Model):
    trainer_name = models.ForeignKey(CreateUser, on_delete=models.CASCADE)
    pokemon_name = models.CharField(max_length=25, blank=False, null=False)
    nickname = models.CharField(max_length=25, blank=True)
    level = models.PositiveSmallIntegerField(default=1)
    nature = models.CharField(choices=NATURE, default=1,max_length=25)
    game = models.CharField(choices=BASE_GAME, default=1,max_length=64)



    #defines manager for Pokemon class
    Pokemon = models.Manager()

    def __str__(self):
        return self.name


