import yfinance as yf
import sqlite3

def fetch_and_store_stock_data(symbol, company_name):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1mo")  # Fetches the last month of data

    conn = sqlite3.connect('non_api_stocks.db')
    cursor = conn.cursor()

    for date, row in hist.iterrows():
        closing_price = row['Close']
        opening_price = row['Open']
        change = closing_price - opening_price
        date_str = date.strftime('%Y-%m-%d')

        cursor.execute('''
        INSERT INTO stock_prices (company_name, company_token, date, closing_price, change)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            company_name,
            symbol,
            date_str,
            closing_price,
            change
        ))

    conn.commit()
    conn.close()

def get_stock_data_by_date(from_date, to_date):
    conn = sqlite3.connect('non_api_stocks.db')
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


