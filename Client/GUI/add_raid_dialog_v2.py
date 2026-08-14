# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_raid_dialog_v2.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Add_Raid_Dialog_v2(object):
    def setupUi(self, Add_Raid_Dialog_v2):
        if not Add_Raid_Dialog_v2.objectName():
            Add_Raid_Dialog_v2.setObjectName(u"Add_Raid_Dialog_v2")
        Add_Raid_Dialog_v2.resize(449, 422)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Add_Raid_Dialog_v2.sizePolicy().hasHeightForWidth())
        Add_Raid_Dialog_v2.setSizePolicy(sizePolicy)
        Add_Raid_Dialog_v2.setMinimumSize(QSize(449, 422))
        Add_Raid_Dialog_v2.setMaximumSize(QSize(449, 422))
        self.verticalLayout_2 = QVBoxLayout(Add_Raid_Dialog_v2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.raid_name_label_2 = QLabel(Add_Raid_Dialog_v2)
        self.raid_name_label_2.setObjectName(u"raid_name_label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.raid_name_label_2.sizePolicy().hasHeightForWidth())
        self.raid_name_label_2.setSizePolicy(sizePolicy1)
        self.raid_name_label_2.setMinimumSize(QSize(100, 40))
        self.raid_name_label_2.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_2.addWidget(self.raid_name_label_2)

        self.new_raid_name_line_edit = QLineEdit(Add_Raid_Dialog_v2)
        self.new_raid_name_line_edit.setObjectName(u"new_raid_name_line_edit")
        sizePolicy.setHeightForWidth(self.new_raid_name_line_edit.sizePolicy().hasHeightForWidth())
        self.new_raid_name_line_edit.setSizePolicy(sizePolicy)
        self.new_raid_name_line_edit.setMinimumSize(QSize(171, 24))
        self.new_raid_name_line_edit.setMaximumSize(QSize(171, 24))

        self.horizontalLayout_2.addWidget(self.new_raid_name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(Add_Raid_Dialog_v2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.boss_name_label = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label.setObjectName(u"boss_name_label")

        self.horizontalLayout_8.addWidget(self.boss_name_label)

        self.label_3 = QLabel(Add_Raid_Dialog_v2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boss_name_label_1 = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label_1.setObjectName(u"boss_name_label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.boss_name_label_1.sizePolicy().hasHeightForWidth())
        self.boss_name_label_1.setSizePolicy(sizePolicy2)
        self.boss_name_label_1.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_3.addWidget(self.boss_name_label_1)

        self.boss_name_line_edit_1 = QLineEdit(Add_Raid_Dialog_v2)
        self.boss_name_line_edit_1.setObjectName(u"boss_name_line_edit_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_1.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_1.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.boss_name_line_edit_1)

        self.boss_element_box_1 = QComboBox(Add_Raid_Dialog_v2)
        self.boss_element_box_1.setObjectName(u"boss_element_box_1")

        self.horizontalLayout_3.addWidget(self.boss_element_box_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.boss_name_label_2 = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label_2.setObjectName(u"boss_name_label_2")
        sizePolicy2.setHeightForWidth(self.boss_name_label_2.sizePolicy().hasHeightForWidth())
        self.boss_name_label_2.setSizePolicy(sizePolicy2)
        self.boss_name_label_2.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_4.addWidget(self.boss_name_label_2)

        self.boss_name_line_edit_2 = QLineEdit(Add_Raid_Dialog_v2)
        self.boss_name_line_edit_2.setObjectName(u"boss_name_line_edit_2")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_2.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_2.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.boss_name_line_edit_2)

        self.boss_element_box_2 = QComboBox(Add_Raid_Dialog_v2)
        self.boss_element_box_2.setObjectName(u"boss_element_box_2")

        self.horizontalLayout_4.addWidget(self.boss_element_box_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.boss_name_label_3 = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label_3.setObjectName(u"boss_name_label_3")
        sizePolicy2.setHeightForWidth(self.boss_name_label_3.sizePolicy().hasHeightForWidth())
        self.boss_name_label_3.setSizePolicy(sizePolicy2)
        self.boss_name_label_3.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_5.addWidget(self.boss_name_label_3)

        self.boss_name_line_edit_3 = QLineEdit(Add_Raid_Dialog_v2)
        self.boss_name_line_edit_3.setObjectName(u"boss_name_line_edit_3")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_3.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_3.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.boss_name_line_edit_3)

        self.boss_element_box_3 = QComboBox(Add_Raid_Dialog_v2)
        self.boss_element_box_3.setObjectName(u"boss_element_box_3")

        self.horizontalLayout_5.addWidget(self.boss_element_box_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.boss_name_label_4 = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label_4.setObjectName(u"boss_name_label_4")
        sizePolicy2.setHeightForWidth(self.boss_name_label_4.sizePolicy().hasHeightForWidth())
        self.boss_name_label_4.setSizePolicy(sizePolicy2)
        self.boss_name_label_4.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_6.addWidget(self.boss_name_label_4)

        self.boss_name_line_edit_4 = QLineEdit(Add_Raid_Dialog_v2)
        self.boss_name_line_edit_4.setObjectName(u"boss_name_line_edit_4")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_4.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_4.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.boss_name_line_edit_4)

        self.boss_element_box_4 = QComboBox(Add_Raid_Dialog_v2)
        self.boss_element_box_4.setObjectName(u"boss_element_box_4")

        self.horizontalLayout_6.addWidget(self.boss_element_box_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.boss_name_label_5 = QLabel(Add_Raid_Dialog_v2)
        self.boss_name_label_5.setObjectName(u"boss_name_label_5")
        sizePolicy2.setHeightForWidth(self.boss_name_label_5.sizePolicy().hasHeightForWidth())
        self.boss_name_label_5.setSizePolicy(sizePolicy2)
        self.boss_name_label_5.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_7.addWidget(self.boss_name_label_5)

        self.boss_name_line_edit_5 = QLineEdit(Add_Raid_Dialog_v2)
        self.boss_name_line_edit_5.setObjectName(u"boss_name_line_edit_5")
        sizePolicy3.setHeightForWidth(self.boss_name_line_edit_5.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit_5.setSizePolicy(sizePolicy3)
        self.boss_name_line_edit_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.boss_name_line_edit_5)

        self.boss_element_box_5 = QComboBox(Add_Raid_Dialog_v2)
        self.boss_element_box_5.setObjectName(u"boss_element_box_5")

        self.horizontalLayout_7.addWidget(self.boss_element_box_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.add_raid_buttonBox = QDialogButtonBox(Add_Raid_Dialog_v2)
        self.add_raid_buttonBox.setObjectName(u"add_raid_buttonBox")
        self.add_raid_buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.add_raid_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.add_raid_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.add_raid_buttonBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.add_raid_buttonBox)


        self.retranslateUi(Add_Raid_Dialog_v2)
        self.add_raid_buttonBox.accepted.connect(Add_Raid_Dialog_v2.accept)
        self.add_raid_buttonBox.rejected.connect(Add_Raid_Dialog_v2.reject)

        QMetaObject.connectSlotsByName(Add_Raid_Dialog_v2)
    # setupUi

    def retranslateUi(self, Add_Raid_Dialog_v2):
        Add_Raid_Dialog_v2.setWindowTitle(QCoreApplication.translate("Add_Raid_Dialog_v2", u"Dialog", None))
        self.raid_name_label_2.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Raid Name:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_label.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">  Name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Weakness</span></p></body></html>", None))
        self.boss_name_label_1.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 1</span></p></body></html>", None))
        self.boss_name_label_2.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 2</span></p></body></html>", None))
        self.boss_name_label_3.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 3</span></p></body></html>", None))
        self.boss_name_label_4.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 4</span></p></body></html>", None))
        self.boss_name_label_5.setText(QCoreApplication.translate("Add_Raid_Dialog_v2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Boss 5</span></p></body></html>", None))
    # retranslateUi

