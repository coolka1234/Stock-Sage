from MainMenu import Ui_MainMenuWindow
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButtpnNewsBriefing.clicked.connect(self.openNewWindow)
    def openNewWindow(self):
        self.hide()
        self.newWindow = QMainWindow()
        # self.ui = Ui_MainMenuWindow()
        # self.ui.setupUi(self.newWindow)
        self.newWindow.show()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainMenuWindow()
    app.exec_()