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


# =========================
# CATEGORY ENDPOINT
# =========================
@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# =========================
# GET RECIPES
# =========================
@api_view(['GET'])
@permission_classes([AllowAny])
def get_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True, context={'request': request})
    return Response(serializer.data)


# =========================
# CREATE RECIPE
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def add_recipe(request):

    data = {k: v for k, v in request.data.items()}

    if 'ingredients' in data and isinstance(data['ingredients'], str):
        try:
            data['ingredients'] = json.loads(data['ingredients'])
        except (json.JSONDecodeError, ValueError):
            data['ingredients'] = []

    serializer = RecipeSerializer(data=data, context={'request': request})

    if serializer.is_valid():
        recipe = serializer.save()

        if recipe.image:
            recipe.image_key = os.path.basename(recipe.image.name)
            recipe.save(update_fields=['image_key'])

        return Response(
            RecipeSerializer(recipe, context={'request': request}).data,
            status=status.HTTP_201_CREATED
        )

    print("DEBUG SERIALIZER ERRORS:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# REGISTER USER
# =========================
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"error": "Missing credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password)

    return Response(
        {"id": user.id},
        status=status.HTTP_201_CREATED
    )


# =========================
# UPDATE RECIPE
# =========================
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def update_recipe(request, pk):

    recipe = get_object_or_404(Recipe, pk=pk)
    data = {k: v for k, v in request.data.items()}

    if 'ingredients' in data and isinstance(data['ingredients'], str):
        try:
            data['ingredients'] = json.loads(data['ingredients'])
        except:
            pass

    serializer = RecipeSerializer(recipe, data=data, partial=True, context={'request': request})

    if serializer.is_valid():
        updated = serializer.save()

        if 'image' in request.FILES:
            updated.image_key = os.path.basename(updated.image.name)
            updated.save(update_fields=['image_key'])

        return Response(
            RecipeSerializer(updated, context={'request': request}).data
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# DELETE RECIPE
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_recipe(request, pk):

    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.image and os.path.isfile(recipe.image.path):
        os.remove(recipe.image.path)

    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# =========================
# PROTECTED TEST VIEW
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "message": "Authorized",
        "user": request.user.username
    })