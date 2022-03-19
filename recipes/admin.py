"""
Admin
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Recipe Admin
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote = ('content')
