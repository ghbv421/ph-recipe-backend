from django.urls import path
from .views import get_recipes, add_recipe, register_user

urlpatterns = [
    path('recipes/', get_recipes), # Endpoint: /api/recipes/ 
    path('recipes/add/', add_recipe), # Endpoint: /api/recipes/add/ 
    path('register/', register_user), # Endpoint: /api/register/
]