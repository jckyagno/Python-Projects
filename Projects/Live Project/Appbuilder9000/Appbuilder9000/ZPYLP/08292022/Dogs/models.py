from django.db import models

#drop down menu for dog sizes
DOG_SIZES = (
    ('X-small', 'Xtra-Small'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('X-large', 'Xtra-Large')
)

class Dogs(models.Model):
    name = models.CharField(max_length=60, null=False)
    breed = models.CharField(max_length=40)
    color = models.CharField(max_length=30)
    coat = models.CharField(max_length=30)
    size = models.CharField(max_length=20, choices=DOG_SIZES)

    Dog = models.Manager()

    def __str__(self):
        return self.name