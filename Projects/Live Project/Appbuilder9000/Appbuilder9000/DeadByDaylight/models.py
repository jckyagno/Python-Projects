from django.db import models


class Killer(models.Model):
    full_Name = models.CharField(max_length=100)
    movement_Speed = models.CharField(max_length=10)
    terror_Radius_Size = models.CharField(max_length=10)
    portrait_of_Killer = models.CharField(max_length=1000)
    image_Of_Killer = models.CharField(max_length=1000)
    release_Date = models.DateField()
    killer_Type = models.CharField(max_length=20, choices=[('ranged', 'Ranged'),
                                                         ('stealth', 'Stealth'),
                                                           ('melee', 'Melee')])
    lore = models.TextField()

    Killers = models.Manager()

    def __str__(self):
        return self.full_Name

class KillerPerk(models.Model):
    perk_One = models.CharField(max_length=30)
    image_Of_Perk_One = models.CharField(max_length=1000)
    perk_One_Description = models.TextField()
    perk_Two = models.CharField(max_length=30)
    image_Of_Perk_Two = models.CharField(max_length=1000)
    perk_Two_Description = models.TextField()
    perk_Three = models.CharField(max_length=30)
    image_Of_Perk_Three = models.CharField(max_length=1000)
    perk_Three_Description = models.TextField()

    KillerPerks = models.Manager()

    def __str__(self):
        return self.perk_One

class Survivor(models.Model):
    full_Name = models.CharField(max_length=100)
    portrait_of_Survivor = models.CharField(max_length=1000)
    image_Of_Survivor = models.CharField(max_length=1000)
    release_Date = models.DateField()
    lore= models.TextField()

    Survivors = models.Manager()

    def __str__(self):
        return self.full_Name

class SurvivorPerk(models.Model):
    perk_One = models.CharField(max_length=30)
    image_Of_Perk_One = models.CharField(max_length=1000)
    perk_One_Description = models.TextField()
    perk_Two = models.CharField(max_length=30)
    image_Of_Perk_Two = models.CharField(max_length=1000)
    perk_Two_Description = models.TextField()
    perk_Three = models.CharField(max_length=30)
    image_Of_Perk_Three = models.CharField(max_length=1000)
    perk_Three_Description = models.TextField()

    SurvivorPerks = models.Manager()

    def __str__(self):
        return self.perk_One