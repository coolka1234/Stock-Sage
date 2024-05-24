import yfinance as yf
import sqlite3
import datetime
class StockAction():
    def __init__(self, row_number=1):
        self.row_number = row_number
        row = StockAction.get_row_by_number(self.row_number)
        self.id = row[0]
        self.company_name = row[1].split(' ')[0]
        self.company_token = row[2]
        self.date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        self.opening_price = row[4]
        self.closing_price = row[5]
        self.change = row[6]
    
    def get_row_by_number(row_number):
        conn = sqlite3.connect('non_api_stocks.db')
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