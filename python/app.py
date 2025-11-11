from flask import Flask, request, render_template, redirect
from functions import *

app = Flask(__name__)

try:
    create_db()
except:
    print("Databasen eksisterer allerede.")

try:
    create_table_users()
except:
    print("Tabell 'users' finnes allerede.")




    