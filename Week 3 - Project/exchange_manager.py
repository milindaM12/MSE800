
from database import create_connection
from datetime import datetime

def create_exchange(from_currency, to_currency, rate, fee):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO exchange (from_currency, to_currency, exchange_rate, fee, exchange_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (from_currency, to_currency, rate, fee, datetime.now()))

    conn.commit()
    conn.close()
    print("Exchange recorded.")

def view_exchanges():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM exchange")
    rows = cursor.fetchall()

    conn.close()
    return rows