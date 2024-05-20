import newspaper
import nltk
from newspaper import Article
import requests
from bs4 import BeautifulSoup
import re
from config import config
class NewsArticle():
    def __init__(self, url):
        self.url = url
        self.article = Article(url, config=config)
        self.article.download()
        self.article.parse()
        self.article.nlp()
        self.title = self.article.title
        self.text = self.article.text
        self.authors = self.article.authors
        self.publish_date = self.article.publish_date
        self.top_image = self.article.top_image
        self.keywords = self.article.keywords
        self.summary = self.article.summary
        self.html = self.article.html
        self.meta_data = self.article.meta_data
        self.tags = self.article.tags
        self.source = self.article.source_url
    
    def get_nlp(self):
        return self.article.nlp()

if __name__=='__main__':
    url = 'https://businessinsider.com.pl/gospodarka/microsoft-stawia-na-ai-zatrudnia-slynnego-menedzera/n8j2bfm'
    article = NewsArticle(url)
    print(article.title)
    print(article.text)
    print(article.publish_date)
    print(article.keywords)