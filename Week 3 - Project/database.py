# import sqlite3

# def create_connection():
#     conn = sqlite3.connect("users.db")
#     return conn

# def create_table():
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE
#         )
#     ''')
#     conn.commit()
#     conn.close()

import sqlite3

def create_connection():
    conn = sqlite3.connect("finance.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # 1. CUSTOMER
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 2. CURRENCY
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currency (
            currency_code TEXT PRIMARY KEY,
            currency_name TEXT NOT NULL,
            symbol TEXT,
            country TEXT,
            exchange_rate_to_usd REAL,
            is_active INTEGER DEFAULT 1
        )
    ''')

    # 3. ACCOUNT (NO customer_id now ❗)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_type TEXT NOT NULL,
            balance REAL DEFAULT 0.0,
            currency_code TEXT,
            account_number TEXT UNIQUE,
            opened_date DATE,
            status TEXT,
            FOREIGN KEY (currency_code) REFERENCES currency(currency_code)
        )
    ''')

    # 4. ACCOUNT_HOLDER (JUNCTION TABLE ✅)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account_holder (
            account_holder_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            account_id INTEGER NOT NULL,
            role TEXT,
            added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY (account_id) REFERENCES account(account_id)
        )
    ''')

    # 5. EXCHANGE
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange (
            exchange_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_currency TEXT,
            to_currency TEXT,
            exchange_rate REAL,
            fee REAL,
            exchange_date DATETIME,
            FOREIGN KEY (from_currency) REFERENCES currency(currency_code),
            FOREIGN KEY (to_currency) REFERENCES currency(currency_code)
        )
    ''')

    # 6. TRANSACTION
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            exchange_id INTEGER,
            transaction_type TEXT,
            amount REAL,
            transaction_date DATETIME,
            status TEXT,
            description TEXT,
            FOREIGN KEY (account_id) REFERENCES account(account_id),
            FOREIGN KEY (exchange_id) REFERENCES exchange(exchange_id)
        )
    ''')

    conn.commit()
    conn.close()
