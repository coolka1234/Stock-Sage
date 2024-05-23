from newsapi import NewsApiClient
import sqlite3

# 1727a68759c54ed9a2cfddd60bd8232f
newsapi = NewsApiClient(api_key='1727a68759c54ed9a2cfddd60bd8232f')

def fetch_and_store_articles(keyword=None, from_date=None, to_date=None):
    articles = newsapi.get_everything(q=keyword, from_param=from_date, to=to_date, language='en', sort_by='publishedAt')
    store_articles_in_db(articles['articles'])

def store_articles_in_db(articles):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    for article in articles:
        cursor.execute('''
        INSERT INTO articles (source, author, title, description, url, published_at, content)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            article['source']['name'],
            article.get('author'),
            article['title'],
            article.get('description'),
            article['url'],
            article['publishedAt'],
            article.get('content')
        ))

    conn.commit()
    conn.close()

def get_articles_by_date(from_date, to_date):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM articles WHERE published_at BETWEEN ? AND ?
    ''', (from_date, to_date))

    articles = cursor.fetchall()
    conn.close()

    return articles
