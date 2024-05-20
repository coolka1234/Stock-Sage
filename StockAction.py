import yfinance as yf
class StockAction():
    def __init__(self, stock_symbol):
        self.stock = yf.Ticker(stock_symbol)
        self.stock_symbol = stock_symbol
        self.price = self.stock.history(period='1d')['Close'].iloc[0]
        self.change = self.stock.history(period='1d')['Close'].iloc[0] - self.stock.history(period='1d')['Open'].iloc[0]
        self.volume = self.stock.history(period='1d')['Volume'].iloc[0]
        self.prev_close = self.stock.history(period='1d')['Close'].iloc[0]
        self.open = self.stock.history(period='1d')['Open'].iloc[0]
        self.avg_daily_volume = self.stock.info['averageVolume']
        self.stock_exchange = self.stock.info['exchange']
        self.dividend_yield = self.stock.info['dividendYield']

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