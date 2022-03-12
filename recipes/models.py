"""
Models
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Recipe(models.Model):
    """
    Recipe model
    """
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='new_recipe'
    )
    updated_on = models.DateTimeField(auto_now=True)
    directions = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    """
    Ingredients model
    """
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=30, blank=True)
    quantity = models.FloatField()

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="ingredients"
        )
