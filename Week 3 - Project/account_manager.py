from database import create_connection

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

def view_accounts():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM account")
    rows = cursor.fetchall()

    conn.close()
    return rows