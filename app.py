# https://flask.palletsprojects.com/en/stable/quickstart/
# https://www.w3schools.com/python/python_mysql_getstarted.asp
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import mysql.connector
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add a secret key for sessions

@app.route('/')
def index():
    return render_template("account.html")  # Changed to show account.html as first page

def getUsername(userId):
    print("Testing getUsername")
    name = "SELECT username FROM login WHERE userId = '%s'" % (escape(userId))
    print("Username2 Is: ", name)
    return name


@app.route('/home', methods=['GET', 'POST'])
def home():
    #Check if user is logged in 
    if 'userName' in session and 'userId' in session:
        
        return render_template("home.html", userId=session['userId'], userName=session['userName'])
    else:
        # User is not logged back to login page
        return render_template("account.html")

@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    return render_template("createAccount.html")

@app.route('/index2', methods=['GET', 'POST'])
def tempPage():
    return render_template("index2.html")

@app.route('/favorites/<currentUserId>', methods=['GET', 'POST'])
def favorites(currentUserId):
    # connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    query = "SELECT recipeName, recipeId FROM recipes JOIN favorites ON recipes.recipeId = favorites.favoriteId WHERE userId = '%s'" % (escape(currentUserId))
    mycursor = mydb.cursor( )
    mycursor.execute(query)
    result = mycursor.fetchall()
    print("FavoritesResult: ", result)
    return render_template("favorites.html", selectedFavorites =  result)

