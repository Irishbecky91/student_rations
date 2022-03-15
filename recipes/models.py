"""
Models
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """
    Recipe model
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='new_recipe',
        blank=True,
        null=True
    )
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    directions = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Ordering our recipes in created order,
        the lack of '-' means in ascending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def amount_of_likes(self):
        """
        Retun total amount of likes on a recipe
        """
        return self.likes.count()


class Ingredient(models.Model):
    """
    Ingredients model
    """
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=30, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="ingredients"
        )

    def __str__(self):
        """
        Returns a string showing the name.
        """
        return str(self.name)


class Comment(models.Model):
    """
    Comment class
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(max_length=75)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Ordering our posts in created order,
        the lack of '-' means in ascending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the authors name
        and the contact of the comment.
        """
        return f"Comment {self.body} by {self.name}"
