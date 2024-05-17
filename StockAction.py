class StockAction():
    def __init__(self, stock):
        self.stock = stock

    def buy(self, amount):
        self.stock.buy(amount)

    def sell(self, amount):
        self.stock.sell(amount)