import os
from dotenv import load_dotenv
import psycopg2 
from psycopg2.extras import RealDictCursor


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
    conn = None
    cur = None
    accounts = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM accounts;")
        accounts = cur.fetchall()
        
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to run the script")
    finally:
        if conn:
            conn.close()
        if cur:
            cur.close()

    return accounts

def add_account(name, account_type, institution, date_opened):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts (name, account_type, institution, date_opened) VALUES(%s, %s, %s, %s)", (name, account_type, institution, date_opened))
        conn.commit()
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to run the script")
     
    finally:
        if conn:
            conn.close()
        if cur:
            cur.close()

def get_balance():
    conn = None
    cur = None
    balance = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT SUM(amount) FROM balances;")
        balance = cur.fetchall()
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to run the script")

    finally:
        if conn:
            conn.close()
        if cur: 
            cur.close()

    return balance

def add_balance(amount, date, name):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        print(name) 
        cur.execute("SELECT id FROM accounts WHERE name = %s;", (name,))
        conn.commit()
        account_id = cur.fetchone()[0]
        print(account_id)
        cur.execute("INSERT INTO balances (amount, account_id, date) VALUES (%s, %s, %s)", (amount, account_id, date))
        conn.commit()
    
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to run the script")
    
    finally:
        if conn:
            conn.close()
        if cur: 
            cur.close()


def get_balances():
    conn = None
    cur = None
    balances = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM balances;")
        balances = cur.fetchall()
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to run the script")
    finally:
        if conn:
            conn.close()
        if cur:
            cur.close()
 
    return balances



def get_account_by_id(account_id):

    conn = None
    cur = None
    account = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))
        account = cur.fetchone()

    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to the account by its id")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return account


def update_account_by_id(name, account_type, institution, date_opened, id):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE accounts SET name = %s, account_type = %s, institution = %s, date_opened = %s WHERE id = %s", (name, account_type, institution, date_opened, id))
        conn.commit()
    except psycopg2.Error as e:
        print(f"The Error: {e} was cought while trying to update the account")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def delete_account_by_id(account_id):
    conn = None
    cur = None
    items_deleted = 0

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM accounts WHERE id = %s", (account_id,)) 
        conn.commit()
        items_deleted = cur.rowcount
    except psycopg2.Error as e:
        print(f"message: The program crashed because of this error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return items_deleted


def get_balance_by_id(balance_id):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM balances WHERE id = %s", (balance_id,))
        balance_by_id = cur.fetchone()

    except psycopg2.Error as e:
        print(f"Message: site broke because of this error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return balance_by_id

def update_balance_by_id(id, date, amount, account_id):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE balances SET date = %s, amount = %s, account_id = %s WHERE id = %s" , (date, amount, account_id, id))
        conn.commit()
    except psycopg2.Error as e:
        print(f"message: site crashed because this error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def delete_balance_by_id(balance_id):
    conn = None
    cur = None
    item_deleted = 0
    try: 
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM balances WHERE id = %s", (balance_id,))
        conn.commit()
        item_deleted = cur.rowcount


    except psycopg2.Error as e:
        print(f"message: item could not be deleted because of this error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
    return item_deleted







