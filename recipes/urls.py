from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.CreateRecipe.as_view(), name='create_recipes'),
    path('like/<slug:slug>', views.RecipeLike, name='recipe_like'),
]
