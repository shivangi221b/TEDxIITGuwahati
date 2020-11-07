from django.db import models


class Speaker(models.Model):
    nominator_name = models.CharField(max_length=200)
    nominee_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    nominee_about = models.TextField()
    talk_about = models.TextField()
    social_links = models.TextField()
    # know_speaker = models.TextField()
    know_speaker_description = models.TextField()
    spoken_publicly_links = models.TextField()

    def __str__(self):
        return self.nominee_name
