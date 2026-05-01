from database import create_connection
import sqlite3

# def add_customer(first_name, last_name, email):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('''
#         INSERT INTO customer (first_name, last_name, email)
#         VALUES (?, ?, ?)
#     ''', (first_name, last_name, email))

#     conn.commit()
#     conn.close()
#     print("Customer added successfully.")


def add_customer(first_name, last_name, email):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO customer (first_name, last_name, email)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, email))

        conn.commit()
        print("Customer added successfully.")

    except sqlite3.IntegrityError:
        print("❌ Error: Email already exists. Please use a different email.")

    conn.close()    

def view_customers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()

    conn.close()
    return rows

def create_account(account_type, currency_code):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO account (account_type, currency_code)
        VALUES (?, ?)
    ''', (account_type, currency_code))

    conn.commit()
    conn.close()
    print("Account created.")