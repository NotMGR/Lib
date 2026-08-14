# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attempt_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(986, 112)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(50)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_attempt_label_1 = QLabel(Form)
        self.user_attempt_label_1.setObjectName(u"user_attempt_label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_attempt_label_1.sizePolicy().hasHeightForWidth())
        self.user_attempt_label_1.setSizePolicy(sizePolicy)
        self.user_attempt_label_1.setMinimumSize(QSize(0, 50))
        self.user_attempt_label_1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.user_attempt_label_1.setWordWrap(False)

        self.verticalLayout.addWidget(self.user_attempt_label_1)

        self.mock_toggle_button = QPushButton(Form)
        self.mock_toggle_button.setObjectName(u"mock_toggle_button")
        self.mock_toggle_button.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.mock_toggle_button.setFont(font)
        self.mock_toggle_button.setCheckable(False)

        self.verticalLayout.addWidget(self.mock_toggle_button)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.boss_attempt_pbutton_1 = QPushButton(Form)
        self.boss_attempt_pbutton_1.setObjectName(u"boss_attempt_pbutton_1")
        self.boss_attempt_pbutton_1.setMaximumSize(QSize(16777215, 90))
        self.boss_attempt_pbutton_1.setAutoFillBackground(True)
        self.boss_attempt_pbutton_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../../../Pictures/checkmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boss_attempt_pbutton_1.setIcon(icon)
        self.boss_attempt_pbutton_1.setCheckable(True)
        self.boss_attempt_pbutton_1.setFlat(False)

        self.horizontalLayout_11.addWidget(self.boss_attempt_pbutton_1)

        self.boss_attempt_pbutton_2 = QPushButton(Form)
        self.boss_attempt_pbutton_2.setObjectName(u"boss_attempt_pbutton_2")
        self.boss_attempt_pbutton_2.setMaximumSize(QSize(16777215, 90))
        self.boss_attempt_pbutton_2.setAutoFillBackground(False)
        self.boss_attempt_pbutton_2.setStyleSheet(u"")
        self.boss_attempt_pbutton_2.setIcon(icon)
        self.boss_attempt_pbutton_2.setCheckable(True)
        self.boss_attempt_pbutton_2.setFlat(False)

        self.horizontalLayout_11.addWidget(self.boss_attempt_pbutton_2)

        self.boss_attempt_pbutton_3 = QPushButton(Form)
        self.boss_attempt_pbutton_3.setObjectName(u"boss_attempt_pbutton_3")
        self.boss_attempt_pbutton_3.setMaximumSize(QSize(16777215, 90))
        self.boss_attempt_pbutton_3.setAutoFillBackground(False)
        self.boss_attempt_pbutton_3.setStyleSheet(u"")
        self.boss_attempt_pbutton_3.setIcon(icon)
        self.boss_attempt_pbutton_3.setCheckable(True)
        self.boss_attempt_pbutton_3.setFlat(False)

        self.horizontalLayout_11.addWidget(self.boss_attempt_pbutton_3)

        self.boss_attempt_pbutton_4 = QPushButton(Form)
        self.boss_attempt_pbutton_4.setObjectName(u"boss_attempt_pbutton_4")
        self.boss_attempt_pbutton_4.setMaximumSize(QSize(16777215, 90))
        self.boss_attempt_pbutton_4.setAutoFillBackground(False)
        self.boss_attempt_pbutton_4.setStyleSheet(u"")
        self.boss_attempt_pbutton_4.setIcon(icon)
        self.boss_attempt_pbutton_4.setCheckable(True)
        self.boss_attempt_pbutton_4.setFlat(False)

        self.horizontalLayout_11.addWidget(self.boss_attempt_pbutton_4)

        self.boss_attempt_pbutton_5 = QPushButton(Form)
        self.boss_attempt_pbutton_5.setObjectName(u"boss_attempt_pbutton_5")
        self.boss_attempt_pbutton_5.setMaximumSize(QSize(16777215, 90))
        self.boss_attempt_pbutton_5.setAutoFillBackground(False)
        self.boss_attempt_pbutton_5.setStyleSheet(u"")
        self.boss_attempt_pbutton_5.setIcon(icon)
        self.boss_attempt_pbutton_5.setCheckable(True)
        self.boss_attempt_pbutton_5.setFlat(False)

        self.horizontalLayout_11.addWidget(self.boss_attempt_pbutton_5)

        self.attempt_left_label_1 = QLabel(Form)
        self.attempt_left_label_1.setObjectName(u"attempt_left_label_1")

        self.horizontalLayout_11.addWidget(self.attempt_left_label_1)


        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.user_attempt_label_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.mock_toggle_button.setText(QCoreApplication.translate("Form", u"Mock Toggle", None))
        self.mock_toggle_button.setProperty(u"mock_toggle_button", "")
        self.boss_attempt_pbutton_1.setText("")
        self.boss_attempt_pbutton_2.setText("")
        self.boss_attempt_pbutton_3.setText("")
        self.boss_attempt_pbutton_4.setText("")
        self.boss_attempt_pbutton_5.setText("")
        self.attempt_left_label_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">3</span></p></body></html>", None))
    # retranslateUi

