from django.db import models


CATEGORY_CHOICES = [
    ('Inorganic Salt', 'Inorganic Salt'),
    ('Organic Salt', 'Organic Salt'),
    ('Acid', 'Acid'),
    ('Base', 'Base'),
    ('Surfactant', 'Surfactant'),
    ('Solvent', 'Solvent'),
    ('Finished Product', 'Finished Product'),
    ('Other', 'Other'),
]

HAZARD_CHOICES = [
    ('Toxic', 'Toxic'),
    ('Corrosive', 'Corrosive'),
    ('Reactive', 'Reactive'),
    ('Flammable', 'Flammable'),
    ('None', 'None'),
]

class Material(models.Model):
    material_name = models.CharField(max_length=200)
    chemical_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=30)
    amount = models.FloatField()
    chemical_description = models.CharField(max_length=300)
    hazards = models.CharField(max_length=30, choices=HAZARD_CHOICES)

    Materials = models.Manager()

    def __str__(self):
        return self.material_name
