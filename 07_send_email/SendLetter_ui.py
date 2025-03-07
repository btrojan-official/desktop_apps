# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SendLetter.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(442, 398)
        Dialog.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Body = QVBoxLayout()
        self.Body.setObjectName(u"Body")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.checkPriceButton = QPushButton(Dialog)
        self.checkPriceButton.setObjectName(u"checkPriceButton")
        self.checkPriceButton.setStyleSheet(u"background: rgb(0, 70, 200);")

        self.gridLayout.addWidget(self.checkPriceButton, 1, 0, 1, 1)

        self.deliveryTypeGroupBox = QGroupBox(Dialog)
        self.deliveryTypeGroupBox.setObjectName(u"deliveryTypeGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.deliveryTypeGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.postcartRadio = QRadioButton(self.deliveryTypeGroupBox)
        self.postcartRadio.setObjectName(u"postcartRadio")
        self.postcartRadio.setChecked(True)

        self.verticalLayout.addWidget(self.postcartRadio)

        self.letterRadio = QRadioButton(self.deliveryTypeGroupBox)
        self.letterRadio.setObjectName(u"letterRadio")

        self.verticalLayout.addWidget(self.letterRadio)

        self.packageRadio = QRadioButton(self.deliveryTypeGroupBox)
        self.packageRadio.setObjectName(u"packageRadio")

        self.verticalLayout.addWidget(self.packageRadio)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.deliveryTypeGroupBox, 0, 0, 1, 1)

        self.imageLabel = QLabel(Dialog)
        self.imageLabel.setObjectName(u"imageLabel")

        self.gridLayout.addWidget(self.imageLabel, 2, 0, 1, 1)

        self.priceLabel = QLabel(Dialog)
        self.priceLabel.setObjectName(u"priceLabel")

        self.gridLayout.addWidget(self.priceLabel, 2, 1, 1, 1)

        self.adressDataGroupBox = QGroupBox(Dialog)
        self.adressDataGroupBox.setObjectName(u"adressDataGroupBox")
        self.adressDataGroupBox.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.adressDataGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.streetLabel = QLabel(self.adressDataGroupBox)
        self.streetLabel.setObjectName(u"streetLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.streetLabel)

        self.cityLabel = QLabel(self.adressDataGroupBox)
        self.cityLabel.setObjectName(u"cityLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cityLabel)

        self.postNumberLabel = QLabel(self.adressDataGroupBox)
        self.postNumberLabel.setObjectName(u"postNumberLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.postNumberLabel)

        self.streetLineEdit = QLineEdit(self.adressDataGroupBox)
        self.streetLineEdit.setObjectName(u"streetLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.streetLineEdit)

        self.postNumberLineEdit = QLineEdit(self.adressDataGroupBox)
        self.postNumberLineEdit.setObjectName(u"postNumberLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.postNumberLineEdit)

        self.cityLineEdit = QLineEdit(self.adressDataGroupBox)
        self.cityLineEdit.setObjectName(u"cityLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cityLineEdit)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.gridLayout.addWidget(self.adressDataGroupBox, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)

        self.horizontalLayout.addLayout(self.gridLayout)


        self.Body.addLayout(self.horizontalLayout)

        self.submitButton = QPushButton(Dialog)
        self.submitButton.setObjectName(u"submitButton")

        self.Body.addWidget(self.submitButton)


        self.verticalLayout_2.addLayout(self.Body)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Nadaj przesy\u0142k\u0119, Bartosz", None))
        self.checkPriceButton.setText(QCoreApplication.translate("Dialog", u"Sprawd\u017a cen\u0119", None))
        self.deliveryTypeGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Rodzaj przesy\u0142ki", None))
        self.postcartRadio.setText(QCoreApplication.translate("Dialog", u"Poczt\u00f3wka", None))
        self.letterRadio.setText(QCoreApplication.translate("Dialog", u"List", None))
        self.packageRadio.setText(QCoreApplication.translate("Dialog", u"Paczka", None))
        self.imageLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.priceLabel.setText(QCoreApplication.translate("Dialog", u"Cena: ?", None))
        self.adressDataGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Dane adresowe", None))
        self.streetLabel.setText(QCoreApplication.translate("Dialog", u"Ulica z numerem", None))
        self.cityLabel.setText(QCoreApplication.translate("Dialog", u"Miasto", None))
        self.postNumberLabel.setText(QCoreApplication.translate("Dialog", u"Kod pocztowy", None))
        self.submitButton.setText(QCoreApplication.translate("Dialog", u"Zatwierd\u017a", None))
    # retranslateUi

