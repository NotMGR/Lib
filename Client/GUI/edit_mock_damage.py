# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_mock_damage.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_edit_mock_form(object):
    def setupUi(self, edit_mock_form):
        if not edit_mock_form.objectName():
            edit_mock_form.setObjectName(u"edit_mock_form")
        edit_mock_form.resize(700, 216)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_mock_form.sizePolicy().hasHeightForWidth())
        edit_mock_form.setSizePolicy(sizePolicy)
        edit_mock_form.setMinimumSize(QSize(700, 216))
        edit_mock_form.setMaximumSize(QSize(700, 216))
        edit_mock_form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        edit_mock_form.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(edit_mock_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edit_name_label = QLabel(edit_mock_form)
        self.edit_name_label.setObjectName(u"edit_name_label")
        self.edit_name_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.edit_name_label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.boss_label_1 = QLabel(edit_mock_form)
        self.boss_label_1.setObjectName(u"boss_label_1")

        self.horizontalLayout_11.addWidget(self.boss_label_1)

        self.boss_weak_label_img_1 = QLabel(edit_mock_form)
        self.boss_weak_label_img_1.setObjectName(u"boss_weak_label_img_1")
        self.boss_weak_label_img_1.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_1.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_11.addWidget(self.boss_weak_label_img_1)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.boss_name_2 = QLabel(edit_mock_form)
        self.boss_name_2.setObjectName(u"boss_name_2")
        self.boss_name_2.setScaledContents(True)
        self.boss_name_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.boss_name_2)

        self.dmg_done_label = QLabel(edit_mock_form)
        self.dmg_done_label.setObjectName(u"dmg_done_label")

        self.verticalLayout.addWidget(self.dmg_done_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.boss_dmg_1 = QLineEdit(edit_mock_form)
        self.boss_dmg_1.setObjectName(u"boss_dmg_1")
        self.boss_dmg_1.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.boss_dmg_1)


        self.horizontalLayout_12.addLayout(self.verticalLayout)

        self.boss_name_1 = QLabel(edit_mock_form)
        self.boss_name_1.setObjectName(u"boss_name_1")
        self.boss_name_1.setScaledContents(True)
        self.boss_name_1.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.boss_name_1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nikke_img_label_1 = QLabel(edit_mock_form)
        self.nikke_img_label_1.setObjectName(u"nikke_img_label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nikke_img_label_1.sizePolicy().hasHeightForWidth())
        self.nikke_img_label_1.setSizePolicy(sizePolicy1)
        self.nikke_img_label_1.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_1.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_1)

        self.nikke_img_label_2 = QLabel(edit_mock_form)
        self.nikke_img_label_2.setObjectName(u"nikke_img_label_2")
        sizePolicy1.setHeightForWidth(self.nikke_img_label_2.sizePolicy().hasHeightForWidth())
        self.nikke_img_label_2.setSizePolicy(sizePolicy1)
        self.nikke_img_label_2.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_2)

        self.nikke_img_label_3 = QLabel(edit_mock_form)
        self.nikke_img_label_3.setObjectName(u"nikke_img_label_3")
        sizePolicy1.setHeightForWidth(self.nikke_img_label_3.sizePolicy().hasHeightForWidth())
        self.nikke_img_label_3.setSizePolicy(sizePolicy1)
        self.nikke_img_label_3.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_3)

        self.nikke_img_label_4 = QLabel(edit_mock_form)
        self.nikke_img_label_4.setObjectName(u"nikke_img_label_4")
        sizePolicy1.setHeightForWidth(self.nikke_img_label_4.sizePolicy().hasHeightForWidth())
        self.nikke_img_label_4.setSizePolicy(sizePolicy1)
        self.nikke_img_label_4.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_4)

        self.nikke_img_label_5 = QLabel(edit_mock_form)
        self.nikke_img_label_5.setObjectName(u"nikke_img_label_5")
        sizePolicy1.setHeightForWidth(self.nikke_img_label_5.sizePolicy().hasHeightForWidth())
        self.nikke_img_label_5.setSizePolicy(sizePolicy1)
        self.nikke_img_label_5.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nikke_cbox_1 = QComboBox(edit_mock_form)
        self.nikke_cbox_1.setObjectName(u"nikke_cbox_1")
        self.nikke_cbox_1.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_1.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_1)

        self.nikke_cbox_2 = QComboBox(edit_mock_form)
        self.nikke_cbox_2.setObjectName(u"nikke_cbox_2")
        self.nikke_cbox_2.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_2.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_2)

        self.nikke_cbox_3 = QComboBox(edit_mock_form)
        self.nikke_cbox_3.setObjectName(u"nikke_cbox_3")
        self.nikke_cbox_3.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_3.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_3)

        self.nikke_cbox_4 = QComboBox(edit_mock_form)
        self.nikke_cbox_4.setObjectName(u"nikke_cbox_4")
        self.nikke_cbox_4.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_4.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_4)

        self.nikke_cbox_5 = QComboBox(edit_mock_form)
        self.nikke_cbox_5.setObjectName(u"nikke_cbox_5")
        self.nikke_cbox_5.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_5.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.delete_mock_button = QPushButton(edit_mock_form)
        self.delete_mock_button.setObjectName(u"delete_mock_button")

        self.horizontalLayout_3.addWidget(self.delete_mock_button)

        self.buttonBox = QDialogButtonBox(edit_mock_form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.horizontalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(edit_mock_form)

        QMetaObject.connectSlotsByName(edit_mock_form)
    # setupUi

    def retranslateUi(self, edit_mock_form):
        edit_mock_form.setWindowTitle(QCoreApplication.translate("edit_mock_form", u"Edit Mock", None))
        self.edit_name_label.setText(QCoreApplication.translate("edit_mock_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">User:</span></p></body></html>", None))
        self.boss_label_1.setText(QCoreApplication.translate("edit_mock_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_1.setText(QCoreApplication.translate("edit_mock_form", u"w", None))
        self.boss_name_2.setText(QCoreApplication.translate("edit_mock_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label.setText(QCoreApplication.translate("edit_mock_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.boss_name_1.setText(QCoreApplication.translate("edit_mock_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.nikke_img_label_1.setText("")
        self.nikke_img_label_2.setText("")
        self.nikke_img_label_3.setText("")
        self.nikke_img_label_4.setText("")
        self.nikke_img_label_5.setText("")
        self.delete_mock_button.setText(QCoreApplication.translate("edit_mock_form", u"Delete Mock", None))
    # retranslateUi

