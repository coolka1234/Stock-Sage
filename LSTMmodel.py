from math import comb
import yfinance as yf
from newspaper import Article
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from datetime import datetime
from create_data_structures import np_news, np_stock
from NewsFeature import NewsFeature
from StockAction import StockAction
import nltk
nltk.download('punkt')


articles : np.ndarray[NewsFeature]=np_news()
stock_data: np.ndarray[StockAction]=np_stock()


def preprocess_text(text):
    text = re.sub(r'\W', ' ', text) #znaki specjalne na spacje
    text = re.sub(r'\s+', ' ', text) #wiecej niz jedna spacja na jedna spacje
    text = re.sub(r'\d+', '', text) #usuwanie cyfr
    text = text.lower() #zmiana na male litery
    return text

for article in articles:
    article.content = preprocess_text(article.content)

combined_data = []

for entry in stock_data:
    news = [article.content for article in articles if article.real_date == entry.date and entry.company_name in article.companies]
    combined_data.append({'date': entry.date, 'company': entry.company_name, 'open_price': entry.open_price, 'close_price': entry.close_price, 'articles': articles})

combined_data = [entry for entry in combined_data if entry['articles']] #usuwanie pustych list

vectorizer = TfidfVectorizer(max_features=500)
all_articles = [' '.join(entry['articles']) for entry in combined_data]
text_features = vectorizer.fit_transform(all_articles).toarray()

features = []
targets = []

for i, entry in enumerate(combined_data):
    open_price = entry.open_price
    close_price = entry.close_price
    stock_features = [open_price, close_price]
    combined_features = np.hstack((text_features[i], stock_features))
    features.append(combined_features)
    targets.append(close_price)

features = np.array(features)
targets = np.array(targets)

X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)

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
