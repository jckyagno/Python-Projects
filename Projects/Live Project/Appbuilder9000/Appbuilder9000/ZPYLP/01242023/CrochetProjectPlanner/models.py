from django.db import models

TYPE_CHOICES = {
    ('clothing', 'clothing'),
    ('amigurumi', 'amigurumi'),
    ('furnishings', 'furnishings'),
    ('other', 'other'),
}

class Project(models.Model):
    project_name = models.CharField(max_length=60, default="", blank=True, null=False)
    item_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    yarn_weight = models.IntegerField(default="", blank=True, null=False)
    number_of_rolls = models.IntegerField(default="", blank=True, null=False)
    budget = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.project_name
