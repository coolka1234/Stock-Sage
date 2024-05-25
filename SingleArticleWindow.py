from SingleArticle import Ui_MainMenuWindow
from PyQt6.QtWidgets import QMainWindow
from NewsFeature import NewsFeature
class SingleArticleWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self, NewsFeature: NewsFeature):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.labelId.setText(str(NewsFeature.id))
        self.labelTitle.setText(NewsFeature.title)
        self.labelUrl.setText(NewsFeature.url)
        self.labelContent.setText(NewsFeature.content)
        self.labelAuthor.setText(NewsFeature.author)
