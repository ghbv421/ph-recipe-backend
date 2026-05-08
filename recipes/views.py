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
@permission_classes([AllowAny]) 
def get_recipes(request):
    """
    Returns the list of recipes (Arroz Caldo, Crispy Lechon, etc.)
    Aligned with the mobile UI Dashboard feature.
    """
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    # Task 3: Returns 200 OK by default with JSON data
    return Response(serializer.data) 

# --- TASK 4: DATA CREATION ENDPOINT ---
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def add_recipe(request):
    """
    Enables adding new data through the API.
    Task 7: Demonstrates Frontend -> API -> Database flow.
    """
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Task 7 & 8: Explicitly returns 201 Created
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Task 8: Returns 400 Bad Request if input is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- TASK 6: AUTHENTICATION (REGISTER) ---
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    User registration system for Task 6.
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """
    Task 6: Verifies that Token Authentication is working.
    """
    return Response({"message": f"Hello {request.user.username}, you are authorized!"})