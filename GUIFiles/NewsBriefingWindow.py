from datetime import date, datetime
from NewsBriefing import Ui_MainMenuWindow
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt6.QtCore import QDateTime, QDate
import sys
sys.path.insert(0, '..')
from fetch_and_store import fetch_and_store_articles, get_articles_by_date
from utility_functions import change_date_format
from PyQt6.QtCore import QDateTime, QDate


class NewsBriefingWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.fillComboBoxes()
        self.set_min_date()
        self.set_max_date()
        self.pushButtonExecute.clicked.connect(self.fillNewsList)
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
    
    def fillNewsList(self):
        self.listWidgetNews.clear()
        date_from = str(self.dateTimeEditFrom.text())
        date_to = str(self.dateTimeEditTo.text())
        date_from = change_date_format(date_from)
        date_to = change_date_format(date_to)
        if self.comboBox.currentText() is None or self.comboBox.currentText() == '':
            language='en-US'
        else:
            language=self.comboBox.currentText()
        if self.comboBox_2.currentText() is None or self.comboBox_2.currentText() == '':
            sort_by='publishedAt'
        else:
            sort_by=self.comboBox_2.currentText()
        print(date_from)
        print(date_to)
        print(self.lineEditKeywoardInput.text())
        print(language)
        print(sort_by)
        articles_dict= fetch_and_store_articles(keyword=self.lineEditKeywoardInput.text(), from_date=date_from, to_date=date_to, language=language, sort_by=sort_by)
        for article in articles_dict['articles']:
            self.listWidgetNews.addItem(f"Title: {article['title']}")
            self.listWidgetNews.addItem(f"Description: {article['description']}")
            self.listWidgetNews.addItem(f"URL: {article['url']}")
            self.listWidgetNews.addItem(f"Published at: {article['publishedAt']}")
            self.listWidgetNews.addItem(f"Content: {article['content']}")
            self.listWidgetNews.addItem("-------------------------------------------------")


    def set_min_date(self):
        current_date = QDateTime.currentDateTime()

        min_date = current_date.addDays(-29)
        self.dateTimeEditFrom.setMinimumDateTime(min_date)
    
    def set_max_date(self):
        current_date = QDateTime.currentDateTime()
        self.dateTimeEditTo.setDate(current_date.date())
        self.dateTimeEditTo.setMaximumDateTime(current_date)
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = NewsBriefingWindow()
    app.exec()