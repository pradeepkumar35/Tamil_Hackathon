# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacenkDuTt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################
# IMPORT CUSTOM BUTTONS FILE
from custom_buttons import *
########################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 331)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0))\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55ffff;\">Q</span><span style=\" font-size:18pt; font-style:italic; text-decoration: underline; color:#ffffff;\">BUTTON</span><span style=\" font-size:18pt;\"> CUS</span><span style=\" font-size:24pt; font-weight:600; color:#55ffff;\">T</span><span style=\" font-size:18pt;\">O</span><span style=\" font-size:18pt; font-weight:600;\">MIZ</span><span style=\" font-size:18pt;\">ATION</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "Loading", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", "Amazon", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", "PlayStore", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", "BitCoin", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", "Surf", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", "NodeJs", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", "Show Love", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", "Subscribe", None))
    # retranslateUi

