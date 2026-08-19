# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_union_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Union_Dialog(object):
    def setupUi(self, Union_Dialog):
        if not Union_Dialog.objectName():
            Union_Dialog.setObjectName(u"Union_Dialog")
        Union_Dialog.resize(332, 150)
        Union_Dialog.setMinimumSize(QSize(332, 150))
        Union_Dialog.setMaximumSize(QSize(332, 150))
        self.gridLayout = QGridLayout(Union_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.union_label = QLabel(Union_Dialog)
        self.union_label.setObjectName(u"union_label")

        self.horizontalLayout_5.addWidget(self.union_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.edit_union_cbox = QComboBox(Union_Dialog)
        self.edit_union_cbox.setObjectName(u"edit_union_cbox")
        self.edit_union_cbox.setMinimumSize(QSize(170, 0))
        self.edit_union_cbox.setEditable(True)

        self.horizontalLayout_5.addWidget(self.edit_union_cbox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.union_name_label = QLabel(Union_Dialog)
        self.union_name_label.setObjectName(u"union_name_label")

        self.horizontalLayout.addWidget(self.union_name_label)

        self.union_name_line_edit = QLineEdit(Union_Dialog)
        self.union_name_line_edit.setObjectName(u"union_name_line_edit")

        self.horizontalLayout.addWidget(self.union_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ok_cancel_button_box = QDialogButtonBox(Union_Dialog)
        self.ok_cancel_button_box.setObjectName(u"ok_cancel_button_box")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ok_cancel_button_box.setFont(font)
        self.ok_cancel_button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.ok_cancel_button_box.setCenterButtons(True)

        self.horizontalLayout_2.addWidget(self.ok_cancel_button_box)

        self.delete_union_button = QPushButton(Union_Dialog)
        self.delete_union_button.setObjectName(u"delete_union_button")
        self.delete_union_button.setFont(font)

        self.horizontalLayout_2.addWidget(self.delete_union_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Union_Dialog)

        QMetaObject.connectSlotsByName(Union_Dialog)
    # setupUi

    def retranslateUi(self, Union_Dialog):
        Union_Dialog.setWindowTitle(QCoreApplication.translate("Union_Dialog", u"Dialog", None))
        self.union_label.setText(QCoreApplication.translate("Union_Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Union:</span></p></body></html>", None))
        self.union_name_label.setText(QCoreApplication.translate("Union_Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Union Name:</span></p></body></html>", None))
        self.delete_union_button.setText(QCoreApplication.translate("Union_Dialog", u"Delete Union", None))
    # retranslateUi

