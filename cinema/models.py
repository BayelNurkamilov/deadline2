from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    release = models.DateField()
    actors = models.ManyToManyField(Actor)

