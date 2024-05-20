import re
from NewsArticle import NewsArticle
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()  
    return text

from sklearn.feature_extraction.text import TfidfVectorizer
news=NewsArticle('https://www.bloomberg.com/news/articles/2024-05-19/asian-stocks-to-rise-after-us-gains-china-support-markets-wrap')
summaries = [preprocess_text(article[1]) for article in news.keywords]
vectorizer = TfidfVectorizer(max_features=500)  
text_features = vectorizer.fit_transform(summaries).toarray()
print(text_features)