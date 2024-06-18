from src.gui.NewsBriefing import Ui_MainMenuWindow
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PyQt6.QtCore import QDateTime
from src.database.database_create import delete_news_database
from src.database.fetch_and_store import fetch_and_store_articles
from src.utility_functions import change_date_format, find_between
from src.gui.SingleArticleWindow import SingleArticleWindow
from src.database.NewsFeature import NewsFeature
from src.update_api_scrape import update_single_news
import logging

class NewsBriefingWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self, main_window):
        logging.basicConfig( level=logging.DEBUG, filename='docs/logs.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        super().__init__()
        self.setupUi(self)
        self.show()
        self.fillComboBoxes()
        self.set_min_date()
        self.set_max_date()
        try:
            self.pushButtonExecute.clicked.connect(self.fillNewsList)
            self.listWidgetNews.itemDoubleClicked.connect(self.open_news)
            self.main_window = main_window
            self.main_window.pushButtonNewsBriefing.setEnabled(False)
            self.pushButtonClear.clicked.connect(self.clear)
        except Exception as e:
            logging.error(f'Error: {e}')
            
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
        if date_from == '' or date_to == '':
            QMessageBox.critical(self, 'Error', 'Please select both dates')
            return
        if self.dateTimeEditFrom.date() >= self.dateTimeEditTo.date():
            QMessageBox.critical(self, 'Error', 'From date cannot be greater than to date')
            return
        if self.lineEditKeywoardInput.text() == '':
            QMessageBox.critical(self, 'Error', 'Please provide a keyword')
            return
        date_from = change_date_format(date_from)
        date_to = change_date_format(date_to)
        if self.comboBox.currentText() is None or self.comboBox.currentText() == '':
            language_sel='en'
        else:
            language_sel=self.comboBox.currentText()
        if self.comboBox_2.currentText() is None or self.comboBox_2.currentText() == '':
            sort_by_sel='publishedAt'
        else:
            sort_by_sel=self.comboBox_2.currentText()
        try:
            articles_dict= fetch_and_store_articles(keyword=self.lineEditKeywoardInput.text(), from_date=date_from, to_date=date_to, language=language_sel, sort_by=sort_by_sel)
        except Exception as e:
            logging.error(f'Error: {e}')
            QMessageBox.critical(self, 'Error', 'There was a problem fetching the data. Please try again later')
            return
        # self.listWidgetNews.addItem(f"Total results: {articles_dict['totalResults']}")
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
        id = NewsFeature.get_id_by_description(description)
        update_single_news(id)  
        self.news= SingleArticleWindow(NewsFeature=NewsFeature(id))
        self.news.show()

    def set_min_date(self):
        current_date = QDateTime.currentDateTime()

        min_date = current_date.addDays(-29)
        self.dateTimeEditFrom.setMinimumDateTime(min_date)
        self.dateTimeEditTo.setMinimumDateTime(min_date)
    
    def set_max_date(self):
        current_date = QDateTime.currentDateTime()
        self.dateTimeEditTo.setDate(current_date.date())
        self.dateTimeEditTo.setMaximumDateTime(current_date)
    
    def closeEvent(self, event):
        if self.main_window is not None:
            self.main_window.w = None
            self.main_window.pushButtonNewsBriefing.setEnabled(True)
        delete_news_database()
    
    def clear(self):
        self.lineEditKeywoardInput.clear()
        self.listWidgetNews.clear()
        self.set_min_date()
        self.set_max_date()
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = NewsBriefingWindow()
    app.exec()