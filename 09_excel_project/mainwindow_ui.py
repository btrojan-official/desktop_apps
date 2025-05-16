# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sheet_combobox = QComboBox(self.centralwidget)
        self.sheet_combobox.setObjectName(u"sheet_combobox")

        self.horizontalLayout.addWidget(self.sheet_combobox)

        self.filter_button = QPushButton(self.centralwidget)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setMinimumSize(QSize(100, 0))
        self.filter_button.setStyleSheet(u"background-color: #217346;")

        self.horizontalLayout.addWidget(self.filter_button)

        self.chart_button = QPushButton(self.centralwidget)
        self.chart_button.setObjectName(u"chart_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_button.sizePolicy().hasHeightForWidth())
        self.chart_button.setSizePolicy(sizePolicy)
        self.chart_button.setMinimumSize(QSize(100, 0))
        self.chart_button.setAutoFillBackground(False)
        self.chart_button.setStyleSheet(u"background-color: #217346;")

        self.horizontalLayout.addWidget(self.chart_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.undo_button = QPushButton(self.centralwidget)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setToolTipDuration(1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditUndo))
        self.undo_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.undo_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.sheet_tableview = QTableView(self.centralwidget)
        self.sheet_tableview.setObjectName(u"sheet_tableview")

        self.verticalLayout.addWidget(self.sheet_tableview)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")

        self.horizontalLayout_2.addWidget(self.path_label)

        self.records_label = QLabel(self.centralwidget)
        self.records_label.setObjectName(u"records_label")
        self.records_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.records_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 33))
        self.menu_open = QMenu(self.menubar)
        self.menu_open.setObjectName(u"menu_open")
        self.menuSave_as = QMenu(self.menubar)
        self.menuSave_as.setObjectName(u"menuSave_as")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_open.menuAction())
        self.menubar.addAction(self.menuSave_as.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menuSave_as.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Desktop Excel Editor", None))
        self.filter_button.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.chart_button.setText(QCoreApplication.translate("MainWindow", u"Generate Chart", None))
        self.undo_button.setText("")
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"Path: C://ProgramFiles/danger_virus.bat", None))
        self.records_label.setText(QCoreApplication.translate("MainWindow", u"Records: 1901", None))
        self.menu_open.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuSave_as.setTitle(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

