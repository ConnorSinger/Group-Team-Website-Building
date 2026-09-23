# Cook-Up Recipe Database System

This folder contains organized database operations for the Cook-Up recipe application.

## 📁 Folder Structure

```
database/
├── connection.py              # Database connection management
├── setup_database.sh         # Bash script for database setup
├── recipes/
│   ├── recipe_operations.py  # Recipe CRUD operations
│   └── post_recipe.py        # Interactive recipe posting script
└── scripts/
    └── add_sample_recipes.sql # SQL script with sample recipes
```

## 🚀 Quick Start

### 1. Add Sample Recipes to Database
```bash
cd database
bash setup_database.sh samples
```

### 2. Test Python Recipe Operations
```bash
cd database
bash setup_database.sh test
```

### 3. View Database Statistics
```bash
cd database
bash setup_database.sh stats
```

### 4. Run Everything
```bash
cd database
bash setup_database.sh all
```

## 🐍 Python Usage

### Add Recipe Interactively
```bash
cd database/recipes
python3 post_recipe.py
```

### Add Demo Recipes
```bash
cd database/recipes
python3 post_recipe.py --quick
```

### Use in Your Code
```python
from database.recipes.recipe_operations import RecipeDatabase

# Create recipe database instance
recipe_db = RecipeDatabase()

# Add a recipe
recipe_data = {
    'title': 'My Recipe',
    'description': 'A delicious recipe',
    'instructions': 'Step 1, Step 2, Step 3',
    'ingredients': 'ingredient1, ingredient2',
    'category': 'dinner',
    'prep_time': '15 minutes',
    'cook_time': '30 minutes',
    'servings': '4',
    'difficulty': 'Medium',
    'author': 'Chef Name'
}

success, recipe_id, error = recipe_db.add_recipe(recipe_data)
if success:
    print(f"Recipe added with ID: {recipe_id}")
else:
    print(f"Error: {error}")
```

## 📊 Database Schema

The recipes table has these fields:
- `recipeId` (int) - Primary key
- `recipeName` (varchar 45) - Recipe title
- `description` (varchar 45) - Recipe description
- `instructions` (varchar 45) - Cooking instructions
- `recipeIngredients` (varchar 45) - Recipe ingredients
- `category` (varchar 45) - Recipe category
- `preptime` (varchar 45) - Preparation time
- `cook_time` (varchar 45) - Cooking time
- `servings` (varchar 45) - Number of servings
- `difficulty` (varchar 45) - Recipe difficulty
- `author` (varchar 45) - Recipe author
- `user_id` (int) - Foreign key to users table (nullable)
- `created_at` (timestamp) - Creation timestamp

## 🛠️ Features

### RecipeDatabase Class Methods:
- `add_recipe(recipe_data)` - Add a new recipe
- `get_recipe_by_id(recipe_id)` - Get recipe by ID
- `get_all_recipes()` - Get all recipes
- `search_recipes(search_term)` - Search recipes by name/category

### Benefits:
- ✅ Organized code structure
- ✅ Error handling for database operations
- ✅ Easy to use Python classes
- ✅ Interactive command-line tools
- ✅ SQL scripts for bulk operations
- ✅ Proper database connection management

## 🔧 Integration with Flask App

Your Flask app can now use these organized database operations:

```python
from database.recipes.recipe_operations import RecipeDatabase

@app.route('/post-recipes.html', methods=['POST'])
def post_recipes():
    # ... get form data ...
    
    recipe_db = RecipeDatabase()
    success, recipe_id, error = recipe_db.add_recipe(recipe_data)
    
    if success:
        return redirect(url_for('home'))
    else:
        return render_template("post-recipes.html", error=error)
```