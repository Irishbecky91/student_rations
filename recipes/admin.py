"""
Admin
"""
"""
This is the admin.py page
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Ingredient


# Register your models here.
class IngredientInline(admin.TabularInline):
    """
    Ingredient Inline
    """
    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Recipe Admin
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    searcf_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote = ('content')
    inlines = [IngredientInline, ]
