import os
import yfinance as yf
import sqlite3
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
class StockAction():
    def __init__(self, row_number=1, temp=False):
        self.row_number = row_number
        row = []
        if temp:
            row =StockAction.get_row_by_number_temp(self.row_number)
        else:
            row = StockAction.get_row_by_number(self.row_number)
        # row = StockAction.get_row_by_number(self.row_number)
        self.id = row[0]
        self.company_name = row[1].split(' ')[0]
        self.company_token = row[2]
        self.date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        self.opening_price = row[4]
        self.closing_price = row[5]
        self.change = row[6]
    
    def get_row_by_number(row_number):
        conn = sqlite3.connect('src/database/non_api_stocks.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM stock_prices WHERE id = ?', (row_number,))

        row = cursor.fetchone()
        conn.close()
        return row
    def graph_stock_data(symbol, period='1mo', interval='1d'):
        if period == '':
            period = '1mo'
        if symbol == '':
            return
        if interval == '':
            interval = '1d'
        plt.ioff()
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period, interval=interval)
        data.index = pd.to_datetime(data.index)
        mpf.plot(data, type='candle', style='charles', title=symbol, volume=True)
        if os.path.exists('plots/stock_data.png'):
            os.remove('plots/stock_data.png')
        if not os.path.exists('plots'):
            os.makedirs('plots')
        plt.savefig('plots/stock_data.png', bbox_inches='tight')
        plt.close()
    
    def get_row_by_number_temp(row_number):
        conn = sqlite3.connect('src/database/temporary_stocks.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM stock_prices WHERE id = ?', (row_number,))

        row = cursor.fetchone()
        conn.close()
        return row

if __name__=='__main__':
    stock_symbol = 'AAPL'
    stock = StockAction(stock_symbol)
    print(stock.price)
    print(stock.change)
    print(stock.volume)
    print(stock.prev_close)
    print(stock.open)
    print(stock.avg_daily_volume)
    print(stock.stock_exchange)