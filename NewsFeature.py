import sqlite3
from collections import namedtuple
class NewsFeature():
    def __init__(self, num_from_db=1):
        self.num_from_db = num_from_db
        row= NewsFeature.get_row_by_number(self.num_from_db)
        # self.NewsAttributes = namedtuple('NewsAttributes', ['id, source, author, title, description, url, date, content'])
        # self.NewsAttributes.id=row[0]
        # self.NewsAttributes.source=row[1]
        # self.NewsAttributes.author=row[2]
        # self.NewsAttributes.title=row[3]
        # self.NewsAttributes.description=row[4]
        # self.NewsAttributes.url=row[5]
        # self.NewsAttributes.date=row[6]
        # self.NewsAttributes.content=row[7]
        self.id = row[0]
        self.source = row[1]
        self.author = row[2]
        self.title = row[3]
        self.description = row[4]
        self.url = row[5]
        self.date = row[6]
        self.content = row[7]
        self.row=row

    def get_row_by_number(row_number):
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM articles WHERE id = ?', (row_number,))

        row = cursor.fetchone()
        conn.close()
        return row
