import os, mysql.connector; from dotenv import load_dotenv

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

    result = mycursor.fetchall()
    print(mycursor.rowcount, "endring(er)")

def create_table_users():
    mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")

    mydb.commit()
    tables = mycursor.execute("SHOW TABLES")
    
    print("Tabell ble lagt til.\nOppdatert tabelliste:", tables)

def add_content_users():
    sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()
    
    print(mycursor.rowcount, "endring(er).")
    
#kjøring av funksjoner