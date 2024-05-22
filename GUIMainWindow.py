from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
class MainWindow():
    def __init__(self):
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("Main Window")
        self.main_window.show()
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Dialog")
