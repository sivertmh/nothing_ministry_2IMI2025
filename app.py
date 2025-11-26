from flask import Flask, request, render_template, redirect, session
from flask_session import Session
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

# legger til startinnhold i user-tabell
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

@app.route('/u/register', methods=['POST', 'GET'])
def add_customer():
    #hvis noen POST-er, altså trykker submit på form, så kjører koden
    if request.method == 'POST':
        mydb = get_connection()
        mycursor = mydb.cursor()
        
        name = request.form['name']
        surname = request.form['surname']
        username = request.form['username']
        email = request.form['email']
        
        sql = "INSERT INTO user (name, surname, username, email) VALUES (%s, %s, %s, %s)"
        val = (name, surname, username, email)
        
        mycursor.execute(sql, val)
        
        mydb.commit()
        
        return redirect('/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)