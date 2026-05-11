# recipes/serializers.py
from rest_framework import serializers
from .models import Recipe, Category

class CategorySerializer(serializers.ModelSerializer):
    # This dynamically counts how many recipes belong to this category
    recipe_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_key', 'recipe_count']

    def get_recipe_count(self, obj):
        # 'recipes' comes from the related_name in your Recipe model ForeignKey
        return obj.recipes.count()

class RecipeSerializer(serializers.ModelSerializer):
    # This adds the actual name of the category to the JSON response
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
<<<<<<< Updated upstream
        model = Recipe
        # We list them out to ensure category_name is included
        fields = [
            'id', 'name', 'image_key', 'category', 
            'category_name', 'rating', 'time', 'ingredients'
        ]
=======
        model  = Recipe
        fields = '__all__'   # now includes: id, name, description, image, image_key, category, rating, time
>>>>>>> Stashed changes
