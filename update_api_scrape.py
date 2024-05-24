import sqlite3
import NewsFeature
def update_single_news_row(name, data, index):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE articles SET {name} = ? WHERE url = ?', (data, index))
    conn.commit()
    conn.close()

def scrape_content(url):
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('p')
    data = ''
    for i in content:
        data += i.text
    return data

def update_all_news():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    table_name = 'articles'
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    for i in range(1, row_count):
        curr_news= NewsFeature.NewsFeature(i)
        row = curr_news.row
        url = curr_news.url
        data = scrape_content(url)
        update_single_news_row('content', data, url)
    conn.close()