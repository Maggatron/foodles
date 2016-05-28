from __future__ import unicode_literals

from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = ListField(models.CharField(max_length=50))
    quantities = ListField(models.CharField(max_length=50))
    method = models.TextField()
