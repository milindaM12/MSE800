from database import create_connection

def add_currency(code, name, rate):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO currency (currency_code, currency_name, exchange_rate_to_usd)
        VALUES (?, ?, ?)
    ''', (code, name, rate))

    conn.commit()
    conn.close()
    print("Currency added.")

def view_currencies():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM currency")
    rows = cursor.fetchall()

    conn.close()
    return rows