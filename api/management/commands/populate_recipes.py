from django.core.management.base import BaseCommand
from api.models import Recipe

class Command(BaseCommand):
    help = 'Populate the database with initial recipe data'

    def handle(self, *args, **kwargs):
        recipes = [
            {
                "name": "Spaghetti Carbonara",
                "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
                "ingredients": "Spaghetti, Eggs, Parmesan Cheese, Pancetta, Black Pepper, Salt",
                "instructions": "1. Cook the spaghetti. 2. Fry the pancetta until crisp. 3. Beat the eggs and mix with cheese. 4. Combine spaghetti with pancetta and egg mixture. 5. Season with salt and pepper.",
                "image": "https://imgur.com/bPojqr4.jpg"
            },
            {
                "name": "Chicken Tikka Masala",
                "description": "A flavorful Indian curry dish made with marinated chicken and a spiced tomato sauce.",
                "ingredients": "Chicken, Yogurt, Garlic, Ginger, Tomatoes, Garam Masala, Cream, Onion",
                "instructions": "1. Marinate the chicken in yogurt and spices. 2. Grill the chicken. 3. Cook the onion, garlic, and ginger. 4. Add tomatoes and spices. 5. Stir in cream and add the chicken. 6. Serve with rice or naan.",
                "image": "https://imgur.com/mewc0Bj.jpg"
            },
            # Add more recipes as needed
        ]

        for recipe_data in recipes:
            Recipe.objects.create(**recipe_data)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with recipes.'))
