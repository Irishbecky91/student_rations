"""
Forms
"""
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
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
            'ingredients',
            'directions',
            'featured_image',
        ]
        widgets = {
            'directions': SummernoteInplaceWidget(),
            'ingredients': SummernoteInplaceWidget()
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

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
