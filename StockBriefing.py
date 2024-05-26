# Form implementation generated from reading ui file 'StockBriefing.ui'
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
        self.labelTitle.setGeometry(QtCore.QRect(30, 30, 211, 71))
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
        self.layoutWidget.setGeometry(QtCore.QRect(750, 120, 301, 551))
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
        self.labelCompanyName.setObjectName("labelCompanyName")
        self.verticalLayout_4.addWidget(self.labelCompanyName)
        self.lineEditSymbolnput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEditSymbolnput.setObjectName("lineEditSymbolnput")
        self.verticalLayout_4.addWidget(self.lineEditSymbolnput)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelTitlePeriod = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitlePeriod.setFont(font)
        self.labelTitlePeriod.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelTitlePeriod.setScaledContents(False)
        self.labelTitlePeriod.setObjectName("labelTitlePeriod")
        self.verticalLayout_3.addWidget(self.labelTitlePeriod)
        self.comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTitleLanguage_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.labelTitleLanguage_2.sizePolicy().hasHeightForWidth())
        self.labelTitleLanguage_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitleLanguage_2.setFont(font)
        self.labelTitleLanguage_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelTitleLanguage_2.setScaledContents(False)
        self.labelTitleLanguage_2.setObjectName("labelTitleLanguage_2")
        self.verticalLayout_2.addWidget(self.labelTitleLanguage_2)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
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
        self.labelSypckGraph = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelSypckGraph.setGeometry(QtCore.QRect(50, 120, 657, 545))
        self.labelSypckGraph.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSypckGraph.setObjectName("labelSypckGraph")
        MainMenuWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainMenuWindow)
        self.statusbar.setObjectName("statusbar")
        MainMenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "News Briefing - Stock Sage"))
        self.labelTitle.setText(_translate("MainMenuWindow", "Stock Briefing"))
        self.labelCompanyName.setText(_translate("MainMenuWindow", "Company Symbol:"))
        self.lineEditSymbolnput.setPlaceholderText(_translate("MainMenuWindow", "Input symbol..."))
        self.labelTitlePeriod.setText(_translate("MainMenuWindow", "Period:"))
        self.comboBox.setPlaceholderText(_translate("MainMenuWindow", "Select period..."))
        self.labelTitleLanguage_2.setText(_translate("MainMenuWindow", "Interval:"))
        self.comboBox_2.setPlaceholderText(_translate("MainMenuWindow", "Select interval..."))
        self.pushButtonExecute.setToolTip(_translate("MainMenuWindow", "Search with given criteria"))
        self.pushButtonExecute.setText(_translate("MainMenuWindow", "Search"))
        self.pushButtonClear.setToolTip(_translate("MainMenuWindow", "Clear search results"))
        self.pushButtonClear.setText(_translate("MainMenuWindow", "Clear"))
        self.labelSypckGraph.setText(_translate("MainMenuWindow", "Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec())
