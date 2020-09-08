from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.name
