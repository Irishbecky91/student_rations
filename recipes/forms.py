"""
Forms
"""
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Recipe Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Recipe
        fields = '__all__'
        