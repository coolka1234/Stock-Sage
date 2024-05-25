from datetime import date, datetime
from re import S
from NewsBriefing import Ui_MainMenuWindow
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt6.QtCore import QDateTime, QDate
from fetch_and_store import fetch_and_store_articles, get_articles_by_date
from utility_functions import change_date_format, find_between
from PyQt6.QtCore import QDateTime, QDate
from SingleArticleWindow import SingleArticleWindow
from NewsFeature import NewsFeature

class NewsBriefingWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.fillComboBoxes()
        self.set_min_date()
        self.set_max_date()
        self.pushButtonExecute.clicked.connect(self.fillNewsList)
        self.listWidgetNews.itemDoubleClicked.connect(self.open_news)
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
            language_sel='en'
        else:
            language=self.comboBox.currentText()
        if self.comboBox_2.currentText() is None or self.comboBox_2.currentText() == '':
            sort_by_sel='publishedAt'
        else:
            sort_by_sel=self.comboBox_2.currentText()
        articles_dict= fetch_and_store_articles(keyword=self.lineEditKeywoardInput.text(), from_date=date_from, to_date=date_to, language=language_sel, sort_by=sort_by_sel)
        self.listWidgetNews.addItem(f"Total results: {articles_dict['totalResults']}")
        for article in articles_dict['articles']:
            item = f"Title: {article['title']}\n" \
                   f"Description: {article['description']}\n" \
                   f"URL: {article['url']}\n" \
                   f"Published at: {article['publishedAt']}\n" \
                   f"Content: {article['content']}\n" \
                   "-------------------------------------------------"
            self.listWidgetNews.addItem(item)

    def open_news(self):
        clicked_item = self.listWidgetNews.currentItem().text()
        description = find_between(clicked_item, 'Description: ', '\nURL')
        self.news= SingleArticleWindow(NewsFeature=NewsFeature(NewsFeature.get_id_by_description(description)))
        self.news.show()

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