from django.db import models

TYPE_CHOICE = {
    ('arms', 'arms'),
    ('legs', 'legs'),
    ('back', 'back'),
    ('abs', 'abs')
}


class Entry(models.Model):
    title = models.CharField(max_length=90, choices=TYPE_CHOICE)
    name = models.CharField(max_length=50, default="", blank=True, null=False)
    description = models.CharField(max_length=90)
    calories = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    Entries = models.Manager()

    def __str__(self):
        return self.name


