import yfinance as yf
from newspaper import Article
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense
from datetime import datetime
import nltk
nltk.download('punkt')


def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.publish_date, article.summary

def fetch_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    hist = stock.history(start=start_date, end=end_date)
    return hist

urls = ['https://example.com/news_article1', 'https://example.com/news_article2']
articles = [fetch_article(url) for url in urls]

symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'
stock_data = fetch_stock_data(symbol, start_date, end_date)

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

summaries = [preprocess_text(article[1]) for article in articles]
dates = [article[0] for article in articles]

vectorizer = TfidfVectorizer(max_features=500)
text_features = vectorizer.fit_transform(summaries).toarray()

def align_stock_data_with_articles(dates, stock_data):
    stock_features = []
    for date in dates:
        stock_info = stock_data.loc[date.strftime('%Y-%m-%d')]
        stock_features.append(stock_info[['Open', 'Close']].values)
    return np.array(stock_features)

dates = [date for date in dates if date.strftime('%Y-%m-%d') in stock_data.index]
stock_features = align_stock_data_with_articles(dates, stock_data)

combined_features = np.hstack((text_features, stock_features))

X_train, X_test, y_train, y_test = train_test_split(combined_features[:-1], stock_data['Close'].values[1:], test_size=0.2, random_state=42)

X_train = np.expand_dims(X_train, axis=1)
X_test = np.expand_dims(X_test, axis=1)

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(50))
model.add(Dense(1))  # Output layer for predicting stock price

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

from sklearn.metrics import mean_squared_error

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
