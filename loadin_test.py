# load_predict.py

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

# Load the model
model = load_model('stock_prediction_model.h5')

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Example new data for prediction
new_articles = ['Apple announces new iPhone with groundbreaking features.']
new_open_prices = [150.0]  # Example open price

# Preprocess and vectorize the new data
new_articles = [preprocess_text(article) for article in new_articles]
new_data_text_features = vectorizer.transform(new_articles).toarray()
new_data_stock_features = np.array(new_open_prices).reshape(-1, 1)  # Reshape to (n_samples, 1)

# Combine text features and stock features
new_combined_features = np.hstack((new_data_text_features, new_data_stock_features))

# Reshape for LSTM model (samples, timesteps, features)
new_combined_features = np.expand_dims(new_combined_features, axis=1)

# Make predictions with the loaded model
predicted_stock_price = model.predict(new_combined_features)
print(f'Predicted Stock Price: {predicted_stock_price[0][0]}')
