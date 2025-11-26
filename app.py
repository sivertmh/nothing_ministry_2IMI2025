from flask import Flask, request, render_template, redirect
#importerer alle funksjoner fra min functions.py
from python.functions import *

app = Flask(__name__)

#lager db om den ikke finnes
try:
    create_db()
except:
    print("Databasen eksisterer allerede.")

#lager tabeller om den ikke finnes
try:
    create_tables()
except:
    print("Starttabeller er i orden.")
    
try:
    add_content_user()
except:
    print("Tabellen 'user' skal ha data i seg.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/u/<string:username>")
def show_user(username):
    mydb = get_connection()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT username FROM user WHERE username = %s", (username,))
    row = mycursor.fetchone()

    mydb.close()

    if row:
        username = row[0]
    else:
        username = "User not found"

    return render_template("user.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)