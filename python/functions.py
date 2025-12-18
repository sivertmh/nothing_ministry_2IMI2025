import os, mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    # kobler til db med miljøvariabler fra .env
    return mysql.connector.connect(
        # prøver først med skole-nettverksoppsett
        host=os.environ.get("DB_HOST", "localhost") or os.environ.get("DB_HOST_HOME"),
        user=os.environ.get("DB_USER") or os.environ.get("DB_USER_HOME"),
        password=os.environ.get("DB_PASSWORD") or os.environ.get("DB_PASSWORD_HOME"),
        database=os.environ.get("DB_NAME"),
        port="3306"
    )

# Brukes til å koble til db. Absolutt nødvendig.
mydb = get_connection()
mycursor = mydb.cursor()

def create_db():
    mycursor.execute("CREATE DATABASE nothing_ministry")
    
    mydb.commit()
    print(mycursor.rowcount, "endring(er)")

def show_customers():
    mycursor.execute("SELECT * FROM users")

    print(mycursor.rowcount, "endring(er)")

# Lager standard tabeller til database. For at category-tabellen skal "funke" må den få insert-data med de forskjellige sjangerne.
def create_tables():
    mycursor.execute("CREATE TABLE `user` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL)")
    mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
    mycursor.execute("CREATE TABLE creator (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category_id INT, FOREIGN KEY (category_id) REFERENCES category(id))")
    mycursor.execute("CREATE TABLE item (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, creator_id INT, category_id INT, FOREIGN KEY (category_id) REFERENCES category(id), FOREIGN KEY (creator_id) REFERENCES creator(id))")
    mycursor.execute("CREATE TABLE owned (id INT AUTO_INCREMENT PRIMARY KEY, date_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user_id INT, item_id INT, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (item_id) REFERENCES item(id))")

    mydb.commit()
    print("Standardtabeller ble laget.")

# NYERE ENN add_content_user. Setter inn standard data. Category-data trengs for at appen skal funke ordentlig.
def insert_default_data():
    # standardbrukere
    sql_user = "INSERT INTO user (name, surname, username, email) VALUES (%s, %s, %s, %s)"
    val_user = [
        ("Sivert", "Peregrine", "sivert", "sivertp@email.com"),
        ("Ylla", "K", "ylla", "yllak@email.com"),
        ("Yll", "K", "yll", "yllk@email.com"),
    ]
    mycursor.executemany(sql_user, val_user)

    # standardkategorier
    sql_category = "INSERT INTO category (name) VALUES (%s)"
    val_category = [
        ("book",),
        ("music",),
        ("film",),
        ("series",),
        ("videogame",)
    ]
    mycursor.executemany(sql_category, val_category)
    
    # standard creators
    sql_creator = "INSERT INTO creator (name, category_id) VALUES (%s, %s)"
    val_creator = [
        ("Miguel de Ceraventes", 1),
        ("Ray Bradbury", 1),
        ("The Beatles", 2),
        ("Kaizers Orchestra", 2),
    ]
    mycursor.executemany(sql_creator, val_creator)
    
    # standard items
    sql_item = "INSERT INTO item (name, creator_id, category_id) VALUES (%s, %s, %s)"
    val_item = [
        # bøker (cat 1)
        ("Don Quixote", 1, 1),
        ("Fahrenheit 451", 2, 1),
        ("The Martian Chronicles", 2, 1),
        # musikk-album (cat 2)
        ("Rubber Soul", 3, 2),
        ("Abbey Road", 3, 2),
        ("Violeta Violeta Volum 1", 4, 2,),
    ]
    mycursor.executemany(sql_item, val_item)

    mydb.commit()

    print(mycursor.rowcount, "endring(er). Standard data i tabeller skal være i orden.")
    