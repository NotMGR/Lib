# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_boss_dialog.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Boss_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(225, 170)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(225, 170))
        Dialog.setMaximumSize(QSize(225, 170))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.boss_raid_label = QLabel(Dialog)
        self.boss_raid_label.setObjectName(u"boss_raid_label")
        self.boss_raid_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.boss_raid_label)

        self.boss_raid_box = QComboBox(Dialog)
        self.boss_raid_box.setObjectName(u"boss_raid_box")
        self.boss_raid_box.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.boss_raid_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boss_name_label = QLabel(Dialog)
        self.boss_name_label.setObjectName(u"boss_name_label")
        self.boss_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.boss_name_label)

        self.boss_name_line_edit = QLineEdit(Dialog)
        self.boss_name_line_edit.setObjectName(u"boss_name_line_edit")
        sizePolicy.setHeightForWidth(self.boss_name_line_edit.sizePolicy().hasHeightForWidth())
        self.boss_name_line_edit.setSizePolicy(sizePolicy)
        self.boss_name_line_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.boss_name_line_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.boss_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boss_element_label = QLabel(Dialog)
        self.boss_element_label.setObjectName(u"boss_element_label")

        self.horizontalLayout.addWidget(self.boss_element_label)

        self.boss_element_box = QComboBox(Dialog)
        self.boss_element_box.setObjectName(u"boss_element_box")

        self.horizontalLayout.addWidget(self.boss_element_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boss_hp_label = QLabel(Dialog)
        self.boss_hp_label.setObjectName(u"boss_hp_label")

        self.horizontalLayout_2.addWidget(self.boss_hp_label)

        self.boss_hp_line_edit = QLineEdit(Dialog)
        self.boss_hp_line_edit.setObjectName(u"boss_hp_line_edit")
        sizePolicy.setHeightForWidth(self.boss_hp_line_edit.sizePolicy().hasHeightForWidth())
        self.boss_hp_line_edit.setSizePolicy(sizePolicy)
        self.boss_hp_line_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.boss_hp_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox_2 = QDialogButtonBox(Dialog)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_2.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.boss_raid_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Raid:</span></p></body></html>", None))
        self.boss_name_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Boss name:</span></p></body></html>", None))
        self.boss_element_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weakness:</span></p></body></html>", None))
        self.boss_hp_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hp:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.buttonBox_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

