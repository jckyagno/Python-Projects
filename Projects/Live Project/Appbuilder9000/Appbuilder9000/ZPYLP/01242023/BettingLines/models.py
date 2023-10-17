from django.db import models
from django.forms import ModelForm
from django import forms

Sports_Selection = [
    ('MLB', 'MLB'),
    ('NFL', 'NFL'),
    ('NBA', 'NBA'),
    ('UFC', 'UFC'),
    ('BOXING', 'BOXING'),
    ('NcaaF', 'NcaaF'),
    ('Other', 'Other'),
]

Win_or_Lose = [
    ('Win', 'Win'),
    ('Lose', 'Lose'),
]


class Bet(models.Model):
    HomeTeam = models.CharField(max_length=80)
    AwayTeam = models.CharField(max_length=80, null=True)
    Sport = models.CharField(max_length=40, choices=Sports_Selection)
    Result = models.CharField(max_length=100, choices=Win_or_Lose)
    Wager = models.IntegerField(default="", null=True)
    Line = models.CharField(max_length=10, default="", null=True)

    # object management
    BettingLinesModel = models.Manager()

    # Returns the values
    def __str__(self):
        return self.HomeTeam
