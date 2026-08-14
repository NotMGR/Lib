# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mock_damage.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_damage_done_form(object):
    def setupUi(self, damage_done_form):
        if not damage_done_form.objectName():
            damage_done_form.setObjectName(u"damage_done_form")
        damage_done_form.resize(689, 836)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(damage_done_form.sizePolicy().hasHeightForWidth())
        damage_done_form.setSizePolicy(sizePolicy)
        damage_done_form.setMinimumSize(QSize(689, 836))
        damage_done_form.setMaximumSize(QSize(689, 836))
        damage_done_form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        damage_done_form.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(damage_done_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.select_user_label = QLabel(damage_done_form)
        self.select_user_label.setObjectName(u"select_user_label")

        self.horizontalLayout_11.addWidget(self.select_user_label)

        self.select_user_cbox = QComboBox(damage_done_form)
        self.select_user_cbox.setObjectName(u"select_user_cbox")
        self.select_user_cbox.setEditable(True)

        self.horizontalLayout_11.addWidget(self.select_user_cbox)

        self.select_raid_label = QLabel(damage_done_form)
        self.select_raid_label.setObjectName(u"select_raid_label")

        self.horizontalLayout_11.addWidget(self.select_raid_label)

        self.select_raid_cbox = QComboBox(damage_done_form)
        self.select_raid_cbox.setObjectName(u"select_raid_cbox")
        self.select_raid_cbox.setEditable(True)

        self.horizontalLayout_11.addWidget(self.select_raid_cbox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boss_label = QLabel(damage_done_form)
        self.boss_label.setObjectName(u"boss_label")

        self.horizontalLayout_3.addWidget(self.boss_label)

        self.boss_weak_label_img_1 = QLabel(damage_done_form)
        self.boss_weak_label_img_1.setObjectName(u"boss_weak_label_img_1")
        self.boss_weak_label_img_1.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_1.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_3.addWidget(self.boss_weak_label_img_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.boss_name_1 = QLabel(damage_done_form)
        self.boss_name_1.setObjectName(u"boss_name_1")
        self.boss_name_1.setScaledContents(True)
        self.boss_name_1.setWordWrap(True)

        self.verticalLayout.addWidget(self.boss_name_1)

        self.dmg_done_label = QLabel(damage_done_form)
        self.dmg_done_label.setObjectName(u"dmg_done_label")

        self.verticalLayout.addWidget(self.dmg_done_label)

        self.boss_dmg_1 = QLineEdit(damage_done_form)
        self.boss_dmg_1.setObjectName(u"boss_dmg_1")

        self.verticalLayout.addWidget(self.boss_dmg_1)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nikke_img_label_1 = QLabel(damage_done_form)
        self.nikke_img_label_1.setObjectName(u"nikke_img_label_1")
        self.nikke_img_label_1.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_1.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_1)

        self.nikke_img_label_2 = QLabel(damage_done_form)
        self.nikke_img_label_2.setObjectName(u"nikke_img_label_2")
        self.nikke_img_label_2.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_2)

        self.nikke_img_label_3 = QLabel(damage_done_form)
        self.nikke_img_label_3.setObjectName(u"nikke_img_label_3")
        self.nikke_img_label_3.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_3)

        self.nikke_img_label_4 = QLabel(damage_done_form)
        self.nikke_img_label_4.setObjectName(u"nikke_img_label_4")
        self.nikke_img_label_4.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_4)

        self.nikke_img_label_5 = QLabel(damage_done_form)
        self.nikke_img_label_5.setObjectName(u"nikke_img_label_5")
        self.nikke_img_label_5.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.nikke_img_label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nikke_cbox_1 = QComboBox(damage_done_form)
        self.nikke_cbox_1.setObjectName(u"nikke_cbox_1")
        self.nikke_cbox_1.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_1.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_1)

        self.nikke_cbox_2 = QComboBox(damage_done_form)
        self.nikke_cbox_2.setObjectName(u"nikke_cbox_2")
        self.nikke_cbox_2.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_2.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_2)

        self.nikke_cbox_3 = QComboBox(damage_done_form)
        self.nikke_cbox_3.setObjectName(u"nikke_cbox_3")
        self.nikke_cbox_3.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_3.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_3)

        self.nikke_cbox_4 = QComboBox(damage_done_form)
        self.nikke_cbox_4.setObjectName(u"nikke_cbox_4")
        self.nikke_cbox_4.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_4.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_4)

        self.nikke_cbox_5 = QComboBox(damage_done_form)
        self.nikke_cbox_5.setObjectName(u"nikke_cbox_5")
        self.nikke_cbox_5.setMinimumSize(QSize(90, 0))
        self.nikke_cbox_5.setEditable(True)

        self.horizontalLayout_2.addWidget(self.nikke_cbox_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.boss_label_2 = QLabel(damage_done_form)
        self.boss_label_2.setObjectName(u"boss_label_2")

        self.horizontalLayout_6.addWidget(self.boss_label_2)

        self.boss_weak_label_img_2 = QLabel(damage_done_form)
        self.boss_weak_label_img_2.setObjectName(u"boss_weak_label_img_2")
        self.boss_weak_label_img_2.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_2.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_6.addWidget(self.boss_weak_label_img_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.boss_name_2 = QLabel(damage_done_form)
        self.boss_name_2.setObjectName(u"boss_name_2")
        self.boss_name_2.setScaledContents(True)
        self.boss_name_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.boss_name_2)

        self.dmg_done_label_2 = QLabel(damage_done_form)
        self.dmg_done_label_2.setObjectName(u"dmg_done_label_2")

        self.verticalLayout_3.addWidget(self.dmg_done_label_2)

        self.boss_dmg_2 = QLineEdit(damage_done_form)
        self.boss_dmg_2.setObjectName(u"boss_dmg_2")

        self.verticalLayout_3.addWidget(self.boss_dmg_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.nikke_img_label_6 = QLabel(damage_done_form)
        self.nikke_img_label_6.setObjectName(u"nikke_img_label_6")
        self.nikke_img_label_6.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_6.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.nikke_img_label_6)

        self.nikke_img_label_7 = QLabel(damage_done_form)
        self.nikke_img_label_7.setObjectName(u"nikke_img_label_7")
        self.nikke_img_label_7.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_7.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.nikke_img_label_7)

        self.nikke_img_label_8 = QLabel(damage_done_form)
        self.nikke_img_label_8.setObjectName(u"nikke_img_label_8")
        self.nikke_img_label_8.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_8.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.nikke_img_label_8)

        self.nikke_img_label_9 = QLabel(damage_done_form)
        self.nikke_img_label_9.setObjectName(u"nikke_img_label_9")
        self.nikke_img_label_9.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_9.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.nikke_img_label_9)

        self.nikke_img_label_10 = QLabel(damage_done_form)
        self.nikke_img_label_10.setObjectName(u"nikke_img_label_10")
        self.nikke_img_label_10.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_10.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.nikke_img_label_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.nikke_cbox_6 = QComboBox(damage_done_form)
        self.nikke_cbox_6.setObjectName(u"nikke_cbox_6")
        self.nikke_cbox_6.setEditable(True)

        self.horizontalLayout_8.addWidget(self.nikke_cbox_6)

        self.nikke_cbox_7 = QComboBox(damage_done_form)
        self.nikke_cbox_7.setObjectName(u"nikke_cbox_7")
        self.nikke_cbox_7.setEditable(True)

        self.horizontalLayout_8.addWidget(self.nikke_cbox_7)

        self.nikke_cbox_8 = QComboBox(damage_done_form)
        self.nikke_cbox_8.setObjectName(u"nikke_cbox_8")
        self.nikke_cbox_8.setEditable(True)

        self.horizontalLayout_8.addWidget(self.nikke_cbox_8)

        self.nikke_cbox_9 = QComboBox(damage_done_form)
        self.nikke_cbox_9.setObjectName(u"nikke_cbox_9")
        self.nikke_cbox_9.setEditable(True)

        self.horizontalLayout_8.addWidget(self.nikke_cbox_9)

        self.nikke_cbox_10 = QComboBox(damage_done_form)
        self.nikke_cbox_10.setObjectName(u"nikke_cbox_10")
        self.nikke_cbox_10.setEditable(True)

        self.horizontalLayout_8.addWidget(self.nikke_cbox_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.boss_label_3 = QLabel(damage_done_form)
        self.boss_label_3.setObjectName(u"boss_label_3")

        self.horizontalLayout_10.addWidget(self.boss_label_3)

        self.boss_weak_label_img_3 = QLabel(damage_done_form)
        self.boss_weak_label_img_3.setObjectName(u"boss_weak_label_img_3")
        self.boss_weak_label_img_3.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_3.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_10.addWidget(self.boss_weak_label_img_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.boss_name_3 = QLabel(damage_done_form)
        self.boss_name_3.setObjectName(u"boss_name_3")
        self.boss_name_3.setScaledContents(True)
        self.boss_name_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.boss_name_3)

        self.dmg_done_label_3 = QLabel(damage_done_form)
        self.dmg_done_label_3.setObjectName(u"dmg_done_label_3")

        self.verticalLayout_5.addWidget(self.dmg_done_label_3)

        self.boss_dmg_3 = QLineEdit(damage_done_form)
        self.boss_dmg_3.setObjectName(u"boss_dmg_3")

        self.verticalLayout_5.addWidget(self.boss_dmg_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.nikke_img_label_11 = QLabel(damage_done_form)
        self.nikke_img_label_11.setObjectName(u"nikke_img_label_11")
        self.nikke_img_label_11.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_11.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.nikke_img_label_11)

        self.nikke_img_label_12 = QLabel(damage_done_form)
        self.nikke_img_label_12.setObjectName(u"nikke_img_label_12")
        self.nikke_img_label_12.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_12.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.nikke_img_label_12)

        self.nikke_img_label_13 = QLabel(damage_done_form)
        self.nikke_img_label_13.setObjectName(u"nikke_img_label_13")
        self.nikke_img_label_13.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_13.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.nikke_img_label_13)

        self.nikke_img_label_14 = QLabel(damage_done_form)
        self.nikke_img_label_14.setObjectName(u"nikke_img_label_14")
        self.nikke_img_label_14.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_14.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.nikke_img_label_14)

        self.nikke_img_label_15 = QLabel(damage_done_form)
        self.nikke_img_label_15.setObjectName(u"nikke_img_label_15")
        self.nikke_img_label_15.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_15.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.nikke_img_label_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.nikke_cbox_11 = QComboBox(damage_done_form)
        self.nikke_cbox_11.setObjectName(u"nikke_cbox_11")
        self.nikke_cbox_11.setEditable(True)

        self.horizontalLayout_13.addWidget(self.nikke_cbox_11)

        self.nikke_cbox_12 = QComboBox(damage_done_form)
        self.nikke_cbox_12.setObjectName(u"nikke_cbox_12")
        self.nikke_cbox_12.setEditable(True)

        self.horizontalLayout_13.addWidget(self.nikke_cbox_12)

        self.nikke_cbox_13 = QComboBox(damage_done_form)
        self.nikke_cbox_13.setObjectName(u"nikke_cbox_13")
        self.nikke_cbox_13.setEditable(True)

        self.horizontalLayout_13.addWidget(self.nikke_cbox_13)

        self.nikke_cbox_14 = QComboBox(damage_done_form)
        self.nikke_cbox_14.setObjectName(u"nikke_cbox_14")
        self.nikke_cbox_14.setEditable(True)

        self.horizontalLayout_13.addWidget(self.nikke_cbox_14)

        self.nikke_cbox_15 = QComboBox(damage_done_form)
        self.nikke_cbox_15.setObjectName(u"nikke_cbox_15")
        self.nikke_cbox_15.setEditable(True)

        self.horizontalLayout_13.addWidget(self.nikke_cbox_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.boss_label_4 = QLabel(damage_done_form)
        self.boss_label_4.setObjectName(u"boss_label_4")

        self.horizontalLayout_15.addWidget(self.boss_label_4)

        self.boss_weak_label_img_4 = QLabel(damage_done_form)
        self.boss_weak_label_img_4.setObjectName(u"boss_weak_label_img_4")
        self.boss_weak_label_img_4.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_4.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_15.addWidget(self.boss_weak_label_img_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.boss_name_4 = QLabel(damage_done_form)
        self.boss_name_4.setObjectName(u"boss_name_4")
        self.boss_name_4.setScaledContents(True)
        self.boss_name_4.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.boss_name_4)

        self.dmg_done_label_4 = QLabel(damage_done_form)
        self.dmg_done_label_4.setObjectName(u"dmg_done_label_4")

        self.verticalLayout_7.addWidget(self.dmg_done_label_4)

        self.boss_dmg_4 = QLineEdit(damage_done_form)
        self.boss_dmg_4.setObjectName(u"boss_dmg_4")

        self.verticalLayout_7.addWidget(self.boss_dmg_4)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.nikke_img_label_16 = QLabel(damage_done_form)
        self.nikke_img_label_16.setObjectName(u"nikke_img_label_16")
        self.nikke_img_label_16.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_16.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.nikke_img_label_16)

        self.nikke_img_label_17 = QLabel(damage_done_form)
        self.nikke_img_label_17.setObjectName(u"nikke_img_label_17")
        self.nikke_img_label_17.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_17.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.nikke_img_label_17)

        self.nikke_img_label_18 = QLabel(damage_done_form)
        self.nikke_img_label_18.setObjectName(u"nikke_img_label_18")
        self.nikke_img_label_18.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_18.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.nikke_img_label_18)

        self.nikke_img_label_19 = QLabel(damage_done_form)
        self.nikke_img_label_19.setObjectName(u"nikke_img_label_19")
        self.nikke_img_label_19.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_19.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.nikke_img_label_19)

        self.nikke_img_label_20 = QLabel(damage_done_form)
        self.nikke_img_label_20.setObjectName(u"nikke_img_label_20")
        self.nikke_img_label_20.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_20.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.nikke_img_label_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.nikke_cbox_16 = QComboBox(damage_done_form)
        self.nikke_cbox_16.setObjectName(u"nikke_cbox_16")
        self.nikke_cbox_16.setEditable(True)

        self.horizontalLayout_17.addWidget(self.nikke_cbox_16)

        self.nikke_cbox_17 = QComboBox(damage_done_form)
        self.nikke_cbox_17.setObjectName(u"nikke_cbox_17")
        self.nikke_cbox_17.setEditable(True)

        self.horizontalLayout_17.addWidget(self.nikke_cbox_17)

        self.nikke_cbox_18 = QComboBox(damage_done_form)
        self.nikke_cbox_18.setObjectName(u"nikke_cbox_18")
        self.nikke_cbox_18.setEditable(True)

        self.horizontalLayout_17.addWidget(self.nikke_cbox_18)

        self.nikke_cbox_19 = QComboBox(damage_done_form)
        self.nikke_cbox_19.setObjectName(u"nikke_cbox_19")
        self.nikke_cbox_19.setEditable(True)

        self.horizontalLayout_17.addWidget(self.nikke_cbox_19)

        self.nikke_cbox_20 = QComboBox(damage_done_form)
        self.nikke_cbox_20.setObjectName(u"nikke_cbox_20")
        self.nikke_cbox_20.setEditable(True)

        self.horizontalLayout_17.addWidget(self.nikke_cbox_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.boss_label_5 = QLabel(damage_done_form)
        self.boss_label_5.setObjectName(u"boss_label_5")

        self.horizontalLayout_19.addWidget(self.boss_label_5)

        self.boss_weak_label_img_5 = QLabel(damage_done_form)
        self.boss_weak_label_img_5.setObjectName(u"boss_weak_label_img_5")
        self.boss_weak_label_img_5.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_img_5.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_19.addWidget(self.boss_weak_label_img_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.boss_name_5 = QLabel(damage_done_form)
        self.boss_name_5.setObjectName(u"boss_name_5")
        self.boss_name_5.setScaledContents(True)
        self.boss_name_5.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.boss_name_5)

        self.dmg_done_label_5 = QLabel(damage_done_form)
        self.dmg_done_label_5.setObjectName(u"dmg_done_label_5")

        self.verticalLayout_9.addWidget(self.dmg_done_label_5)

        self.boss_dmg_5 = QLineEdit(damage_done_form)
        self.boss_dmg_5.setObjectName(u"boss_dmg_5")

        self.verticalLayout_9.addWidget(self.boss_dmg_5)


        self.horizontalLayout_18.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.nikke_img_label_21 = QLabel(damage_done_form)
        self.nikke_img_label_21.setObjectName(u"nikke_img_label_21")
        self.nikke_img_label_21.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_21.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.nikke_img_label_21)

        self.nikke_img_label_22 = QLabel(damage_done_form)
        self.nikke_img_label_22.setObjectName(u"nikke_img_label_22")
        self.nikke_img_label_22.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_22.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.nikke_img_label_22)

        self.nikke_img_label_23 = QLabel(damage_done_form)
        self.nikke_img_label_23.setObjectName(u"nikke_img_label_23")
        self.nikke_img_label_23.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_23.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.nikke_img_label_23)

        self.nikke_img_label_24 = QLabel(damage_done_form)
        self.nikke_img_label_24.setObjectName(u"nikke_img_label_24")
        self.nikke_img_label_24.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_24.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.nikke_img_label_24)

        self.nikke_img_label_25 = QLabel(damage_done_form)
        self.nikke_img_label_25.setObjectName(u"nikke_img_label_25")
        self.nikke_img_label_25.setMinimumSize(QSize(90, 90))
        self.nikke_img_label_25.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.nikke_img_label_25)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.nikke_cbox_21 = QComboBox(damage_done_form)
        self.nikke_cbox_21.setObjectName(u"nikke_cbox_21")
        self.nikke_cbox_21.setEditable(True)

        self.horizontalLayout_21.addWidget(self.nikke_cbox_21)

        self.nikke_cbox_22 = QComboBox(damage_done_form)
        self.nikke_cbox_22.setObjectName(u"nikke_cbox_22")
        self.nikke_cbox_22.setEditable(True)

        self.horizontalLayout_21.addWidget(self.nikke_cbox_22)

        self.nikke_cbox_23 = QComboBox(damage_done_form)
        self.nikke_cbox_23.setObjectName(u"nikke_cbox_23")
        self.nikke_cbox_23.setEditable(True)

        self.horizontalLayout_21.addWidget(self.nikke_cbox_23)

        self.nikke_cbox_24 = QComboBox(damage_done_form)
        self.nikke_cbox_24.setObjectName(u"nikke_cbox_24")
        self.nikke_cbox_24.setEditable(True)

        self.horizontalLayout_21.addWidget(self.nikke_cbox_24)

        self.nikke_cbox_25 = QComboBox(damage_done_form)
        self.nikke_cbox_25.setObjectName(u"nikke_cbox_25")
        self.nikke_cbox_25.setEditable(True)

        self.horizontalLayout_21.addWidget(self.nikke_cbox_25)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_18.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.buttonBox = QDialogButtonBox(damage_done_form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_11.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.retranslateUi(damage_done_form)

        QMetaObject.connectSlotsByName(damage_done_form)
    # setupUi

    def retranslateUi(self, damage_done_form):
        damage_done_form.setWindowTitle(QCoreApplication.translate("damage_done_form", u"Add Mocks", None))
        self.select_user_label.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Select user:</span></p></body></html>", None))
        self.select_raid_label.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Select Raid:</span></p></body></html>", None))
        self.boss_label.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_1.setText(QCoreApplication.translate("damage_done_form", u"w", None))
        self.boss_name_1.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.nikke_img_label_1.setText("")
        self.nikke_img_label_2.setText("")
        self.nikke_img_label_3.setText("")
        self.nikke_img_label_4.setText("")
        self.nikke_img_label_5.setText("")
        self.boss_label_2.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_2.setText(QCoreApplication.translate("damage_done_form", u"w", None))
        self.boss_name_2.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label_2.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.nikke_img_label_6.setText("")
        self.nikke_img_label_7.setText("")
        self.nikke_img_label_8.setText("")
        self.nikke_img_label_9.setText("")
        self.nikke_img_label_10.setText("")
        self.boss_label_3.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_3.setText(QCoreApplication.translate("damage_done_form", u"w", None))
        self.boss_name_3.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label_3.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.nikke_img_label_11.setText("")
        self.nikke_img_label_12.setText("")
        self.nikke_img_label_13.setText("")
        self.nikke_img_label_14.setText("")
        self.nikke_img_label_15.setText("")
        self.boss_label_4.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_4.setText(QCoreApplication.translate("damage_done_form", u"w", None))
        self.boss_name_4.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label_4.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.nikke_img_label_16.setText("")
        self.nikke_img_label_17.setText("")
        self.nikke_img_label_18.setText("")
        self.nikke_img_label_19.setText("")
        self.nikke_img_label_20.setText("")
        self.boss_label_5.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Boss:</span></p></body></html>", None))
        self.boss_weak_label_img_5.setText(QCoreApplication.translate("damage_done_form", u"w", None))
        self.boss_name_5.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.dmg_done_label_5.setText(QCoreApplication.translate("damage_done_form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Damage Done:</span></p></body></html>", None))
        self.nikke_img_label_21.setText("")
        self.nikke_img_label_22.setText("")
        self.nikke_img_label_23.setText("")
        self.nikke_img_label_24.setText("")
        self.nikke_img_label_25.setText("")
    # retranslateUi

