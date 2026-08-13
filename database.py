import os
from dotenv import load_dotenv
import psycopg2 


# THIS FUNCTION STABLISH THE CONNECTION WITH THE DATABASE
def get_connection():
    
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_password = os.getenv("DB_PASSWORD")

    # THIS CREATES A CONNECTION TO AN EXISTING DATABASE USING THE PARAMS BELLOW
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

    return conn

def get_accounts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts;")
    accounts = cur.fetchall()
    cur.close()
    conn.close()

    return accounts
