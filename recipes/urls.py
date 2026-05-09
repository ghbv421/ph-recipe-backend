from django.urls import path
from .views import get_recipes, add_recipe, register_user, get_categories

urlpatterns = [
    # Recipe Endpoints
    path('recipes/', get_recipes),           # Endpoint: /api/recipes/ 
    path('recipes/add/', add_recipe),       # Endpoint: /api/recipes/add/ 
    
    # Category Endpoints
    path('categories/', get_categories),     # Endpoint: /api/categories/
    
    # Auth Endpoints
    path('register/', register_user),        # Endpoint: /api/register/
]