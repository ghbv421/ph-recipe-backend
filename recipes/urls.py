from django.urls import path
from rest_framework.authtoken import views # Import this for tokens
from .views import get_recipes, add_recipe, register_user

urlpatterns = [
    path('recipes/', get_recipes), 
    path('recipes/add/', add_recipe), 
    path('register/', register_user), 
    # ADD THIS LINE:
    path('login/', views.obtain_auth_token), # Endpoint: /api/login/
]