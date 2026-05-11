from rest_framework import serializers
from .models import Recipe, Category


# =========================
# CATEGORY SERIALIZER
# =========================
class CategorySerializer(serializers.ModelSerializer):
    recipe_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_key', 'recipe_count']

    def get_recipe_count(self, obj):
        # counts related recipes in this category
        return obj.recipes.count()


# =========================
# RECIPE SERIALIZER
# =========================
class RecipeSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Recipe

        # MUST MATCH YOUR ACTUAL MODEL FIELDS
        fields = [
            'id',
            'name',
            'image',
            'image_key',
            'category',
            'category_name',
            'rating',
            'time',
            'ingredients',
            'instructions',
        ]