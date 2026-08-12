from database import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("INSERT INTO accounts (name, account_type, institution, date_opened) VALUES (%s, %s, %s, %s)", ("retirement roth ira", "roth_ira", "fidelity", "2012-03-08"))

conn.commit()

cur.close()
conn.close()