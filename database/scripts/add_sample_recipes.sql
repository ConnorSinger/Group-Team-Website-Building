-- =========================================
-- RECIPE DATABASE SETUP AND SAMPLE DATA
-- =========================================

-- Check current database structure
DESCRIBE recipes;

-- Show current recipes count
SELECT COUNT(*) as total_recipes FROM recipes;

-- =========================================
-- SAMPLE RECIPES TO ADD TO DATABASE
-- =========================================

-- Get next available ID
SELECT MAX(recipeId) + 1 as next_available_id FROM recipes;

-- Classic Chocolate Chip Cookies
INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, preptime, cook_time, servings, difficulty, author, user_id)
VALUES (4001, 'Classic Chocolate Chip Cookies', 'Best homemade cookies ever', 
'1. Preheat oven to 375F. 2. Mix dry ingredients. 3. Cream butter and sugars. 4. Add eggs and vanilla. 5. Combine wet and dry. 6. Fold in chocolate chips. 7. Bake 9-11 minutes.',
'2¼ cups flour, 1 tsp baking soda, 1 tsp salt, 1 cup butter, ¾ cup granulated sugar, ¾ cup brown sugar, 2 eggs, 2 tsp vanilla, 2 cups chocolate chips',
'desserts', '20 minutes', '11 minutes', '48', 'Easy', 'Chef Baker', NULL);

-- Beef Stir Fry
INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, preptime, cook_time, servings, difficulty, author, user_id)
VALUES (4002, 'Quick Beef Stir Fry', 'Fast and delicious dinner', 
'1. Cut beef into strips. 2. Heat oil in wok. 3. Stir fry beef 3-4 minutes. 4. Add vegetables. 5. Stir fry 2-3 minutes. 6. Add sauce. 7. Serve over rice.',
'1 lb beef sirloin, 2 tbsp oil, 1 bell pepper, 1 onion, 2 cloves garlic, ¼ cup soy sauce, 2 tbsp oyster sauce, 1 tsp cornstarch',
'dinner', '15 minutes', '8 minutes', '4', 'Medium', 'Chef Wang', NULL);

-- Fluffy Pancakes
INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, preptime, cook_time, servings, difficulty, author, user_id)
VALUES (4003, 'Fluffy Breakfast Pancakes', 'Perfect weekend breakfast', 
'1. Mix dry ingredients. 2. Whisk wet ingredients separately. 3. Combine wet and dry gently. 4. Heat griddle. 5. Pour batter. 6. Flip when bubbles form. 7. Serve hot with syrup.',
'2 cups flour, 2 tbsp sugar, 2 tsp baking powder, 1 tsp salt, 2 eggs, 1¾ cups milk, ¼ cup melted butter',
'breakfast', '10 minutes', '15 minutes', '8', 'Easy', 'Chef Morning', NULL);

-- Caesar Salad
INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, preptime, cook_time, servings, difficulty, author, user_id)
VALUES (4004, 'Classic Caesar Salad', 'Fresh and crispy salad', 
'1. Wash and chop romaine. 2. Make dressing with anchovy, garlic, lemon. 3. Toss lettuce with dressing. 4. Add parmesan and croutons. 5. Serve immediately.',
'2 heads romaine lettuce, ½ cup parmesan cheese, ¾ cup croutons, 3 cloves garlic, 2 anchovy fillets, ¼ cup lemon juice, ½ cup olive oil',
'appetizers', '15 minutes', '0 minutes', '6', 'Medium', 'Chef Caesar', NULL);

-- Chicken Soup
INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, preptime, cook_time, servings, difficulty, author, user_id)
VALUES (4005, 'Homemade Chicken Soup', 'Comfort food at its best', 
'1. Boil chicken with herbs. 2. Remove chicken and shred. 3. Strain broth. 4. Sauté vegetables. 5. Add broth and chicken back. 6. Simmer 20 minutes. 7. Season and serve.',
'1 whole chicken, 2 carrots, 2 celery stalks, 1 onion, 3 cloves garlic, 8 cups water, salt, pepper, thyme, bay leaves',
'lunch', '20 minutes', '45 minutes', '6', 'Medium', 'Chef Comfort', NULL);

-- =========================================
-- VERIFY ALL RECIPES WERE ADDED
-- =========================================

-- Show all newly added recipes
SELECT recipeId, recipeName, category, author, preptime, cook_time, servings
FROM recipes 
WHERE recipeId BETWEEN 4001 AND 4005
ORDER BY recipeId;

-- Show total count after additions
SELECT COUNT(*) as total_recipes_after_insert FROM recipes;