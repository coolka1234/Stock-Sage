import sqlite3
from collections import namedtuple
import datetime
class NewsFeature():
    def __init__(self, num_from_db=1):
        self.num_from_db = num_from_db
        row= NewsFeature.get_row_by_number(self.num_from_db)
        self.id = row[0]
        self.source = row[1]
        self.author = row[2]
        self.title = row[3]
        self.description = row[4]
        self.url = row[5]
        self.date = row[6]
        self.content = row[7]
        self.real_date=datetime.datetime.strptime(self.date.split('T')[0], '%Y-%m-%d')
        self.companies=row[8]
        self.row=row

    def get_row_by_number(row_number):
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM articles WHERE id = ?', (row_number,))

        row = cursor.fetchone()
        conn.close()
        return row
    
    def get_row_by_description(description):
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM articles WHERE description = ?', (description,))

        row = cursor.fetchone()
        conn.close()
        return row
    def get_id_by_description(description):
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM articles WHERE description = ?', (description,))

        id = cursor.fetchone()
        conn.close()
        return id[0]
    
    def __str__(self):
        return f'{self.content}'
