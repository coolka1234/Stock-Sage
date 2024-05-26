import csv
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from StockPrediction import Ui_MainMenuWindow
import numpy as np
import re
import datetime
import sqlite3
from utility_functions import date_to_ISO_8601
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from datetime import date, datetime
from NewsFeature import NewsFeature
from StockAction import StockAction
from fetch_and_store import fetch_and_store_articles, fetch_and_store_articles_to_temporary_db, get_articles_by_date
from non_api_fetch_and_store_stocks import fetch_and_store_stock_data, fetch_and_store_stock_data_to_temporary_db, get_stock_data_by_date, print_stock_data
import nltk
nltk.download('punkt')
import sys

def np_news():
    news_array=np.array([])
    conn = sqlite3.connect('temporary_news.db')
    cursor = conn.cursor()
    table_name = 'articles'
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    for i in range(1, row_count):
        curr_news= NewsFeature.NewsFeature(i)
        news_array=np.append(news_array,curr_news)
    conn.close()
    return news_array

def np_stock():
    stock_array=np.array([])
    conn = sqlite3.connect('temporary_stocks.db')
    cursor = conn.cursor()
    table_name = 'stock_prices'
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    for i in range(1, row_count):
        curr_stock= StockAction.StockAction(i)
        stock_array=np.append(stock_array,curr_stock)
    conn.close()
    return stock_array

def append_if_not_exists(file_path, data):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        if data in reader:
            return 
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    

class StockPredictionWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.model=load_model('stock_prediction_model.h5')
        
    
    def display_prediction(self, symbol, name):
        append_if_not_exists('companies_of_interest.csv', name)
        date_today=datetime.datetime.now()
        date_yesterday=date_today-datetime.timedelta(days=1)
        date_yesterday=date_to_ISO_8601(date_yesterday)
        date_today=date_to_ISO_8601(date_today)
        self.progressBar.setValue(10)
        fetch_and_store_articles_to_temporary_db(keyword=symbol, from_date=date_yesterday, to_date=date_today, language='en', sort_by='publishedAt')
        fetch_and_store_stock_data_to_temporary_db(symbol, symbol, period='1d')
        news=np_news()
        stock=np_stock()
        news_vectorizer=TfidfVectorizer(max_features=500)
        new_data_news=news_vectorizer.transform(news)
        combined_features=np.hstack((new_data_news, stock))
        combined_features = np.expand_dims(combined_features, axis=1)
        predicted_stock_price = self.model.predict(combined_features)
        self.labelRaport.setText(f'Predicted stock price for {name} is {predicted_stock_price}')



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=StockPredictionWindow()
    window.show()
