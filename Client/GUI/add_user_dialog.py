# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_user_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(274, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(274, 130))
        Dialog.setMaximumSize(QSize(274, 130))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_user_label = QLabel(Dialog)
        self.add_user_label.setObjectName(u"add_user_label")

        self.horizontalLayout.addWidget(self.add_user_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.add_user_line_edit = QLineEdit(Dialog)
        self.add_user_line_edit.setObjectName(u"add_user_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_user_line_edit.sizePolicy().hasHeightForWidth())
        self.add_user_line_edit.setSizePolicy(sizePolicy1)
        self.add_user_line_edit.setMinimumSize(QSize(170, 20))
        self.add_user_line_edit.setMaximumSize(QSize(250, 24))

        self.horizontalLayout.addWidget(self.add_user_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.active_user_label = QLabel(Dialog)
        self.active_user_label.setObjectName(u"active_user_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.active_user_label.sizePolicy().hasHeightForWidth())
        self.active_user_label.setSizePolicy(sizePolicy2)
        self.active_user_label.setMaximumSize(QSize(300, 100))

        self.horizontalLayout_2.addWidget(self.active_user_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.active_radio_button_yes = QRadioButton(Dialog)
        self.active_radio_button_yes.setObjectName(u"active_radio_button_yes")

        self.horizontalLayout_2.addWidget(self.active_radio_button_yes, 0, Qt.AlignmentFlag.AlignBottom)

        self.active_radio_button_no = QRadioButton(Dialog)
        self.active_radio_button_no.setObjectName(u"active_radio_button_no")

        self.horizontalLayout_2.addWidget(self.active_radio_button_no, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Member", None))
        self.add_user_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Name:</span></p></body></html>", None))
        self.active_user_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Active:</span></p></body></html>", None))
        self.active_radio_button_yes.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.active_radio_button_no.setText(QCoreApplication.translate("Dialog", u"No", None))
    # retranslateUi

