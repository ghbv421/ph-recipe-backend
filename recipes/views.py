from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Recipe
from .serializers import RecipeSerializer

# --- TASK 3: DATA LISTING ENDPOINT ---
@api_view(['GET'])
@permission_classes([AllowAny]) # Anyone can see the recipes on the dashboard
def get_recipes(request):
    """
    Returns the list of recipes (Arroz Caldo, Crispy Lechon, etc.)
    Aligned with the mobile UI Dashboard feature.
    """
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data) # Returns JSON response [cite: 11]

# --- TASK 3: DATA CREATION ENDPOINT ---
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # Requires a login to add new recipes
def add_recipe(request):
    """
    Enables adding new data through the API.
    Required for CRUD operations.
    """
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
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
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response(
            {"error": "Username and password are required."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response(
        {"message": "User created successfully", "id": user.id}, 
        status=status.HTTP_201_CREATED
    )

# --- OPTIONAL: PROTECTED VIEW FOR TESTING ---
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """
    Restricts access to authenticated users.
    Used to verify the login system works.
    """
    return Response({"message": f"Hello {request.user.username}, you are authorized!"})