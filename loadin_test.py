# load_predict.py

from hmac import new
from turtle import st
import numpy as np
from tensorflow.keras.models import load_model
import pickle
import re
import matplotlib.pyplot as plt

# Preprocess text function
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text
def load_predict(news_array, stock_array):
    model = load_model('stock_prediction_model.h5')
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    new_articles = news_array.tolist()
    new_open_prices = [stock_array]
    new_articles = [preprocess_text(article) for article in new_articles]
    new_data_text_features = vectorizer.transform(new_articles).toarray()
    new_data_stock_features = np.array(new_open_prices).reshape(-1, 1)  # Reshape to (n_samples, 1)
    new_combined_features = np.hstack((new_data_text_features, new_data_stock_features))
    new_combined_features = np.expand_dims(new_combined_features, axis=1)
    new_combined_features = np.asarray(new_combined_features).astype(np.float32)
    predicted_stock_price = model.predict(new_combined_features)
    return predicted_stock_price