from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
print("env loaded")

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_password = os.getenv("DB_PASSWORD")
print(f"db_name: {db_name}, db_user: {db_user}")

# THIS CREATES A CONNECTION TO AN EXISTING DATABASE USING THE PARAMS BELLOW
conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

# THIS CREATES A CURSOR (A WAY TO INTERACT WITH THE DB) DO ACTIONS LIKE CUR.EXECURTE("INSERT INTO my_database .....")
cur = conn.cursor()

 
# cur.execute('SELECT version();')

# THIS CLOSE THE CONNECTION TO THE DATABASE. THAT THE ORDER, FIRST WE CLOSE THE CURSOR AND FINALLY THE CONNECTION.
cur.close()
conn.close()


