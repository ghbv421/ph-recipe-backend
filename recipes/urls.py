from django.urls import path
from rest_framework.authtoken import views as auth_views
from .views import get_recipes, add_recipe, register_user, get_categories

urlpatterns = [
    path('recipes/', get_recipes, name='get_recipes'), 
    path('recipes/add/', add_recipe, name='add_recipe'), 
    path('categories/', get_categories, name='get_categories'),
    path('register/', register_user, name='register_user'), 
    path('login/', auth_views.obtain_auth_token, name='api_token_auth'), 
]