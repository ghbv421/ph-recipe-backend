from django.contrib import admin
from .models import Recipe, Category

# Option A: Using the decorator for Recipe to control field order
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # This controls the order of fields when you click on a recipe to edit it
    fields = ('name', 'image_key', 'category', 'rating', 'time', 'ingredients')
    
    # Optional: Adds columns to the list view so you can see info at a glance
    list_display = ('name', 'category', 'rating', 'time')
    # Optional: Adds a filter sidebar for categories
    list_filter = ('category',)

# Option B: Simple registration for Category
admin.site.register(Category)