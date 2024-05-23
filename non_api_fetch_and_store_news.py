from newspaper import Article, Source
import sqlite3
from datetime import datetime
from config import config
from non_api_create_news_database import create_news_database
from newspaper import Article, build
import sqlite3
from datetime import datetime
import urllib

def fetch_article(url):
    try:
        article = Article(url, config=config)
        article.download()
        article.parse()
        return {
            'source': article.source_url,
            'author': article.authors,
            'title': article.title,
            'description': article.meta_description,
            'url': article.url,
            'published_at': article.publish_date,
            'content': article.text
        }
    except Exception as e:
        print(f"Error fetching article from {url}: {e}")
        return None

def fetch_and_store_articles_from_sites(site_urls):
    conn = sqlite3.connect('non_api_news.db')
    cursor = conn.cursor()

    for site_url in site_urls:
        site_url = site_url.strip()
        paper = build(site_url, memoize_articles=False)
        for article in paper.articles:
            article_data = fetch_article(article.url)
            if article_data:
                cursor.execute('''
                INSERT INTO articles (source, author, title, description, url, published_at, content)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    article_data['source'],
                    ', '.join(article_data['author']),
                    article_data['title'],
                    article_data['description'],
                    article_data['url'],
                    article_data['published_at'].strftime('%Y-%m-%d %H:%M:%S') if article_data['published_at'] else None,
                    article_data['content']
                ))

    conn.commit()
    conn.close()

# Example site URL list
site_urls = [
    'https://www.bbc.com',
    'https://www.cnn.com',
    'https://www.techcrunch.com'
]
def get_articles_by_date(from_date, to_date):
    conn = sqlite3.connect('non_api_news.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM articles WHERE published_at BETWEEN ? AND ?
    ''', (from_date, to_date))

    articles = cursor.fetchall()
    conn.close()

    return articles

def print_articles(articles):
    for article in articles:
        print(f"Title: {article[3]}")
        print(f"Source: {article[1]}")
        print(f"Author: {article[2]}")
        print(f"Published At: {article[6]}")
        print(f"Description: {article[4]}")
        print(f"URL: {article[5]}")
        print(f"Content: {article[7]}")
        print("-" * 80)

def main():
    create_news_database()

    # Fetch and store articles from sites
    site_urls = [
        'https://www.bbc.com',
        'https://www.cnn.com',
        'https://www.techcrunch.com'
    ]
    fetch_and_store_articles_from_sites(site_urls)

    # Query articles by date
    articles = get_articles_by_date('2023-05-01', '2023-05-23')
    print_articles(articles)

if __name__ == "__main__":
    main()
