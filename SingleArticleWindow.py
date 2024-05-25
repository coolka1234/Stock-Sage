from SingleArticle import Ui_MainMenuWindow
from PyQt6.QtWidgets import QMainWindow
from NewsFeature import NewsFeature
class SingleArticleWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self, NewsFeature: NewsFeature):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.textEditId.setText(str(NewsFeature.id))
        self.textEditTitle.setText(NewsFeature.title)
        self.textEditUrl.setText(NewsFeature.url)
        self.textEdit.setText(NewsFeature.content)
