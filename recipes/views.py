"""
Views
"""
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Ingredient
from .forms import CommentForm


# Create your views here.
def about(request):
    """
    renders about page
    """
    return render(request, "about.html")


class RecipeList(generic.ListView):
    """
    This class creates the recipe list
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    This creates the recipe view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Displays recipe details in the view
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        ingredients = Ingredient.objects.all()
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe.html',
            {
                "recipe": recipe,
                'ingredients': ingredients,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Submits form content to the database
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class RecipeLike(View):
    """
    Likes on a recipe
    """
    def post(self, request, slug):
        """
        Submits to view
        """
        recipe = get_object_or_404(Recipe(), slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
