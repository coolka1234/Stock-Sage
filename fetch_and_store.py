from newsapi import NewsApiClient
from api_codes import news_api
from database_create import create_temp_news_database
import sqlite3

newsapi = NewsApiClient(api_key=news_api)

def fetch_and_store_articles(keyword=None, from_date=None, to_date=None, language='en-US', sort_by='publishedAt'):
    articles = newsapi.get_everything(q=keyword, from_param=from_date, to=to_date, language=language, sort_by=sort_by)
    print(articles)
    store_articles_in_db(articles['articles'])
    return articles

def fetch_and_store_articles_to_temporary_db(keyword=None, from_date=None, to_date=None, language='en-US', sort_by='publishedAt'):

    articles = newsapi.get_everything(q=keyword, from_param=from_date, to=to_date, language=language, sort_by=sort_by)
    print(articles)
    store_articles_in_temporary_db(articles['articles'])
    return articles

def store_articles_in_temporary_db(articles):
    conn = sqlite3.connect('temporary_news.db')
    cursor = conn.cursor()

    for article in articles:
        cursor.execute('''
        INSERT INTO articles (source, author, title, description, url, published_at, content, companies)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            article['source']['name'],
            article.get('author'),
            article['title'],
            article.get('description'),
            article['url'],
            article['publishedAt'],
            article.get('content'),
            '',
        ))

    conn.commit()
    conn.close()


def store_articles_in_db(articles):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    for article in articles:
        cursor.execute('''
        INSERT INTO articles (source, author, title, description, url, published_at, content, companies)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            article['source']['name'],
            article.get('author'),
            article['title'],
            article.get('description'),
            article['url'],
            article['publishedAt'],
            article.get('content'),
            '',
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
