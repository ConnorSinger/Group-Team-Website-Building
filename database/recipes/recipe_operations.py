#!/usr/bin/env python3
"""
Recipe Database Operations Module
Handles all recipe-related database operations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connection import DatabaseConnection
import mysql.connector

class RecipeDatabase:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_next_recipe_id(self):
        """Get the next available recipe ID"""
        if not self.db.connect():
            return None
        
        try:
            self.db.execute_query("SELECT MAX(recipeId) FROM recipes")
            result = self.db.fetch_one()
            next_id = (result[0] + 1) if result[0] else 1
            return next_id
        except Exception as e:
            print(f"Error getting next recipe ID: {e}")
            return None
        finally:
            self.db.close()
    
    def add_recipe(self, recipe_data):
        """
        Add a new recipe to the database
        
        Args:
            recipe_data (dict): Dictionary containing recipe information
        
        Returns:
            tuple: (success: bool, recipe_id: int or None, error_message: str or None)
        """
        if not self.db.connect():
            return False, None, "Failed to connect to database"
        
        try:
            # Get next recipe ID
            self.db.execute_query("SELECT MAX(recipeId) FROM recipes")
            result = self.db.fetch_one()
            next_id = (result[0] + 1) if result[0] else 1
            
            # Prepare the insert query
            insert_query = """
            INSERT INTO recipes (recipeId, recipeName, description, instructions, 
                               recipeIngredients, category, preptime, cook_time, 
                               servings, difficulty, author, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Prepare values (truncate to fit varchar(45) limits)
            recipe_values = (
                next_id,
                recipe_data.get('title', 'Untitled Recipe')[:45],
                recipe_data.get('description', 'No description')[:45],
                recipe_data.get('instructions', 'No instructions')[:45],
                recipe_data.get('ingredients', 'No ingredients')[:45],
                recipe_data.get('category', 'other'),
                recipe_data.get('prep_time', 'Not specified'),
                recipe_data.get('cook_time', 'Not specified'),
                recipe_data.get('servings', '1'),
                recipe_data.get('difficulty', 'Medium'),
                recipe_data.get('author', 'Anonymous'),
                None  # user_id set to NULL
            )
            
            # Execute the insert
            if self.db.execute_query(insert_query, recipe_values):
                self.db.commit()
                self.db.close()
                return True, next_id, None
            else:
                self.db.close()
                return False, None, "Failed to execute insert query"
                
        except mysql.connector.Error as e:
            self.db.close()
            return False, None, f"Database error: {e.msg}"
        except Exception as e:
            self.db.close()
            return False, None, f"Unexpected error: {str(e)}"
    
    def get_recipe_by_id(self, recipe_id):
        """Get a recipe by its ID"""
        if not self.db.connect():
            return None
        
        try:
            query = "SELECT * FROM recipes WHERE recipeId = %s"
            if self.db.execute_query(query, (recipe_id,)):
                result = self.db.fetch_one()
                return result
            return None
        except Exception as e:
            print(f"Error getting recipe: {e}")
            return None
        finally:
            self.db.close()
    
    def get_all_recipes(self):
        """Get all recipes from the database"""
        if not self.db.connect():
            return []
        
        try:
            query = "SELECT * FROM recipes ORDER BY created_at DESC"
            if self.db.execute_query(query):
                results = self.db.fetch_all()
                return results
            return []
        except Exception as e:
            print(f"Error getting all recipes: {e}")
            return []
        finally:
            self.db.close()
    
    def search_recipes(self, search_term):
        """Search recipes by name"""
        if not self.db.connect():
            return []
        
        try:
            query = "SELECT * FROM recipes WHERE recipeName LIKE %s OR category LIKE %s"
            search_pattern = f"%{search_term}%"
            if self.db.execute_query(query, (search_pattern, search_pattern)):
                results = self.db.fetch_all()
                return results
            return []
        except Exception as e:
            print(f"Error searching recipes: {e}")
            return []
        finally:
            self.db.close()

# Usage example:
if __name__ == "__main__":
    recipe_db = RecipeDatabase()
    
    # Example recipe data
    sample_recipe = {
        'title': 'Test Python Recipe',
        'description': 'A recipe created from Python script',
        'instructions': 'Mix and cook ingredients',
        'ingredients': 'flour, water, salt',
        'category': 'test',
        'prep_time': '10 minutes',
        'cook_time': '15 minutes',
        'servings': '4',
        'difficulty': 'Easy',
        'author': 'Python Script'
    }
    
    # Add the recipe
    success, recipe_id, error = recipe_db.add_recipe(sample_recipe)
    if success:
        print(f"Recipe added successfully with ID: {recipe_id}")
    else:
        print(f"Failed to add recipe: {error}")