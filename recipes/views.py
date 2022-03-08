"""
Views
"""
from django.shortcuts import render
from .forms import RecipeForm


# Create your views here.
def create_recipe(request):
    """
    This creates the recipe form view
    """
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'create_recipe.html', {"form": form})
