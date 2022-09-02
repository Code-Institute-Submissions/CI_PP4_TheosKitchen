from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add Summernote to the admin panel for Recipe model and search fields.
    """
    list_display = (
                   'recipe_name', 'slug', 'status', 'author', 'featured'
                   )
    search_fields = ['recipe_name', 'author']
    prepopulated_fields = {'slug': ('recipe_name',)}
    list_filter = ('status', 'featured')
    summernote_fields = ('instructions', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Add search fields for Category in admin panel
    """
    list_display = ['title', ]
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields to search and approve Disscussion comments.
    """
    list_display = ('post', 'author', 'content', 'approved')
    list_filter = ('approved', 'author')
    search_fields = ('author',)
    actions = ['update_comment']

    def update_comment(self, request, queryset):
        queryset.update(approved=True)
