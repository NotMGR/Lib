# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_edit_user_dialog(object):
    def setupUi(self, edit_user_dialog):
        if not edit_user_dialog.objectName():
            edit_user_dialog.setObjectName(u"edit_user_dialog")
        edit_user_dialog.resize(303, 174)
        edit_user_dialog.setMinimumSize(QSize(303, 174))
        edit_user_dialog.setMaximumSize(QSize(303, 174))
        self.gridLayout = QGridLayout(edit_user_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_user_member_label = QLabel(edit_user_dialog)
        self.edit_user_member_label.setObjectName(u"edit_user_member_label")

        self.horizontalLayout.addWidget(self.edit_user_member_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.edit_user_cbox = QComboBox(edit_user_dialog)
        self.edit_user_cbox.setObjectName(u"edit_user_cbox")
        self.edit_user_cbox.setMinimumSize(QSize(170, 0))
        self.edit_user_cbox.setEditable(True)

        self.horizontalLayout.addWidget(self.edit_user_cbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edit_user_name_label = QLabel(edit_user_dialog)
        self.edit_user_name_label.setObjectName(u"edit_user_name_label")

        self.horizontalLayout_2.addWidget(self.edit_user_name_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.edit_user_line_edit = QLineEdit(edit_user_dialog)
        self.edit_user_line_edit.setObjectName(u"edit_user_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_user_line_edit.sizePolicy().hasHeightForWidth())
        self.edit_user_line_edit.setSizePolicy(sizePolicy)
        self.edit_user_line_edit.setMinimumSize(QSize(170, 20))
        self.edit_user_line_edit.setMaximumSize(QSize(250, 24))

        self.horizontalLayout_2.addWidget(self.edit_user_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_user_active_label = QLabel(edit_user_dialog)
        self.edit_user_active_label.setObjectName(u"edit_user_active_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_user_active_label.sizePolicy().hasHeightForWidth())
        self.edit_user_active_label.setSizePolicy(sizePolicy1)
        self.edit_user_active_label.setMaximumSize(QSize(300, 100))

        self.horizontalLayout_3.addWidget(self.edit_user_active_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.edit_user_active_radio_button_yes = QRadioButton(edit_user_dialog)
        self.edit_user_active_radio_button_yes.setObjectName(u"edit_user_active_radio_button_yes")

        self.horizontalLayout_3.addWidget(self.edit_user_active_radio_button_yes, 0, Qt.AlignmentFlag.AlignBottom)

        self.edit_user_active_radio_button_no = QRadioButton(edit_user_dialog)
        self.edit_user_active_radio_button_no.setObjectName(u"edit_user_active_radio_button_no")

        self.horizontalLayout_3.addWidget(self.edit_user_active_radio_button_no, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.edit_user_button_box = QDialogButtonBox(edit_user_dialog)
        self.edit_user_button_box.setObjectName(u"edit_user_button_box")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.edit_user_button_box.setFont(font)
        self.edit_user_button_box.setOrientation(Qt.Orientation.Horizontal)
        self.edit_user_button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.edit_user_button_box.setCenterButtons(True)

        self.horizontalLayout_4.addWidget(self.edit_user_button_box)

        self.delete_user_button = QPushButton(edit_user_dialog)
        self.delete_user_button.setObjectName(u"delete_user_button")
        self.delete_user_button.setFont(font)

        self.horizontalLayout_4.addWidget(self.delete_user_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(edit_user_dialog)
        self.edit_user_button_box.accepted.connect(edit_user_dialog.accept)
        self.edit_user_button_box.rejected.connect(edit_user_dialog.reject)

        QMetaObject.connectSlotsByName(edit_user_dialog)
    # setupUi

    def retranslateUi(self, edit_user_dialog):
        edit_user_dialog.setWindowTitle(QCoreApplication.translate("edit_user_dialog", u"Edit Member", None))
        self.edit_user_member_label.setText(QCoreApplication.translate("edit_user_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Member</span></p></body></html>", None))
        self.edit_user_name_label.setText(QCoreApplication.translate("edit_user_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Name:</span></p></body></html>", None))
        self.edit_user_active_label.setText(QCoreApplication.translate("edit_user_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Active:</span></p></body></html>", None))
        self.edit_user_active_radio_button_yes.setText(QCoreApplication.translate("edit_user_dialog", u"Yes", None))
        self.edit_user_active_radio_button_no.setText(QCoreApplication.translate("edit_user_dialog", u"No", None))
        self.delete_user_button.setText(QCoreApplication.translate("edit_user_dialog", u"Delete User", None))
    # retranslateUi

