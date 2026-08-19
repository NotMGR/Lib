# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_raid_dialog.ui'
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
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_edit_raid_dialog(object):
    def setupUi(self, edit_raid_dialog):
        if not edit_raid_dialog.objectName():
            edit_raid_dialog.setObjectName(u"edit_raid_dialog")
        edit_raid_dialog.resize(449, 511)
        edit_raid_dialog.setMinimumSize(QSize(449, 511))
        edit_raid_dialog.setMaximumSize(QSize(449, 511))
        self.gridLayout = QGridLayout(edit_raid_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(edit_raid_dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_user_raid_cbox = QComboBox(edit_raid_dialog)
        self.edit_user_raid_cbox.setObjectName(u"edit_user_raid_cbox")
        self.edit_user_raid_cbox.setEditable(True)

        self.horizontalLayout.addWidget(self.edit_user_raid_cbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.union_label = QLabel(edit_raid_dialog)
        self.union_label.setObjectName(u"union_label")
        self.union_label.setMinimumSize(QSize(100, 40))
        self.union_label.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_10.addWidget(self.union_label)

        self.edit_union_cbox = QComboBox(edit_raid_dialog)
        self.edit_union_cbox.setObjectName(u"edit_union_cbox")
        self.edit_union_cbox.setMinimumSize(QSize(0, 0))
        self.edit_union_cbox.setMaximumSize(QSize(250, 16777215))
        self.edit_union_cbox.setEditable(True)

        self.horizontalLayout_10.addWidget(self.edit_union_cbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.raid_name_label_2 = QLabel(edit_raid_dialog)
        self.raid_name_label_2.setObjectName(u"raid_name_label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raid_name_label_2.sizePolicy().hasHeightForWidth())
        self.raid_name_label_2.setSizePolicy(sizePolicy)
        self.raid_name_label_2.setMinimumSize(QSize(150, 40))
        self.raid_name_label_2.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_2.addWidget(self.raid_name_label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.edit_raid_name_line_edit = QLineEdit(edit_raid_dialog)
        self.edit_raid_name_line_edit.setObjectName(u"edit_raid_name_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_raid_name_line_edit.sizePolicy().hasHeightForWidth())
        self.edit_raid_name_line_edit.setSizePolicy(sizePolicy1)
        self.edit_raid_name_line_edit.setMinimumSize(QSize(171, 24))
        self.edit_raid_name_line_edit.setMaximumSize(QSize(170, 24))

        self.horizontalLayout_2.addWidget(self.edit_raid_name_line_edit, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(edit_raid_dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.edit_user_boss_name_label = QLabel(edit_raid_dialog)
        self.edit_user_boss_name_label.setObjectName(u"edit_user_boss_name_label")

        self.horizontalLayout_8.addWidget(self.edit_user_boss_name_label)

        self.label_3 = QLabel(edit_raid_dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boss_name_label_1 = QLabel(edit_raid_dialog)
        self.boss_name_label_1.setObjectName(u"boss_name_label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.boss_name_label_1.sizePolicy().hasHeightForWidth())
        self.boss_name_label_1.setSizePolicy(sizePolicy2)
        self.boss_name_label_1.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_3.addWidget(self.boss_name_label_1)

        self.boss_name_line_edit_1 = QLineEdit(edit_raid_dialog)
        self.boss_name_line_edit_1.setObjectName(u"boss_name_line_edit_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_1.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_1.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.boss_name_line_edit_1)

        self.boss_element_box_1 = QComboBox(edit_raid_dialog)
        self.boss_element_box_1.setObjectName(u"boss_element_box_1")

        self.horizontalLayout_3.addWidget(self.boss_element_box_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.boss_name_label_2 = QLabel(edit_raid_dialog)
        self.boss_name_label_2.setObjectName(u"boss_name_label_2")
        sizePolicy2.setHeightForWidth(self.boss_name_label_2.sizePolicy().hasHeightForWidth())
        self.boss_name_label_2.setSizePolicy(sizePolicy2)
        self.boss_name_label_2.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_4.addWidget(self.boss_name_label_2)

        self.boss_name_line_edit_2 = QLineEdit(edit_raid_dialog)
        self.boss_name_line_edit_2.setObjectName(u"boss_name_line_edit_2")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_2.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_2.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.boss_name_line_edit_2)

        self.boss_element_box_2 = QComboBox(edit_raid_dialog)
        self.boss_element_box_2.setObjectName(u"boss_element_box_2")

        self.horizontalLayout_4.addWidget(self.boss_element_box_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.boss_name_label_3 = QLabel(edit_raid_dialog)
        self.boss_name_label_3.setObjectName(u"boss_name_label_3")
        sizePolicy2.setHeightForWidth(self.boss_name_label_3.sizePolicy().hasHeightForWidth())
        self.boss_name_label_3.setSizePolicy(sizePolicy2)
        self.boss_name_label_3.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_5.addWidget(self.boss_name_label_3)

        self.boss_name_line_edit_3 = QLineEdit(edit_raid_dialog)
        self.boss_name_line_edit_3.setObjectName(u"boss_name_line_edit_3")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_3.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_3.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.boss_name_line_edit_3)

        self.boss_element_box_3 = QComboBox(edit_raid_dialog)
        self.boss_element_box_3.setObjectName(u"boss_element_box_3")

        self.horizontalLayout_5.addWidget(self.boss_element_box_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.boss_name_label_4 = QLabel(edit_raid_dialog)
        self.boss_name_label_4.setObjectName(u"boss_name_label_4")
        sizePolicy2.setHeightForWidth(self.boss_name_label_4.sizePolicy().hasHeightForWidth())
        self.boss_name_label_4.setSizePolicy(sizePolicy2)
        self.boss_name_label_4.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_6.addWidget(self.boss_name_label_4)

        self.boss_name_line_edit_4 = QLineEdit(edit_raid_dialog)
        self.boss_name_line_edit_4.setObjectName(u"boss_name_line_edit_4")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_4.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_4.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.boss_name_line_edit_4)

        self.boss_element_box_4 = QComboBox(edit_raid_dialog)
        self.boss_element_box_4.setObjectName(u"boss_element_box_4")

        self.horizontalLayout_6.addWidget(self.boss_element_box_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.boss_name_label_5 = QLabel(edit_raid_dialog)
        self.boss_name_label_5.setObjectName(u"boss_name_label_5")
        sizePolicy2.setHeightForWidth(self.boss_name_label_5.sizePolicy().hasHeightForWidth())
        self.boss_name_label_5.setSizePolicy(sizePolicy2)
        self.boss_name_label_5.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_7.addWidget(self.boss_name_label_5)

        self.boss_name_line_edit_5 = QLineEdit(edit_raid_dialog)
        self.boss_name_line_edit_5.setObjectName(u"boss_name_line_edit_5")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_5.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_5.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.boss_name_line_edit_5)

        self.boss_element_box_5 = QComboBox(edit_raid_dialog)
        self.boss_element_box_5.setObjectName(u"boss_element_box_5")

        self.horizontalLayout_7.addWidget(self.boss_element_box_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.delete_raid_button = QPushButton(edit_raid_dialog)
        self.delete_raid_button.setObjectName(u"delete_raid_button")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.delete_raid_button.setFont(font)

        self.horizontalLayout_9.addWidget(self.delete_raid_button)

        self.edit_raid_buttonBox = QDialogButtonBox(edit_raid_dialog)
        self.edit_raid_buttonBox.setObjectName(u"edit_raid_buttonBox")
        font1 = QFont()
        font1.setBold(True)
        self.edit_raid_buttonBox.setFont(font1)
        self.edit_raid_buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.edit_raid_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.edit_raid_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.edit_raid_buttonBox.setCenterButtons(True)

        self.horizontalLayout_9.addWidget(self.edit_raid_buttonBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(edit_raid_dialog)

        QMetaObject.connectSlotsByName(edit_raid_dialog)
    # setupUi

    def retranslateUi(self, edit_raid_dialog):
        edit_raid_dialog.setWindowTitle(QCoreApplication.translate("edit_raid_dialog", u"Edit Raid", None))
        self.label.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Select Raid:</span></p></body></html>", None))
        self.union_label.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Union:</span></p></body></html>", None))
        self.raid_name_label_2.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Raid Name:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.edit_user_boss_name_label.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">  Name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Weakness</span></p></body></html>", None))
        self.boss_name_label_1.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 1</span></p></body></html>", None))
        self.boss_name_label_2.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 2</span></p></body></html>", None))
        self.boss_name_label_3.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 3</span></p></body></html>", None))
        self.boss_name_label_4.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 4</span></p></body></html>", None))
        self.boss_name_label_5.setText(QCoreApplication.translate("edit_raid_dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 5</span></p></body></html>", None))
        self.delete_raid_button.setText(QCoreApplication.translate("edit_raid_dialog", u"Delete Raid", None))
    # retranslateUi

