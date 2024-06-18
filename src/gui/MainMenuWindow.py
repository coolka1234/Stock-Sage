import os
from src.gui.MainMenu import Ui_MainMenuWindow
from src.gui.NewsBriefingWindow import NewsBriefingWindow
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from src.gui.StockPredictionWindow import StockPredictionWindow
from src.gui.StockBriefingWindow import StockBriefingWindow
import logging
class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        logging.basicConfig( level=logging.DEBUG, filename='docs/logs.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        super().__init__()
        self.setupUi(self)
        self.show()
        self.w = None
        self.w1 = None
        self.w2 = None
        self.pushButtonNewsBriefing.clicked.connect(self.openNewWindow)
        self.pushButtonStockPrediction.clicked.connect(self.openNewWindowStockPrediction)
        self.pushButtonStockBriefing.clicked.connect(self.openNewWindowStockBriefing)
        self.pushButtonUserManual.clicked.connect(self.display_user_manual)
        self.pushButtonUserManualExit.clicked.connect(self.close)
    def openNewWindow(self):
        if self.w is None:
            self.w = NewsBriefingWindow(self)
            logging.debug('News Briefing window opened')
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.
    
    def openNewWindowStockPrediction(self):
        if self.w1 is None:
            self.w1 = StockPredictionWindow(self)
            logging.debug('Stock Prediction window opened')
            self.w1.show()
        else:
            self.w1.close()
            self.w1 = None
    
    def openNewWindowStockBriefing(self):
        if self.w2 is None:
            logging.debug('Stock Briefing window opened')
            self.w2 = StockBriefingWindow(self)
            self.w2.show()
        else:
            self.w2.close()
            self.w2 = None
    def closeEvent(self, event):
        if self.w is not None:
            self.w.close()
        if self.w1 is not None:
            self.w1.close()
        if self.w2 is not None:
            self.w2.close()
        if os.path.exists('database/temporary_news.db'):
            logging.debug('Removing temporary news database')
            os.remove('database/temporary_news.db')
        if os.path.exists('database/temporary_stocks.db'):
            logging.debug('Removing temporary stocks database')
            os.remove('database/temporary_stocks.db')
        event.accept()
    def display_user_manual(self):
        logging.debug('User manual opened')
        QMessageBox.information(self, 'User Manual', 'Welocme to Stock Sage!\n Current veriosn: 1.0.1 \n In order to read the news, please double click selected item. \n For stock vieweing, please enter the symbol and select the period and interval. \n For stock prediction, please enter the symbol and select the period and interval. \n For more information, please visit: https://github.com/coolka1234/AI-News-Trader \n Enjoy!')
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainMenuWindow()
    app.exec()