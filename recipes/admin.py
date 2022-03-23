"""
Admin
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Recipe Admin
    """
    list_display = ('title', 'author', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', )
    summernote = ('content', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class defines the appearance and control over the comments in
    the admin.
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']  # Allows approval of comments

    def approve_comments(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)
