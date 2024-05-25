from NewsBriefing import Ui_MainMenuWindow
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
class NewsBriefingWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
    def openNewWindow(self):
        self.hide()
        self.newWindow = QMainWindow()
        # self.ui = Ui_MainMenuWindow()
        # self.ui.setupUi(self.newWindow)
        self.newWindow.show()
    def fillComboBoxes(self):
        languages={'es', 'he', 'se', 'it', 'ru', 'sv', 'ar', 'no', 'nl', 'en-US', 'en', 'pt', 'cn', 'de', 'zh', 'fr', 'ud'}
        self.comboBox.addItems(languages)
        sort_by = {'relevancy', 'popularity', 'publishedAt'}
        self.comboBox_2.addItems(sort_by)
    
if __name__ == "__main__":
    app = QApplication([])
    window = NewsBriefingWindow()
    app.exec_()