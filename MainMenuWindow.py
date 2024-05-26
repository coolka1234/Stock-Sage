from MainMenu import Ui_MainMenuWindow
from NewsBriefingWindow import NewsBriefingWindow
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from StockPredictionWindow import StockPredictionWindow
from StockBriefingWindow import StockBriefingWindow
class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.w = None
        self.w1 = None
        self.w2 = None
        self.pushButtonNewsBriefing.clicked.connect(self.openNewWindow)
        self.pushButtonStockPrediction.clicked.connect(self.openNewWindowStockPrediction)
        self.pushButtonStockBriefing.clicked.connect(self.openNewWindowStockBriefing)
    def openNewWindow(self):
        if self.w is None:
            self.w = NewsBriefingWindow()
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.
    
    def openNewWindowStockPrediction(self):
        if self.w1 is None:
            self.w1 = StockPredictionWindow()
            self.w1.show()
        else:
            self.w1.close()
    
    def openNewWindowStockBriefing(self):
        if self.w2 is None:
            self.w2 = StockBriefingWindow()
            self.w2.show()
        else:
            self.w2.close()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainMenuWindow()
    app.exec()