"""
Views
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientFormSet


# Create your views here.
class CreateRecipe(View):
    """
    This creates the recipe form view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Displays recipe details in the view
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        form = RecipeForm()
        formset = IngredientFormSet()
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True    
            
        return render(request, 'create_recipe.html', {
            "form": form, "formset": formset
            })
    
    def post(self, request, slug, *args, **kwargs):
        """
        Submits form content to the database
        """
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/recipes/create')
        else:
            return render(request, 'create_recipe.html', {"form": form})


class RecipeLike(View):
    """
    Likes on a recipe
    """
