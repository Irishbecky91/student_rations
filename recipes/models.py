"""
Models
"""
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
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
    slug = models.SlugField(blank=False, null=False, default='author')
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
        Ordering our recipes in created order,
        the lack of '-' means in ascending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def amount_of_likes(self):
        """
        Retun total amount of likes on a recipe
        """
        return self.likes.count()

    def get_absolute_url(self):
        """
        gets absolute url
        """
        return reverse(
            "recipe:article_detail",
            kwargs={
                "author": self.author,
                "slug": self.slug
            }
        )

    def get_edit_url(self):
        """
        gets edit url
        """
        return reverse("recipes:update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """
        gets delete url
        """
        return reverse("recipes:delete", kwargs={"slug": self.slug})


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
