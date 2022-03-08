"""
Models
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    """
    Recipe class
    """
    title = models.CharField(max_length=150)
    intro = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()

    def __str__(self):
        return self.title
