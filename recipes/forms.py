"""
Forms
"""
from django import forms
from django.forms import ModelForm
from .models import Recipe, Comment


class RecipeForm(ModelForm):
    """
    Recipe Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Recipe
        fields = [
            'title',
            'description',
            'serves',
            'prep_time',
            'cook_time',
            'directions',
            'ingredients'
        ]

    def clean_servings(self):
        """
        Ensures servings is greater than zero
        """
        value = self.cleaned_data.get("serves")
        print(value)
        if value < 1:
            raise forms.ValidationError(
                "The number of servings must be greater than zero"
                )
        return value


class CommentForm(forms.ModelForm):
    """
    Comment Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)
