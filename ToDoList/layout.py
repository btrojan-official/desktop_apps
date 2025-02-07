# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TODO.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(690, 420)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 691, 421))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"padding: 5px;")
        self.lineEdit.setCursorPosition(0)

        self.verticalLayout.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"padding: 5px")

        self.verticalLayout.addWidget(self.comboBox)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(self.horizontalLayoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setStyleSheet(u";")

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"background: rgb(66, 123, 255); padding: 5px")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background: rgb(66, 123, 255); padding: 5px")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgb(66, 123, 255); padding: 5px")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background: rgb(66, 123, 255); padding: 5px")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background: rgb(66, 123, 255); padding: 5px")

        self.horizontalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.listView = QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Write new task here", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"To Do", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Done", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Select Date and Time:", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Add new", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Remove selected", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Update status", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Load", None))
    # retranslateUi


# if __name__ == '__main__':
#     app = QApplication([])
#     window = Ui_Dialog()
#     window.show()
#     app.exec()