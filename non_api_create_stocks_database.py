import sqlite3

def create_stock_database():
    conn = sqlite3.connect('non_api_stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        company_token TEXT,
        date TEXT,
        closing_price REAL,
        change REAL
    )
    ''')

    conn.commit()
    conn.close()

create_stock_database()
