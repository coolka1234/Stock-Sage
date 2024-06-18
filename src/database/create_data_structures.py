import numpy as np
import src.database.NewsFeature as NewsFeature
import sqlite3
import src.StockAction as StockAction



def np_news():
    news_array=np.array([])
    conn = sqlite3.connect('src/database/news.db')
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
    conn = sqlite3.connect('src/database/non_api_stocks.db')
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