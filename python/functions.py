import os, mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    #Returnerer en aktiv database-tilkobling basert på miljøvariabler.
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port="3306",
    )

mydb = get_connection()
mycursor = mydb.cursor()

def create_db():
    mycursor.execute("CREATE DATABASE nothing_ministry")
    
    mydb.commit()
    print(mycursor.rowcount, "endring(er)")

def show_customers():
    mycursor.execute("SELECT * FROM users")

    print(mycursor.rowcount, "endring(er)")

#lager tabellene som db består av
def create_tables():

    mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL)")
    mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
    mycursor.execute("CREATE TABLE item (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category_id INT, FOREIGN KEY (category_id) REFERENCES category(id))")
    mycursor.execute("CREATE TABLE receipt (id INT AUTO_INCREMENT PRIMARY KEY, date_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user_id INT, item_id INT, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (item_id) REFERENCES item(id))")

    mydb.commit()

def add_content_user():
    sql = "INSERT INTO user (name, surname, username, email) VALUES (%s, %s, %s, %s)"
    val = {
        ("Sivert", "K", "sivek", "sivek@email.com"),
        ("Ylla", "K", "yllak", "yllak@email.com"),
           }
    mycursor.executemany(sql, val)

    mydb.commit()
    
    print(mycursor.rowcount, "endring(er).")
