import sqlite3

def create_database():
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
    )
    ''')

    conn.commit()
    conn.close()

create_database()
