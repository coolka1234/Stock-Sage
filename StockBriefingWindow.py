from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pandas import Period
from StockBriefing import Ui_MainMenuWindow
from StockAction import StockAction
class StockBriefingWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.fillComboBoxes()
        self.pushButtonExecute.clicked.connect(self.display_stock_data)
    def display_stock_data(self):
        symbol = self.lineEditSymbolnput.text()
        Period = self.comboBox.currentText()
        interval=self.comboBox_2.currentText()
        if symbol == '':
            return
        if (Period == ' '):
            Period = '1mo'
        # stock = StockAction(symbol)
        StockAction.graph_stock_data(symbol, Period, interval=interval)
        pixmap=QPixmap('plots/stock_data.png')
        self.labelSypckGraph.setPixmap(pixmap)
    
    def fillComboBoxes(self):
        periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.comboBox.addItems(periods)
        intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        self.comboBox_2.addItems(intervals)

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = StockBriefingWindow()
    window.show()
    sys.exit(app.exec())