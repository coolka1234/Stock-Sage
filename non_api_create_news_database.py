import sqlite3

def create_news_database():
    conn = sqlite3.connect('non_api_news.db')
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
    )
    ''')

    conn.commit()
    conn.close()

create_news_database()
