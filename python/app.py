from flask import Flask, request, render_template, redirect
#importerer alle funksjoner fra functions.py
from functions import *

app = Flask(__name__)

try:
    create_db()
except:
    print("Databasen eksisterer allerede.")

create_tables()

@app.route('/')
def index():
    return render_template("index.html")
    