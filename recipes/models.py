"""
Models
"""
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


def unique_slugify(instance, slug):
    """
    creates a unique slug
    """
    model = Recipe
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=4)
    return unique_slug


class Recipe(models.Model):
    """
    Recipe model
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True)
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    serves = models.IntegerField()
    directions = models.TextField()
    ingredients = models.TextField(default="",
                                   blank=False, null=False)
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
        Ordering the recipes in created order,
        the '-' means in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    def amount_of_likes(self):
        """
        Return total amount of likes on a recipe
        """
        return self.likes.count()

    def get_absolute_url(self):
        """
        gets absolute url
        """
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def get_edit_url(self):
        """
        gets edit url
        """
        return reverse("edit_recipe", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """
        gets delete url
        """
        return reverse("delete_recipe", kwargs={"slug": self.slug})


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
