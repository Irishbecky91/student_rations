"""
Views
"""
from django.shortcuts import render, redirect
from .forms import RecipeForm, IngredientFormSet


# Create your views here.
def create_recipe(request):
    """
    This creates the recipe form view
    """
    if request.method == "GET":
        form = RecipeForm()
        formset = IngredientFormSet()
        return render(request, 'create_recipe.html', {
            "form": form, "formset": formset
            })
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/recipes/create')
        else:
            return render(request, 'create_recipe.html', {"form": form})
