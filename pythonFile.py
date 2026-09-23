# https://flask.palletsprojects.com/en/stable/quickstart/
# https://www.w3schools.com/python/python_mysql_getstarted.asp
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    process_url = url_for("process")
    return render_template("home.html")

@app.route('/home', methods=['POST'])
def home():
    return render_template("home.html")

@app.route('/createAccount', methods=['POST'])
def createAccount():
    return render_template("createAccount.html")


@app.route('/apiPage', methods=['POST'])
def apiPage():
    return render_template("apiPage.html")

@app.route('/route', methods=['POST'])
def process():
    return "Hello, %s!" % escape(request.form['usernameInput'])