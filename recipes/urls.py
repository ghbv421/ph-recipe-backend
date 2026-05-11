from django.urls import path
<<<<<<< Updated upstream
from .views import get_recipes, add_recipe, register_user, get_categories

urlpatterns = [
    # Recipe Endpoints
    path('recipes/', get_recipes),           # Endpoint: /api/recipes/ 
    path('recipes/add/', add_recipe),       # Endpoint: /api/recipes/add/ 
    
    # Category Endpoints
    path('categories/', get_categories),     # Endpoint: /api/categories/
    
    # Auth Endpoints
    path('register/', register_user),        # Endpoint: /api/register/
=======
from rest_framework.authtoken import views as auth_views
# Added update_recipe to the import list
from .views import get_recipes, add_recipe, update_recipe, delete_recipe, register_user, protected_view

urlpatterns = [
    # READ — public
    path('recipes/', get_recipes, name='get_recipes'),

    # CREATE — requires token
    path('recipes/add/', add_recipe, name='add_recipe'),

    # UPDATE — requires token (Matches the frontend fetch URL)
    path('recipes/<int:pk>/update/', update_recipe, name='update_recipe'),

    # DELETE — requires token
    path('recipes/<int:pk>/delete/', delete_recipe, name='delete_recipe'),

    # AUTH
    path('register/', register_user, name='register_user'),
    path('login/', auth_views.obtain_auth_token, name='api_token_auth'),

    # PROTECTED TEST
    path('protected/', protected_view, name='protected_view'),
>>>>>>> Stashed changes
]