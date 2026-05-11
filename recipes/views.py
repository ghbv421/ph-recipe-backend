import os
import json
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Category, Recipe
from .serializers import RecipeSerializer, CategorySerializer

# --- NEW: CATEGORY LISTING ENDPOINT ---
@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    """
    Returns the list of categories (Rice Dishes, Meat & Poultry, etc.)
    Fixes the ImportError and supports the CategoriesScreen fetch.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# --- READ: GET all recipes ---
@api_view(['GET'])
@permission_classes([AllowAny])
def get_recipes(request):
    recipes = Recipe.objects.all()
<<<<<<< Updated upstream
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

# --- TASK 3: DATA CREATION ENDPOINT ---
=======
    serializer = RecipeSerializer(recipes, many=True, context={'request': request})
    return Response(serializer.data)

# --- CREATE: POST new recipe ---
>>>>>>> Stashed changes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def add_recipe(request):
    """
<<<<<<< Updated upstream
    Enables adding new data through the API.
    Required for CRUD operations.
=======
    Creates a new recipe. 
    Uses a dictionary comprehension to avoid 'BufferedRandom' pickle errors 
    and manually parses the ingredients JSON string.
>>>>>>> Stashed changes
    """
    # 1. Manually build a mutable dictionary from request.data
    data = {k: v for k, v in request.data.items()}

    # 2. Force parse ingredients string into a list
    if 'ingredients' in data:
        raw_ingredients = data.get('ingredients')
        if isinstance(raw_ingredients, str):
            try:
                data['ingredients'] = json.loads(raw_ingredients)
            except (json.JSONDecodeError, ValueError):
                data['ingredients'] = []

    # 3. Serialize and Save
    serializer = RecipeSerializer(data=data, context={'request': request})
    if serializer.is_valid():
<<<<<<< Updated upstream
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- TASK 2: AUTHENTICATION (REGISTER) ---
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    User registration system.
    Creates a new Django User based on provided credentials.
    """
=======
        recipe = serializer.save()
        if recipe.image:
            recipe.image_key = os.path.basename(recipe.image.name)
            recipe.save(update_fields=['image_key'])
        return Response(RecipeSerializer(recipe, context={'request': request}).data, status=status.HTTP_201_CREATED)
    
    # Check this output in your terminal if it fails!
    print("DEBUG SERIALIZER ERRORS:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- UPDATE: PUT/PATCH existing recipe ---
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Build mutable dict
    data = {k: v for k, v in request.data.items()}

    if 'ingredients' in data and isinstance(data['ingredients'], str):
        try:
            data['ingredients'] = json.loads(data['ingredients'])
        except:
            pass

    serializer = RecipeSerializer(recipe, data=data, partial=True, context={'request': request})
    if serializer.is_valid():
        updated_recipe = serializer.save()
        if 'image' in request.FILES:
            updated_recipe.image_key = os.path.basename(updated_recipe.image.name)
            updated_recipe.save(update_fields=['image_key'])
        return Response(RecipeSerializer(updated_recipe, context={'request': request}).data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- DELETE: Remove recipe ---
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.image and os.path.isfile(recipe.image.path):
        os.remove(recipe.image.path)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# --- AUTH & PROTECTED ---
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
>>>>>>> Stashed changes
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"error": "Missing credentials"}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, password=password)
    return Response({"id": user.id}, status=status.HTTP_201_CREATED)

# --- OPTIONAL: PROTECTED VIEW FOR TESTING ---
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
<<<<<<< Updated upstream
    """
    Restricts access to authenticated users.
    """
    return Response({"message": f"Hello {request.user.username}, you are authorized!"})
=======
    return Response({"message": "Authorized", "user": request.user.username})
>>>>>>> Stashed changes
