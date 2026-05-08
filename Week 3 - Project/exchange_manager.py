from database import create_connection
from datetime import datetime

def perform_exchange(account_id, from_currency, to_currency, amount):
    conn = create_connection()
    cursor = conn.cursor()

    # 1. Get exchange rate
    cursor.execute('''
        SELECT exchange_rate_to_usd FROM currency WHERE currency_code = ?
    ''', (to_currency,))
    rate_row = cursor.fetchone()

    if not rate_row:
        print("Invalid target currency.")
        return

    rate = rate_row[0]

    # 2. Calculate converted amount
    converted_amount = amount * rate
    fee = converted_amount * 0.02  # 2% fee

    # 3. Insert exchange
    cursor.execute('''
        INSERT INTO exchange (from_currency, to_currency, exchange_rate, fee, exchange_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (from_currency, to_currency, rate, fee, datetime.now()))

    exchange_id = cursor.lastrowid

    # 4. Insert transaction
    cursor.execute('''
        INSERT INTO transactions (account_id, exchange_id, transaction_type, amount, transaction_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (account_id, exchange_id, "EXCHANGE", amount, datetime.now(), "SUCCESS"))

    conn.commit()
    conn.close()

    print(f"Exchange successful!")
    print(f"Converted Amount: {converted_amount}")
    print(f"Fee Charged: {fee}")