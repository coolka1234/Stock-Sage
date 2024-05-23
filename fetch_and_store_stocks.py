import requests
import sqlite3
from datetime import datetime
from api_codes import alpha_api

ALPHA_VANTAGE_API_KEY = alpha_api

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def store_stock_data(symbol, company_name):
    data = fetch_stock_data(symbol)
    time_series = data.get('Time Series (Daily)', {})

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    for date, values in time_series.items():
        closing_price = float(values['4. close'])
        opening_price = float(values['1. open'])
        change = closing_price - opening_price

        cursor.execute('''
        INSERT INTO stock_prices (company_name, company_token, date, closing_price, change)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            company_name,
            symbol,
            date,
            closing_price,
            change
        ))

    conn.commit()
    conn.close()
def get_stock_data_by_date(from_date, to_date):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM stock_prices WHERE date BETWEEN ? AND ?
    ''', (from_date, to_date))

    stocks = cursor.fetchall()
    conn.close()

    return stocks

def print_stock_data(stocks):
    for stock in stocks:
        print(f"Company Name: {stock[1]}")
        print(f"Company Token: {stock[2]}")
        print(f"Date: {stock[3]}")
        print(f"Closing Price: {stock[4]}")
        print(f"Change: {stock[5]}")
        print("-" * 80)
