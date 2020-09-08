from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
