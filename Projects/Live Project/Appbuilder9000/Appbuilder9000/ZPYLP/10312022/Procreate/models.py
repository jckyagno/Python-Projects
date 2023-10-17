from django.db import models

# Create your models here.

SOCIAL_MEDIA_CHOICES = {
    ('Instagram', 'Instagram'),
    ('Facebook', 'Facebook'),
    ('Pintrest', 'Pintrest'),
    ('TikTok', 'Tiktok'),
    ('Tumblr', 'Tumblr'),
    ('Youtube', 'Youtube'),
}
class Procreate(models.Model):
    social_media = models.CharField(max_length=60, choices=SOCIAL_MEDIA_CHOICES)
    artist_name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    image = models.CharField(max_length=255, default="", blank=True)

    ProcreateArt = models.Manager()


    def __str__(self):
        return self.artist_name