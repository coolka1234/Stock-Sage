import newspaper
import nltk
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
#from config import config
class NewsArticle():
    def __init__(self, url):
        self.url = url
        self.article = newspaper.Article(url)
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
    def get_publish_time(self):
        driver = webdriver.Firefox()  # or webdriver.Chrome()
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time_tag = soup.find('time')  # or any other method to find the time tag
        driver.quit()
        if time_tag:
            return time_tag.get('datetime')  # or any other method to extract the time
        return None

if __name__=='__main__':
    url = 'https://www.bloomberg.com/news/articles/2024-05-19/asian-stocks-to-rise-after-us-gains-china-support-markets-wrap'
    article = NewsArticle(url)
    # print(article.title)
    # print(article.text)
    # print(article.publish_date)
    print(article.summary)
    print(article.keywords)
    #print(article.get_publish_time())