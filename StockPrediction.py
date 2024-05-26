# Form implementation generated from reading ui file 'StockPrediction.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(1060, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenuWindow.sizePolicy().hasHeightForWidth())
        MainMenuWindow.setSizePolicy(sizePolicy)
        MainMenuWindow.setMinimumSize(QtCore.QSize(1060, 700))
        MainMenuWindow.setMaximumSize(QtCore.QSize(1060, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../stock_sage_icon_v2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainMenuWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(50, 30, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelTitle.setScaledContents(False)
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(750, 120, 370, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelCompanyName = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(22)
        font.setBold(True)
        self.labelCompanyName.setFont(font)
        self.labelCompanyName.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelCompanyName.setScaledContents(False)
        self.labelCompanyName.setWordWrap(True)
        self.labelCompanyName.setObjectName("labelCompanyName")
        self.verticalLayout_4.addWidget(self.labelCompanyName)
        self.lineEditSymbolnput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEditSymbolnput.setObjectName("lineEditSymbolnput")
        self.verticalLayout_4.addWidget(self.lineEditSymbolnput)
        self.labelCompanyName_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(22)
        font.setBold(True)
        self.labelCompanyName_2.setFont(font)
        self.labelCompanyName_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelCompanyName_2.setScaledContents(False)
        self.labelCompanyName_2.setWordWrap(True)
        self.labelCompanyName_2.setObjectName("labelCompanyName_2")
        self.verticalLayout_4.addWidget(self.labelCompanyName_2)
        self.lineEditNameInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEditNameInput.setObjectName("lineEditNameInput")
        self.verticalLayout_4.addWidget(self.lineEditNameInput)
        self.progressBar = QtWidgets.QProgressBar(parent=self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(750, 60, 191, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonExecute = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButtonExecute.setObjectName("pushButtonExecute")
        self.horizontalLayout.addWidget(self.pushButtonExecute)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.labelRaport = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelRaport.setGeometry(QtCore.QRect(50, 120, 657, 545))
        self.labelRaport.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelRaport.setObjectName("labelRaport")
        MainMenuWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainMenuWindow)
        self.statusbar.setObjectName("statusbar")
        MainMenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "News Briefing - Stock Sage"))
        self.labelTitle.setText(_translate("MainMenuWindow", "Stock Prediciton"))
        self.labelCompanyName.setText(_translate("MainMenuWindow", "Company Symbol:"))
        self.lineEditSymbolnput.setPlaceholderText(_translate("MainMenuWindow", "Input symbol..."))
        self.labelCompanyName_2.setText(_translate("MainMenuWindow", "Company Name:"))
        self.lineEditNameInput.setPlaceholderText(_translate("MainMenuWindow", "Input name..."))
        self.pushButtonExecute.setToolTip(_translate("MainMenuWindow", "Search with given criteria"))
        self.pushButtonExecute.setText(_translate("MainMenuWindow", "Display"))
        self.pushButtonClear.setToolTip(_translate("MainMenuWindow", "Clear search results"))
        self.pushButtonClear.setText(_translate("MainMenuWindow", "Clear"))
        self.labelRaport.setText(_translate("MainMenuWindow", "Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec())
