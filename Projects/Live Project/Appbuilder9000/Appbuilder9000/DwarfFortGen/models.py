from django.db import models

# Create your models here.
SKIN_CHOICES = {
    ('meat', 'meat'),
    ('metal', 'metal'),
    ('fungus', 'fungus'),
    ('scale', 'scale'),
    ('gem', 'gem'),
}

BEAST_CHOICES = {
    ('unknown', 'unknown'),
    ('canine', 'canine'),
    ('feline', 'feline'),
    ('reptilian', 'reptilian'),
    ('avian', 'avian'),
    ('amphibian', 'amphibian'),
}

POWER_CHOICES = {
    ('ominous presence', 'ominous presence'),
    ('deadly dust', 'deadly dust'),
    ('menacing spikes', 'menacing spikes'),
    ('firey breath', 'firey breath'),
    ('sticky webs', 'sticky webs'),
}


class Beast(models.Model):
    name = models.CharField(max_length=60, default="", null=False)
    title = models.CharField(max_length=60, default="Forgotten Beast")
    skin = models.CharField(max_length=60, choices=SKIN_CHOICES)
    species = models.CharField(max_length=60, choices=BEAST_CHOICES)
    power = models.CharField(max_length=60, choices=POWER_CHOICES)
    encounter = models.DateField(auto_now=True)
    sentient = models.BooleanField()
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)

    Beasts = models.Manager()

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(max_length=60, default="", null=False)
    type = models.CharField(max_length=60, default="", null=False)
    size = models.CharField(max_length=60, default="", null=False)
    HP = models.IntegerField(default=0)

    Monsters = models.Manager()

    def __str__(self):
        return self.name
