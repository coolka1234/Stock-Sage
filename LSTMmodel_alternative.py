# train_save_model.py

import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from datetime import datetime
import pandas as pd
import pickle
import nltk
nltk.download('punkt')

# Import custom modules
from create_data_structures import np_news, np_stock
from NewsFeature import NewsFeature
from StockAction import StockAction

# Fetch data
articles: np.ndarray[NewsFeature] = np_news()
stock_data: np.ndarray[StockAction] = np_stock()

# Preprocess text
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

for article in articles:
    article.content = preprocess_text(article.content)

# Combine news articles with stock data
combined_data = []
for entry in stock_data:
    news = [article.content for article in articles if article.real_date == entry.date and entry.company_name in article.companies]
    combined_data.append({'date': entry.date, 'company': entry.company_name, 'open_price': entry.opening_price, 'close_price': entry.closing_price, 'articles': news})

# Filter out entries with no articles
combined_data = [entry for entry in combined_data if entry['articles']]

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(max_features=500)
all_articles = [' '.join(entry['articles']) for entry in combined_data]
text_features = vectorizer.fit_transform(all_articles).toarray()

# Combine text features with stock data
features = []
targets = []
for i, entry in enumerate(combined_data):
    open_price = entry['open_price']
    combined_features = np.hstack((text_features[i], [open_price]))  # Only include open_price
    features.append(combined_features)
    targets.append(entry['close_price'])  # Use close_price as the target

features = np.array(features)
targets = np.array(targets)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)

# Reshape data for LSTM (samples, timesteps, features)
X_train = np.expand_dims(X_train, axis=1)
X_test = np.expand_dims(X_test, axis=1)

# Define the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(50))
model.add(Dense(1))  # Output layer for predicting stock price

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=200, batch_size=32, validation_data=(X_test, y_test))

# Save the model and vectorizer
model.save('stock_prediction_model.h5')
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print('Model and vectorizer saved.')
