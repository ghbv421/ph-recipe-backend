from django.db import models

class Recipe(models.Model):
    # Mapping system categories to Model choices 
    CATEGORY_CHOICES = [
        ('Rice', 'Rice'),
        ('Meat', 'Meat'),
        ('Vegetable', 'Vegetable'),
    ]

    name = models.CharField(max_length=100)
    image_key = models.CharField(max_length=50) # Matches your local ImageMapper keys
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    rating = models.FloatField(default=0.0)
    time = models.CharField(max_length=10) # e.g., "45m"

    
    def __str__(self):
        return self.name