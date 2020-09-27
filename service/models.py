from django.db import models


# Create your models here.

class Mountain(models.Model):
    name = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    altitude = models.FloatField()
