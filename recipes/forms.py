"""
Forms
"""
from django import forms
from .models import Recipe, Ingredient, Comment


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

    def clean_servings(self):
        """
        Ensures servings is greater than zero
        """
        value = self.cleaned_data.get("servings")
        print(value)
        if value < 1:
            raise forms.ValidationError(
                "The number of servings must be greater than zero"
                )
        return value


class IngredientForm(forms.ModelForm):
    """
    Ingredients Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Ingredient
        exclude = ('recipe',)


IngredientFormSet = forms.inlineformset_factory(
    Recipe, Ingredient, form=IngredientForm
    )


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
