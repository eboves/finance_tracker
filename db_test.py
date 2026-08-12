from dotenv import load_dotenv
import os
import psycopg2
from database import get_connection

db_test = get_connection()

cur = db_test.cursor()
cur.execute("INSERT INTO accounts (name, account_type, institution, date_opened) VALUES (%s, %s, %s, %s)", ("amex_savings", "savings", "american express", "2010-08-07"))

db_test.commit()

cur.close()
db_test.close()