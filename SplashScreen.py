import sys
import time
from PyQt6.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from utility_functions import resource_path

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap(resource_path("stock_sage_icon_v2.png"))
        super().__init__(pixmap)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.showMessage("Loading...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, Qt.GlobalColor.white)

def main():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    from MainMenuWindow import MainMenuWindow
    main_window = MainMenuWindow()
    main_window.show()
    splash.finish(main_window)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
