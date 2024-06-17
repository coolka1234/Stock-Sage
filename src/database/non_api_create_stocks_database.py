import sqlite3

def create_stock_database():
    conn = sqlite3.connect('src/database/non_api_stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        company_token TEXT,
        date TEXT,
        opening_price REAL,
        closing_price REAL,
        change REAL
    )
    ''')

    conn.commit()
    conn.close()

def delete_stock_database():
    conn = sqlite3.connect('src/database/non_api_stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS stock_prices
    ''')

    conn.commit()
    conn.close()
