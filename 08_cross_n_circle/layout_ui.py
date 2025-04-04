# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(365, 493)
        MainWindow.setStyleSheet(u"background: #4d4d4d;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.inputX = QLineEdit(self.centralwidget)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setEnabled(True)
        self.inputX.setStyleSheet(u"border: 1px solid #fff;\n"
"padding: 4px;\n"
"color: #fff")

        self.verticalLayout.addWidget(self.inputX)

        self.inputO = QLineEdit(self.centralwidget)
        self.inputO.setObjectName(u"inputO")
        self.inputO.setStyleSheet(u"border: 1px solid #fff;\n"
"padding: 4px;\n"
"color: #fff")

        self.verticalLayout.addWidget(self.inputO)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn3x2 = QPushButton(self.centralwidget)
        self.btn3x2.setObjectName(u"btn3x2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn3x2.sizePolicy().hasHeightForWidth())
        self.btn3x2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        self.btn3x2.setFont(font1)
        self.btn3x2.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn3x2, 1, 2, 1, 1)

        self.btn2x1 = QPushButton(self.centralwidget)
        self.btn2x1.setObjectName(u"btn2x1")
        sizePolicy1.setHeightForWidth(self.btn2x1.sizePolicy().hasHeightForWidth())
        self.btn2x1.setSizePolicy(sizePolicy1)
        self.btn2x1.setFont(font1)
        self.btn2x1.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn2x1, 0, 1, 1, 1)

        self.btn2x2 = QPushButton(self.centralwidget)
        self.btn2x2.setObjectName(u"btn2x2")
        sizePolicy1.setHeightForWidth(self.btn2x2.sizePolicy().hasHeightForWidth())
        self.btn2x2.setSizePolicy(sizePolicy1)
        self.btn2x2.setFont(font1)
        self.btn2x2.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn2x2, 1, 1, 1, 1)

        self.btn3x1 = QPushButton(self.centralwidget)
        self.btn3x1.setObjectName(u"btn3x1")
        sizePolicy1.setHeightForWidth(self.btn3x1.sizePolicy().hasHeightForWidth())
        self.btn3x1.setSizePolicy(sizePolicy1)
        self.btn3x1.setFont(font1)
        self.btn3x1.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn3x1, 0, 2, 1, 1)

        self.btn1x2 = QPushButton(self.centralwidget)
        self.btn1x2.setObjectName(u"btn1x2")
        sizePolicy1.setHeightForWidth(self.btn1x2.sizePolicy().hasHeightForWidth())
        self.btn1x2.setSizePolicy(sizePolicy1)
        self.btn1x2.setFont(font1)
        self.btn1x2.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn1x2, 1, 0, 1, 1)

        self.btn2x3 = QPushButton(self.centralwidget)
        self.btn2x3.setObjectName(u"btn2x3")
        sizePolicy1.setHeightForWidth(self.btn2x3.sizePolicy().hasHeightForWidth())
        self.btn2x3.setSizePolicy(sizePolicy1)
        self.btn2x3.setFont(font1)
        self.btn2x3.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn2x3, 2, 1, 1, 1)

        self.btn1x3 = QPushButton(self.centralwidget)
        self.btn1x3.setObjectName(u"btn1x3")
        sizePolicy1.setHeightForWidth(self.btn1x3.sizePolicy().hasHeightForWidth())
        self.btn1x3.setSizePolicy(sizePolicy1)
        self.btn1x3.setFont(font1)
        self.btn1x3.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn1x3, 2, 0, 1, 1)

        self.btn1x1 = QPushButton(self.centralwidget)
        self.btn1x1.setObjectName(u"btn1x1")
        sizePolicy1.setHeightForWidth(self.btn1x1.sizePolicy().hasHeightForWidth())
        self.btn1x1.setSizePolicy(sizePolicy1)
        self.btn1x1.setFont(font1)
        self.btn1x1.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")
        self.btn1x1.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn1x1, 0, 0, 1, 1)

        self.btn3x3 = QPushButton(self.centralwidget)
        self.btn3x3.setObjectName(u"btn3x3")
        sizePolicy1.setHeightForWidth(self.btn3x3.sizePolicy().hasHeightForWidth())
        self.btn3x3.setSizePolicy(sizePolicy1)
        self.btn3x3.setFont(font1)
        self.btn3x3.setStyleSheet(u"background: #474747;\n"
"border: 2px solid #262626;")

        self.gridLayout.addWidget(self.btn3x3, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btnNewGame = QPushButton(self.centralwidget)
        self.btnNewGame.setObjectName(u"btnNewGame")
        self.btnNewGame.setStyleSheet(u"background: #2cbb53; padding: 6px")

        self.verticalLayout.addWidget(self.btnNewGame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tic Tac Toe", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tic Tac Toe", None))
        self.inputX.setText(QCoreApplication.translate("MainWindow", u"Player X", None))
        self.inputO.setText(QCoreApplication.translate("MainWindow", u"Player O", None))
        self.btn3x2.setText("")
        self.btn2x1.setText("")
        self.btn2x2.setText("")
        self.btn3x1.setText("")
        self.btn1x2.setText("")
        self.btn2x3.setText("")
        self.btn1x3.setText("")
        self.btn1x1.setText("")
        self.btn3x3.setText("")
        self.btnNewGame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
    # retranslateUi

