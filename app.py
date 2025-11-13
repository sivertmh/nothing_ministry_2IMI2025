from flask import Flask, request, render_template, redirect
#importerer alle funksjoner fra min functions.py
from python.functions import *

app = Flask(__name__)

try:
    create_db()
except:
    print("Databasen eksisterer allerede.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/u")
def userpage():
    return render_template("user.html")

create_tables()