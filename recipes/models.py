from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Added image_key to match the Recipe model structure
    image_key = models.CharField(
        max_length=50, 
        default="default_category", 
        help_text="Key for local asset mapping (e.g., 'breakfast')"
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image_key = models.CharField(max_length=50)
    
    # ForeignKey links a Recipe to ONE Category
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='recipes'
    )
    
    rating = models.FloatField(default=0.0)
    time = models.CharField(max_length=10)
    ingredients = models.TextField(
        null=True, 
        blank=True, 
        help_text="Separate ingredients with commas or new lines"
    )
    
    def __str__(self):
        return self.name