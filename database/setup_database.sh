#!/bin/bash

# =====================================
# COOK-UP RECIPE DATABASE SETUP SCRIPT
# =====================================

echo "🍳 Cook-Up Recipe Database Management"
echo "====================================="

# Check if MySQL is running
if ! pgrep -x "mysqld" > /dev/null; then
    echo "❌ MySQL is not running. Please start MySQL first."
    exit 1
fi

# Function to run SQL scripts
run_sql() {
    local script_file=$1
    echo "📝 Running SQL script: $script_file"
    
    if [ -f "$script_file" ]; then
        mysql -u connorsinger fall2025_482cook < "$script_file"
        if [ $? -eq 0 ]; then
            echo "✅ Script executed successfully"
        else
            echo "❌ Script failed to execute"
        fi
    else
        echo "❌ Script file not found: $script_file"
    fi
}

# Function to add sample recipes
add_sample_recipes() {
    echo "🥘 Adding sample recipes to database..."
    run_sql "scripts/add_sample_recipes.sql"
}

# Function to test Python recipe operations
test_python_operations() {
    echo "🐍 Testing Python recipe operations..."
    cd recipes
    python3 post_recipe.py --quick
    cd ..
}

# Function to show database stats
show_stats() {
    echo "📊 Database Statistics:"
    mysql -u connorsinger fall2025_482cook -e "
    SELECT 
        COUNT(*) as total_recipes,
        COUNT(DISTINCT category) as total_categories,
        COUNT(DISTINCT author) as total_authors
    FROM recipes;
    "
    
    echo "📋 Recipes by Category:"
    mysql -u connorsinger fall2025_482cook -e "
    SELECT 
        category,
        COUNT(*) as recipe_count
    FROM recipes 
    GROUP BY category 
    ORDER BY recipe_count DESC;
    "
}

# Main menu
case "$1" in
    "samples")
        add_sample_recipes
        ;;
    "test")
        test_python_operations
        ;;
    "stats")
        show_stats
        ;;
    "all")
        add_sample_recipes
        test_python_operations
        show_stats
        ;;
    *)
        echo "Usage: $0 {samples|test|stats|all}"
        echo ""
        echo "Commands:"
        echo "  samples  - Add sample recipes to database"
        echo "  test     - Test Python recipe operations"
        echo "  stats    - Show database statistics"
        echo "  all      - Run all operations"
        echo ""
        echo "Examples:"
        echo "  $0 samples    # Add sample recipes"
        echo "  $0 all        # Complete setup"
        ;;
esac