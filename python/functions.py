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

def create_tables():
    try:
        mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL)")
        mycursor.execute("CREATE TABLE item (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category_id INT, FOREIGN KEY (category_id) REFERENCES category(id))")
        mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category_id INT, FOREIGN KEY (category_id) REFERENCES category(id))")
        mycursor.execute("CREATE TABLE order (id INT AUTO_INCREMENT PRIMARY KEY, date_ordered CURRENT_TIMESTAMP, FOREIGN KEY user_id REFERENCES user(id), FOREIGN KEY product_id REFERENCES product(id)")

        mydb.commit()
    except:
        print("Noen eller alle tabeller finnes allerede.")

    print("Oppdatert tabelliste:\n")
    mycursor.execute("SHOW TABLES")
    
    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
def reset_tables():
    sql = "DROP TABLE IF EXISTS user"
    mycursor.execute(sql)
    
    mydb.commit()
    
    print(mycursor.rowcount, "endring(er).")

def add_content_users():
    sql = "INSERT INTO user (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()
    
    print(mycursor.rowcount, "endring(er).")

def show_tables():
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    
#kjøring av funksjoner

