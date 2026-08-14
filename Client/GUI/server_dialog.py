# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_dialog.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_server_dialog(object):
    def setupUi(self, server_dialog):
        if not server_dialog.objectName():
            server_dialog.setObjectName(u"server_dialog")
        server_dialog.resize(346, 141)
        server_dialog.setMinimumSize(QSize(346, 141))
        server_dialog.setMaximumSize(QSize(346, 141))
        self.gridLayout = QGridLayout(server_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.server_address_label = QLabel(server_dialog)
        self.server_address_label.setObjectName(u"server_address_label")

        self.horizontalLayout.addWidget(self.server_address_label)

        self.server_url_line_edit = QLineEdit(server_dialog)
        self.server_url_line_edit.setObjectName(u"server_url_line_edit")

        self.horizontalLayout.addWidget(self.server_url_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.test_connection_button = QPushButton(server_dialog)
        self.test_connection_button.setObjectName(u"test_connection_button")
        self.test_connection_button.setMinimumSize(QSize(141, 31))

        self.horizontalLayout_2.addWidget(self.test_connection_button)

        self.connection_status_label = QLabel(server_dialog)
        self.connection_status_label.setObjectName(u"connection_status_label")
        self.connection_status_label.setMinimumSize(QSize(161, 31))

        self.horizontalLayout_2.addWidget(self.connection_status_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.ok_cancel_button = QDialogButtonBox(server_dialog)
        self.ok_cancel_button.setObjectName(u"ok_cancel_button")
        self.ok_cancel_button.setOrientation(Qt.Orientation.Horizontal)
        self.ok_cancel_button.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.ok_cancel_button.setCenterButtons(True)

        self.verticalLayout.addWidget(self.ok_cancel_button)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(server_dialog)
        self.ok_cancel_button.accepted.connect(server_dialog.accept)
        self.ok_cancel_button.rejected.connect(server_dialog.reject)

        QMetaObject.connectSlotsByName(server_dialog)
    # setupUi

    def retranslateUi(self, server_dialog):
        server_dialog.setWindowTitle(QCoreApplication.translate("server_dialog", u"Select Server", None))
        self.server_address_label.setText(QCoreApplication.translate("server_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Server Address</span></p></body></html>", None))
        self.test_connection_button.setText(QCoreApplication.translate("server_dialog", u"Test Connection", None))
        self.connection_status_label.setText(QCoreApplication.translate("server_dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

