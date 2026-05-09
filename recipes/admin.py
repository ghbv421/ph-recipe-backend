from django.contrib import admin
from .models import Recipe, Category

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Field order when editing
    fields = ('name', 'image_key', 'category', 'rating', 'time', 'ingredients')
    
    # Columns shown in the main list view
    list_display = ('name', 'category', 'rating', 'time')
    
    # Sidebar filters
    list_filter = ('category',)
    
    # Search bar for quick lookup
    search_fields = ('name', 'ingredients')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Controls the order when editing
    fields = ('name', 'image_key')
    
    # Shows both the name and the image key in the list view
    list_display = ('name', 'image_key')
    
    # Allows you to click the name or the image_key to open the edit page
    list_display_links = ('name',)