
### 1. Start the Application
```bash
export FLASK_ENV=development
export FLASK_APP=app.py
flask run -p 8080
```

**🌐 Your app is now running at: http://localhost:8080**

---

## 🔐 How to Login

### Option 1: Use Demo Account (Recommended)
- **Username:** `admin`
- **Password:** `1234`
   Username: bill
   password: welcome123

### Option 2: Create New Account
1. Go to http://localhost:8080
2. Click "Get Started" or "Register" 
3. Fill out the registration form:
   - Choose a username (letters/numbers only)
   - Create a password (minimum 8 characters, must include letters AND numbers)
   - Provide an email address
4. Click "Create Account"
5. You'll be redirected to login - use your new credentials

---

## 📖 Complete User Guide

### After Logging In - What You Can Do:

#### 🏠 **Home Dashboard**
- View welcome message with your username
- Navigate to different sections using the top navigation menu
- Access logout

#### 📝 **Post New Recipes** 
1. Click "POST RECIPES" in the navigation menu
2. Fill out the recipe form:
   - **Recipe Name:** Give your dish a catchy title
   - **Description:** Describe what makes your recipe special
   - **Ingredients:** List each ingredient on a new line
   - **Instructions:** Step-by-step cooking directions
   - **Prep Time:** How long to prepare (in minutes)
   - **Cook Time:** How long to cook (in minutes)
   - **Servings:** How many people it feeds
   - **Difficulty:** Choose Easy, Medium, or Hard
3. Click "Share Recipe"
4. Your recipe is now live and visible to all users!

#### 🍽️ **Browse All Recipes**
1. Click "RECIPES" in the navigation menu
2. Browse through all community recipes
3. Click on any recipe title to view full details
4. See recipe information, cooking times, difficulty levels

#### 👤 **Your Favorites Page**

   - **Favorites:** Recipes you've liked from other users


---

## 🎯 Step-by-Step Walkthrough

### First Time User Journey:
1. **Start:** Go to http://localhost:8080
2. **Register:** Click "Get Started" → Fill registration form → Submit
3. **Login:** Enter your new username/password → Click "Login"
4. **Explore:** Browse existing recipes in "RECIPES" section
5. **Favorite:** working on favorites (predetermined: bill account has two favorites, no way now to favorite)
6. **Share:** Click "POST RECIPES" → Create your first recipe

### Regular User Flow:
1. **Login:** Use saved credentials
2. **Browse:** Check "RECIPES" for new community posts
3. **Interact:** view details
4. **Contribute:** Post new recipes when you cook something amazing
5. **Manage:** Use profile to organize your recipes and favorites

---


```

### Database Schema
The app automatically creates these tables:
- `users` - User accounts and authentication
- `recipes` - Recipe content and metadata  
- `recipe_likes` - Favorite recipes tracking
- `recipe_comments` - Recipe comments (future feature)

### Port Configuration
- Default: http://localhost:8080
- To change port: `flask run -p 5000` (or any port number)

---

## 🆘 Troubleshooting

### Common Issues:

**"Address already in use" error:**
```bash
# Kill existing Flask process
pkill -f flask
# Then restart: flask run -p 8080
```

**Database connection errors:**
- Make sure MySQL is running: `sudo service mysql start`
- Check database name matches: `fall2025_482cook`
- Verify MySQL user has proper permissions

**Login not working:**
- Use demo account: `demo` / `demo1234`
- Password must be 8+ characters with letters AND numbers
- Try creating a new account if issues persist

**Page not loading:**
- Check Flask is running: look for "Running on http://127.0.0.1:8080"
- Try refreshing browser or clearing cache
- Check terminal for error messages

---

## ✨ Features Overview

### ✅ Currently Available:
- ✅ User registration and secure login
- ✅ Recipe posting with rich details
- ✅ Browse all community recipes  
- ✅ Favorite/unfavorite recipes
- ✅ Personal profile with recipe management
- ✅ Responsive web design
- ✅ Session management
- ✅ Password encryption and security

### 🚧 Coming Soon:
- Recipe comments and ratings
- Recipe search and filtering
- User-to-user messaging
- Recipe categories and tags
- Image uploads for recipes
- Advanced user profiles

---

## 🤝 Contributing

This is a course project for Fall 2025. The application is actively being developed and improved.

**Repository:** https://github.com/krispepper/482_cookup_phase_1  
**Current Version:** Phase 1 - Full Feature Release  
**Last Updated:** October 2025

---

*Happy Cooking! 👨‍🍳👩‍🍳*
