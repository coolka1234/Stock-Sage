import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential # type: ignore (this has to be here, its a known keras bug)
from tensorflow.keras.layers import LSTM, Dense # type: ignore
import pickle
import nltk
nltk.download('punkt')

from src.database.create_data_structures import np_news, np_stock
from src.database.NewsFeature import NewsFeature
from src.StockAction import StockAction

articles: np.ndarray[NewsFeature] = np_news()
stock_data: np.ndarray[StockAction] = np_stock()

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

for article in articles:
    article.content = preprocess_text(article.content)

combined_data = []
for entry in stock_data:
    news = [article.content for article in articles if article.real_date == entry.date and entry.company_name in article.companies]
    combined_data.append({'date': entry.date, 'company': entry.company_name, 'open_price': entry.opening_price, 'close_price': entry.closing_price, 'articles': news})

combined_data = [entry for entry in combined_data if entry['articles']]

vectorizer = TfidfVectorizer(max_features=500)
all_articles = [' '.join(entry['articles']) for entry in combined_data]
text_features = vectorizer.fit_transform(all_articles).toarray()

features = []
targets = []
weight_factor = 1000 # zwracaj szczegolna uwage na otwarcie!!!!!!
for i, entry in enumerate(combined_data):
    # open_price = entry['open_price']
    # combined_features = np.hstack((text_features[i], [open_price]))
    # features.append(combined_features)
    # targets.append(entry['close_price'])  
    open_price = entry['open_price']
    weighted_open_price = np.full((weight_factor,), open_price)
    combined_features = np.hstack((text_features[i], weighted_open_price)) 
    features.append(combined_features)
    targets.append(entry['close_price'])
    

features = np.array(features)
targets = np.array(targets)

feature_scaler = MinMaxScaler()
target_scaler = MinMaxScaler()

features = feature_scaler.fit_transform(features)
targets = target_scaler.fit_transform(targets.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)
X_train = np.expand_dims(X_train, axis=1)
X_test = np.expand_dims(X_test, axis=1)

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(50)) # zwraca output na kazdym kroku
model.add(Dense(1))  

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=2000, batch_size=32, validation_data=(X_test, y_test))

model.save('src/models/stock_prediction_model.h5')
with open('src/models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('src/models/feature_scaler.pkl', 'wb') as f:
    pickle.dump(feature_scaler, f)
with open('src/models/target_scaler.pkl', 'wb') as f:
    pickle.dump(target_scaler, f)
print('Model and vectorizer saved.')
