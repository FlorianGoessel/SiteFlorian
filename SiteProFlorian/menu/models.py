from django.db import models


class Sons(models.Model):
    titre = models.CharField(max_length=50)
    plugin = models.CharField(max_length=500)
    beatmaker = models.CharField(max_length=100)
    date = models.DateTimeField ()
    cover = models.ImageField(null=True, blank=False, upload_to='images/')
    explicitcontent = models.BooleanField(default=False)

    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20, default=3)

    def __str__(self):
        return self.titre
