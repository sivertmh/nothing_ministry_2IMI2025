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

# legger til startinnhold i user-tabell
try:
    insert_default_data()
except:
    print("Standard data enten finnes fra før eller mangler.")

# startside
@app.route("/")
def index():
    return render_template("index.html")

# varierende brukerside
@app.route("/u/<string:username>")
def show_user(username):
    mydb = get_connection()
    mycursor = mydb.cursor()

    # Henter brukernavn og id basert på brukernavn i url
    mycursor.execute("SELECT id, name FROM user WHERE username = %s", (username,))
    # row = (1, "sivert")
    row = mycursor.fetchone()

    # om henting av brukernavn og id funket kjøres denne (hvis row-variabelen er uten error)
    if row:
        user_id, name = row
        mycursor.execute("SELECT item_id FROM owned WHERE user_id = %s", (user_id,))
        # item_id = (1,)
        item_id = mycursor.fetchone()
        
        # henter og lagrer produktnavn i en variabel item_name
        mycursor.execute("SELECT name FROM item WHERE id=%s", (item_id))
        # item_name = ("Don Quixote",)
        item_name = mycursor.fetchone()
        
        # lagrer en brukers items i variabel
        mycursor.execute("SELECT * FROM owned WHERE user_id = %s", (user_id,))
        items = mycursor.fetchall()
    # kjøres hvis henting av brukernavn og id ga error (hvis row-variabelen får error)
    else:
        name = "User not found"
        items = []

    mydb.close()

    return render_template("user.html", name=name, items=items)

    
# registering av bruker
@app.route('/u/register', methods=['POST', 'GET'])
def register_user():
    # Hvis POST gjøres (submit), så legges bruker og går tilbake til startside.
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
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)