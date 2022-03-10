"""
Views
"""
from django.shortcuts import render, redirect
from .forms import RecipeForm


# Create your views here.
def create_recipe(request):
    """
    This creates the recipe form view
    """
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'create_recipe.html', {"form": form})
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'create_recipe.html', {"form": form})
