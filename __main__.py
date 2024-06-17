from src.gui.MainMenuWindow import MainMenuWindow
from PyQt6.QtWidgets import QApplication
if __name__ == "__main__":
    app = QApplication([])
    window = MainMenuWindow()
    app.exec()