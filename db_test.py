from database import get_connection

conn = get_connection()

cur = conn.cursor()
cur.execute("SELECT version();")
version = cur.fetchone()[0]

print(version)

cur.close()
conn.close()