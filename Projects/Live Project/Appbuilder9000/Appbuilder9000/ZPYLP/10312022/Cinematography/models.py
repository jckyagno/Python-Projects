from django.db import models


TYPE_SENSOR = {
    ('Medium', 'Medium'),
    ('Full_Frame', 'Full_Frame'),
    ('APS-C', 'APS-C'),
    ('M4/3', 'M4/3'),
}

FOCAL_LENGTH = {
    ('24mm', '24mm'),
    ('35mm', '35mm'),
    ('50mm', '50mm'),
    ('85mm', '85mm'),
}


class FieldOfView(models.Model):
    sensorSize = models.CharField(max_length=10, choices=TYPE_SENSOR)
    lensFocal = models.CharField(max_length=5, choices=FOCAL_LENGTH)
    manufacturer = models.CharField(max_length=15, default='')

    Camera = models.Manager()

    def __str__(self):
        return self.manufacturer
