import sqlite3

def create_news_database():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        author TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        published_at TEXT,
        content TEXT
        companies TEXT
    )
    ''')

    conn.commit()
    conn.close()

def create_temp_news_database():
    conn = sqlite3.connect('temporary_news.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        author TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        published_at TEXT,
        content TEXT,
        companies TEXT
    )
    ''')

    conn.commit()
    conn.close()


def create_stock_database():
    conn = sqlite3.connect('stocks.db')
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

def create_temp_stock_database():
    conn = sqlite3.connect('temporary_stocks.db')
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

def delete_news_database():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS articles
    ''')

    conn.commit()
    conn.close()

def delete_temp_news_database():
    conn = sqlite3.connect('temporary_news.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS articles
    ''')

    conn.commit()
    conn.close()

def delete_stock_database():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS stock_prices
    ''')

    conn.commit()
    conn.close()

def delete_temp_stock_database():
    conn = sqlite3.connect('temporary_stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS stock_prices
    ''')

    conn.commit()
    conn.close()
