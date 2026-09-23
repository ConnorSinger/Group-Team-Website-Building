#!/usr/bin/env python3
"""
Recipe Posting Script
Use this script to easily add recipes to the database from command line
"""

import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recipe_operations import RecipeDatabase

def post_recipe_interactive():
    """Interactive script to post a recipe"""
    print("=== COOK-UP RECIPE POSTING SYSTEM ===")
    print("Enter recipe details below:")
    
    # Get recipe information from user
    title = input("Recipe Title: ").strip()
    if not title:
        print("Error: Recipe title is required!")
        return
    
    description = input("Description (optional): ").strip()
    category = input("Category (appetizers/main-course/desserts/beverages/breakfast/lunch/dinner/snacks): ").strip()
    
    print("\nIngredients (press Enter twice when done):")
    ingredients = []
    while True:
        ingredient = input("- ").strip()
        if not ingredient:
            break
        ingredients.append(ingredient)
    
    print("\nInstructions (press Enter twice when done):")
    instructions = []
    step = 1
    while True:
        instruction = input(f"{step}. ").strip()
        if not instruction:
            break
        instructions.append(f"{step}. {instruction}")
        step += 1
    
    prep_time = input("Prep time (e.g., '15 minutes'): ").strip()
    cook_time = input("Cook time (e.g., '30 minutes'): ").strip()
    servings = input("Number of servings: ").strip()
    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
    author = input("Author name: ").strip()
    
    # Prepare recipe data
    recipe_data = {
        'title': title,
        'description': description or f"Delicious {title}",
        'instructions': ' '.join(instructions),
        'ingredients': ', '.join(ingredients),
        'category': category or 'other',
        'prep_time': prep_time or 'Not specified',
        'cook_time': cook_time or 'Not specified',
        'servings': servings or '1',
        'difficulty': difficulty or 'Medium',
        'author': author or 'Anonymous'
    }
    
    # Add recipe to database
    print("\nAdding recipe to database...")
    recipe_db = RecipeDatabase()
    success, recipe_id, error = recipe_db.add_recipe(recipe_data)
    
    if success:
        print(f"✅ Recipe '{title}' added successfully with ID: {recipe_id}")
        print(f"🍽️  Category: {recipe_data['category']}")
        print(f"👨‍🍳 Author: {recipe_data['author']}")
        print(f"⏱️  Prep: {recipe_data['prep_time']}, Cook: {recipe_data['cook_time']}")
        print(f"🍽️  Servings: {recipe_data['servings']}")
    else:
        print(f"❌ Failed to add recipe: {error}")

def post_quick_recipe(title, category, ingredients, instructions, author="Script User"):
    """Quick function to post a recipe programmatically"""
    recipe_data = {
        'title': title,
        'description': f"Delicious {title}",
        'instructions': instructions,
        'ingredients': ingredients,
        'category': category,
        'prep_time': '15 minutes',
        'cook_time': '30 minutes',
        'servings': '4',
        'difficulty': 'Medium',
        'author': author
    }
    
    recipe_db = RecipeDatabase()
    success, recipe_id, error = recipe_db.add_recipe(recipe_data)
    
    if success:
        print(f"✅ Quick recipe '{title}' added with ID: {recipe_id}")
        return recipe_id
    else:
        print(f"❌ Failed to add recipe: {error}")
        return None

def main():
    """Main function"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--quick":
            # Quick demo recipes
            print("Adding demo recipes...")
            
            post_quick_recipe(
                "Python Pasta",
                "dinner", 
                "pasta, tomatoes, garlic, olive oil",
                "1. Boil pasta. 2. Sauté garlic. 3. Add tomatoes. 4. Mix with pasta.",
                "Python Chef"
            )
            
            post_quick_recipe(
                "Code Coffee",
                "beverages",
                "coffee beans, hot water, sugar",
                "1. Grind beans. 2. Brew with hot water. 3. Add sugar to taste.",
                "Programmer"
            )
            
        elif sys.argv[1] == "--help":
            print("Usage:")
            print("  python post_recipe.py           - Interactive mode")
            print("  python post_recipe.py --quick   - Add demo recipes")
            print("  python post_recipe.py --help    - Show this help")
    else:
        # Interactive mode
        post_recipe_interactive()

if __name__ == "__main__":
    main()