@app.route('/post-recipes.html', methods=['GET', 'POST'])
def post_recipes():
    if request.method == 'POST':
        # Check if user is logged in (any user can post recipes)
        if 'userName' not in session:
            return render_template("post-recipes.html", error="Please log in to post a recipe.")
        
        # Get form data
        title = request.form.get('title')
        category = request.form.get('category')
        prep_time = request.form.get('prepTime')
        cook_time = request.form.get('cookTime')
        servings = request.form.get('servings')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        notes = request.form.get('notes')
        
        # Validate required fields
        if not title or not category or not ingredients or not instructions:
            return render_template("post-recipes.html", error="Please fill in all required fields (Title, Category, Ingredients, Instructions).")
        
        # Format times with "minutes" suffix if provided
        prep_time_formatted = f"{prep_time} minutes" if prep_time else "Not specified"
        cook_time_formatted = f"{cook_time} minutes" if cook_time else "Not specified"
        
        # Connect to database
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="connorsinger",  # replace with your username for compsci
                database="fall2025_482cook"
            )
            
            mycursor = mydb.cursor()
            
            # Get the next available recipeId
            mycursor.execute("SELECT MAX(recipeId) FROM recipes")
            max_id_result = mycursor.fetchone()
            next_recipe_id = (max_id_result[0] + 1) if max_id_result[0] else 1
            
            # Insert new recipe
            insert_query = """
            INSERT INTO recipes (recipeId, recipeName, description, instructions, recipeIngredients, category, 
                               preptime, cook_time, servings, difficulty, author, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Prepare values (truncate long text to fit varchar(45) limits)
            recipe_values = (
                next_recipe_id,  # Add the recipeId
                title[:45] if title else "Untitled Recipe",
                (notes if notes else f"Delicious {title} recipe")[:45],
                instructions[:45] if instructions else "No instructions provided",
                ingredients[:45] if ingredients else "No ingredients listed",
                category,
                prep_time_formatted,
                cook_time_formatted,
                servings if servings else "1",
                "Medium",  # default difficulty
                session['userName'],  # author from session
                None  # user_id set to NULL to avoid foreign key constraint
            )
            
            mycursor.execute(insert_query, recipe_values)
            mydb.commit()
            
            print(f"Recipe '{title}' added successfully by {session['userName']} with ID {next_recipe_id}")
            
            mycursor.close()
            mydb.close()
            
            # Redirect to home with success message
            return redirect(url_for('home'))
            
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Error message: {err.msg}")
            return render_template("post-recipes.html", error=f"Database error: {err.msg}")
        except Exception as e:
            print(f"General error: {e}")
            return render_template("post-recipes.html", error="An unexpected error occurred. Please try again.")
        
    # GET request - just show the form
    # Allow any logged-in user to access the recipe posting form
    if 'userName' not in session:
        return render_template("post-recipes.html", error="Please log in to post a recipe.")
        
    return render_template("post-recipes.html")

@app.route('/allRecipes', methods=['GET', 'POST'])
def showAllRecipes():
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    query = "SELECT * FROM recipes"
    mycursor = mydb.cursor( )
    mycursor.execute(query)
    result = mycursor.fetchall()
    return render_template("allRecipes.html", allRecipes =  result)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        searchInput  = request.form['searchInput']
    else:
        searchInput = ''
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    searchInput = searchInput.lower()

    query = "SELECT recipeName, recipeId FROM recipes WHERE recipeName LIKE '%%%s%%' UNION SELECT recipeName, recipeId FROM recipes WHERE recipeIngredients LIKE '%%%s%%'" % (escape(searchInput), escape(searchInput)) 


    mycursor = mydb.cursor( )
    mycursor.execute(query)
    result = mycursor.fetchall()
    return render_template("search.html", allRecipes =  result, searchInput=searchInput)

@app.route('/recipes/<recipeId>', methods=['GET', 'POST'])
def recipes(recipeId):
    # connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    query = "SELECT * FROM recipes WHERE recipeId = '%s'" % (escape(recipeId))
    mycursor = mydb.cursor( )
    mycursor.execute(query)
    result = mycursor.fetchall()
    print("RecipesResult: ", result)
    query2 = "SELECT * FROM recipe_comments WHERE recipeId = '%s'" % (escape(recipeId))
    mycursor.execute(query2)
    result2 = mycursor.fetchall()
    print("CommentsResult: ", result2)
    return render_template("recipes.html", selectedRecipe =  result, recipeComments = result2)

@app.route('/recipes/<recipeId>', methods=['GET', 'POST'])
def insertComment(recipeId):
    # connect to the MySQL database
    print("Making a new comment")
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    commentText = request.form['commentText']
    #author = 1010 #placeholder
    commentId = 1010
    userId = session.get('userId', None)
    timeStamp = time.time()
    #This below was another database table that we have i'm not sure what it is or why we have two of them, this one we are using is the simpler one
    #query = "INSERT INTO recipe_comments (commentId, recipeId, userId, commentText, parentCommentId, isApproved, helpfulCount, hasImages, images, createdOn, updatedOn) VALUES (99, '%s', '%s', '%s', NULL, 1, 0, 0, NULL, NOW(), NOW())" % (escape(recipeId), escape(author), escape(commentText))
    query = "INSERT INTO comments(id, post_id, user_id, content, created_at) VALUES ('%s', '%s', '%s', '%s', '%s')" % (escape(commentId,), escape(recipeId), escape(userId), escape(commentText), escape(timeStamp)) 
    mycursor = mydb.cursor( )
    mycursor.execute(query)
    result = mycursor.fetchall()
    print("InsertCommentResult: ", result)
    print("Comment Created and put in database")
    return

@app.route('/apiPage', methods=['GET', 'POST'])
def apiPage():
    return render_template("apiPage.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #register
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        print("Registration attempt - Email:", email, "Username:", username)
        
        #Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="connorsinger",
            database="fall2025_482cook"  
        )
        mycursor = mydb.cursor()
        
        #Check if username already exists
        check_query = "SELECT userId FROM login WHERE username = '%s'" % (escape(username))
        mycursor.execute(check_query)
        existing_user = mycursor.fetchone()
        
        if existing_user:
            return "Username already exists. Please choose a different username."
        
        #Get the next available userId
        max_id_query = "SELECT MAX(userId) FROM login"
        mycursor.execute(max_id_query)
        max_id_result = mycursor.fetchone()
        next_user_id = 1
        if max_id_result and max_id_result[0] is not None:
            next_user_id = max_id_result[0] + 1
        
        #Add new user into database with userId
        insert_query = "INSERT INTO login (userId, username, password) VALUES (%s, %s, %s)"
        mycursor.execute(insert_query, (next_user_id, username, password))
        mydb.commit()
        
        #Redirect to account.html page for login after successful registration
        return redirect(url_for('index'))
    
    # If GET request, show register form
    return render_template("register.html")

def updateSQL():
    print("Update SQL Function Happened")
    return

@app.route('/process', methods=['GET', 'POST'])
def process():
    print("i am in process")
    username = request.form['usernameInput']
    password = request.form['passwordInput']

    print("/process User input is", username);
    out="User ID is: "
    # connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="connorsinger", #replace with your username for compsci
        database="fall2025_482cook"  
    )
    mycursor = mydb.cursor()
    #query = "SELECT username FROM login where username = '%s' limit 1" % (escape(username))

    query = "SELECT userId FROM login WHERE username = '%s' AND password = '%s' limit 1" % (escape(username), escape(password))
    
    #printing the username and password to the terminal for debugging purposes
    print("/process Password Is: ", password);
    print("/process Username Is: ", username);

    print("Query is", query)
    mycursor.execute(query)
    # Equivalent query: 
    # mycursor.execute("SELECT continent FROM country where name = %s limit 1", (username,)) 
    # Angola is a good input when you test
    myresult = mycursor.fetchall()

    if myresult:
        # Store user data in session
        session['userId'] = myresult[0][0]
        session['userName'] = username
        #return out + escape(myresult[0][0]) #if we are able to get something from the sql statement
        #we can also return more than one value (unlimited I think, not too sure) and use it in another html file
        return render_template("home.html", userId = myresult[0][0], userName = username)
    else:
        #if we get nothing from the sql statement
        #return, this is only used for when there is not a valid login
        return "Incorrect username or password: Given Username: " + escape(username) + " Password: " + escape(password)

#Logout button 
@app.route('/logout')
def logout():
    # Clear the session data
    session.pop('userId', None)
    session.pop('userName', None)
    return redirect(url_for('index'))

@app.route('/home2', methods=['GET', 'POST'])
def home2():
    userId = session.get('userId', None)
    userName = session.get('userName', None)
    print("UserID in home2 is: ", userId)
    print("UserName in home2 is: ", userName)
    return render_template("home.html", userId=userId, userName=userName)