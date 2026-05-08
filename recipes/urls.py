# recipes/urls.py
from django.urls import path
from rest_framework.authtoken import views as auth_views
from .views import get_recipes, add_recipe, register_user

urlpatterns = [
    # Do NOT use '/recipes/'. Use 'recipes/'
    path('recipes/', get_recipes, name='get_recipes'), 
    path('recipes/add/', add_recipe, name='add_recipe'), 
    path('register/', register_user, name='register_user'), 
    path('login/', auth_views.obtain_auth_token, name='api_token_auth'), 
]