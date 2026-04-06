from django.contrib import admin
from .models import Recipe

# This line tells Django to show the Recipes table in the admin panel
admin.site.register(Recipe)