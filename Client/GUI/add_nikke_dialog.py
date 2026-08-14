# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_nikke_dialog.ui'
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
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Add_Nikke_Dialog(object):
    def setupUi(self, Add_Nikke_Dialog):
        if not Add_Nikke_Dialog.objectName():
            Add_Nikke_Dialog.setObjectName(u"Add_Nikke_Dialog")
        Add_Nikke_Dialog.resize(289, 249)
        self.gridLayout = QGridLayout(Add_Nikke_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nikke_name_label = QLabel(Add_Nikke_Dialog)
        self.nikke_name_label.setObjectName(u"nikke_name_label")
        self.nikke_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.nikke_name_label)

        self.nikke_name_line_edit = QLineEdit(Add_Nikke_Dialog)
        self.nikke_name_line_edit.setObjectName(u"nikke_name_line_edit")
        self.nikke_name_line_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.nikke_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nikke_element_label = QLabel(Add_Nikke_Dialog)
        self.nikke_element_label.setObjectName(u"nikke_element_label")
        self.nikke_element_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.nikke_element_label)

        self.nikke_element_box = QComboBox(Add_Nikke_Dialog)
        self.nikke_element_box.setObjectName(u"nikke_element_box")
        self.nikke_element_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.nikke_element_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nikke_burst_label = QLabel(Add_Nikke_Dialog)
        self.nikke_burst_label.setObjectName(u"nikke_burst_label")
        self.nikke_burst_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.nikke_burst_label)

        self.nikke_burst_box = QComboBox(Add_Nikke_Dialog)
        self.nikke_burst_box.setObjectName(u"nikke_burst_box")
        self.nikke_burst_box.setEditable(False)
        self.nikke_burst_box.setFrame(True)

        self.horizontalLayout_3.addWidget(self.nikke_burst_box)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nikke_manuf_label = QLabel(Add_Nikke_Dialog)
        self.nikke_manuf_label.setObjectName(u"nikke_manuf_label")
        self.nikke_manuf_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.nikke_manuf_label)

        self.nikke_manuf_box = QComboBox(Add_Nikke_Dialog)
        self.nikke_manuf_box.setObjectName(u"nikke_manuf_box")
        self.nikke_manuf_box.setIconSize(QSize(16, 16))
        self.nikke_manuf_box.setDuplicatesEnabled(False)

        self.horizontalLayout_4.addWidget(self.nikke_manuf_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nikke_role_label = QLabel(Add_Nikke_Dialog)
        self.nikke_role_label.setObjectName(u"nikke_role_label")
        self.nikke_role_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.nikke_role_label.setFrameShape(QFrame.Shape.NoFrame)
        self.nikke_role_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_5.addWidget(self.nikke_role_label)

        self.nikke_role_box = QComboBox(Add_Nikke_Dialog)
        self.nikke_role_box.setObjectName(u"nikke_role_box")

        self.horizontalLayout_5.addWidget(self.nikke_role_box)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nikke_image_label = QLabel(Add_Nikke_Dialog)
        self.nikke_image_label.setObjectName(u"nikke_image_label")

        self.horizontalLayout_6.addWidget(self.nikke_image_label)

        self.nikke_select_image_button = QPushButton(Add_Nikke_Dialog)
        self.nikke_select_image_button.setObjectName(u"nikke_select_image_button")

        self.horizontalLayout_6.addWidget(self.nikke_select_image_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(Add_Nikke_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Add_Nikke_Dialog)

        QMetaObject.connectSlotsByName(Add_Nikke_Dialog)
    # setupUi

    def retranslateUi(self, Add_Nikke_Dialog):
        Add_Nikke_Dialog.setWindowTitle(QCoreApplication.translate("Add_Nikke_Dialog", u"Dialog", None))
        self.nikke_name_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Nikke Name: </span></p></body></html>", None))
        self.nikke_element_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Element:</span></p></body></html>", None))
        self.nikke_burst_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Burst:</span></p></body></html>", None))
        self.nikke_manuf_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Manufacturer:</span></p></body></html>", None))
        self.nikke_role_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Role:</span></p></body></html>", None))
        self.nikke_image_label.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Image:</span></p></body></html>", None))
        self.nikke_select_image_button.setText(QCoreApplication.translate("Add_Nikke_Dialog", u"Open...", None))
    # retranslateUi

