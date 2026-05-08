from database import create_connection
from datetime import datetime

def create_transaction(account_id, exchange_id, amount, t_type):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (account_id, exchange_id, transaction_type, amount, transaction_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (account_id, exchange_id, t_type, amount, datetime.now(), "SUCCESS"))

    conn.commit()
    conn.close()
    print("Transaction completed.")