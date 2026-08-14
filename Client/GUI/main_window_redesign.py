# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_redesign.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1223, 546)
        self.actionAdd_Raid = QAction(MainWindow)
        self.actionAdd_Raid.setObjectName(u"actionAdd_Raid")
        self.actionAdd_Nikke = QAction(MainWindow)
        self.actionAdd_Nikke.setObjectName(u"actionAdd_Nikke")
        self.actionEdit_Nikke = QAction(MainWindow)
        self.actionEdit_Nikke.setObjectName(u"actionEdit_Nikke")
        self.actionAdd_Mock_Damage = QAction(MainWindow)
        self.actionAdd_Mock_Damage.setObjectName(u"actionAdd_Mock_Damage")
        self.actionAdd_Damage = QAction(MainWindow)
        self.actionAdd_Damage.setObjectName(u"actionAdd_Damage")
        self.actionEdit_Mocks = QAction(MainWindow)
        self.actionEdit_Mocks.setObjectName(u"actionEdit_Mocks")
        self.actionEdit_Damage_Records = QAction(MainWindow)
        self.actionEdit_Damage_Records.setObjectName(u"actionEdit_Damage_Records")
        self.actionAdd_Raid_2 = QAction(MainWindow)
        self.actionAdd_Raid_2.setObjectName(u"actionAdd_Raid_2")
        self.actionEdit_Raid = QAction(MainWindow)
        self.actionEdit_Raid.setObjectName(u"actionEdit_Raid")
        self.actionAdd_Raid_Boss = QAction(MainWindow)
        self.actionAdd_Raid_Boss.setObjectName(u"actionAdd_Raid_Boss")
        self.actionEdit_Raid_Boss = QAction(MainWindow)
        self.actionEdit_Raid_Boss.setObjectName(u"actionEdit_Raid_Boss")
        self.actionAdd_Member = QAction(MainWindow)
        self.actionAdd_Member.setObjectName(u"actionAdd_Member")
        self.actionEdit_Member = QAction(MainWindow)
        self.actionEdit_Member.setObjectName(u"actionEdit_Member")
        self.actionServer = QAction(MainWindow)
        self.actionServer.setObjectName(u"actionServer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_stacked_widget = QStackedWidget(self.centralwidget)
        self.main_stacked_widget.setObjectName(u"main_stacked_widget")
        self.mocks_page = QWidget()
        self.mocks_page.setObjectName(u"mocks_page")
        self.gridLayout_3 = QGridLayout(self.mocks_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boss_button_layout = QVBoxLayout()
        self.boss_button_layout.setObjectName(u"boss_button_layout")
        self.boss_push_button_1 = QPushButton(self.mocks_page)
        self.boss_push_button_1.setObjectName(u"boss_push_button_1")
        self.boss_push_button_1.setMinimumSize(QSize(141, 71))

        self.boss_button_layout.addWidget(self.boss_push_button_1)

        self.boss_push_button_2 = QPushButton(self.mocks_page)
        self.boss_push_button_2.setObjectName(u"boss_push_button_2")
        self.boss_push_button_2.setMinimumSize(QSize(141, 71))

        self.boss_button_layout.addWidget(self.boss_push_button_2)

        self.boss_push_button_3 = QPushButton(self.mocks_page)
        self.boss_push_button_3.setObjectName(u"boss_push_button_3")
        self.boss_push_button_3.setMinimumSize(QSize(141, 71))

        self.boss_button_layout.addWidget(self.boss_push_button_3)

        self.boss_push_button_4 = QPushButton(self.mocks_page)
        self.boss_push_button_4.setObjectName(u"boss_push_button_4")
        self.boss_push_button_4.setMinimumSize(QSize(141, 71))

        self.boss_button_layout.addWidget(self.boss_push_button_4)

        self.boss_push_button_5 = QPushButton(self.mocks_page)
        self.boss_push_button_5.setObjectName(u"boss_push_button_5")
        self.boss_push_button_5.setMinimumSize(QSize(141, 71))

        self.boss_button_layout.addWidget(self.boss_push_button_5)

        self.spacing_label_3 = QLabel(self.mocks_page)
        self.spacing_label_3.setObjectName(u"spacing_label_3")
        self.spacing_label_3.setMaximumSize(QSize(200, 300))

        self.boss_button_layout.addWidget(self.spacing_label_3)


        self.horizontalLayout_3.addLayout(self.boss_button_layout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Sort_by_layout = QHBoxLayout()
        self.Sort_by_layout.setSpacing(5)
        self.Sort_by_layout.setObjectName(u"Sort_by_layout")
        self.Sort_by_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.Sort_by_layout.setContentsMargins(0, -1, 650, -1)
        self.sort_by_label = QLabel(self.mocks_page)
        self.sort_by_label.setObjectName(u"sort_by_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_by_label.sizePolicy().hasHeightForWidth())
        self.sort_by_label.setSizePolicy(sizePolicy)
        self.sort_by_label.setAutoFillBackground(False)
        self.sort_by_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.Sort_by_layout.addWidget(self.sort_by_label)

        self.member_sort_mock_button = QPushButton(self.mocks_page)
        self.member_sort_mock_button.setObjectName(u"member_sort_mock_button")
        sizePolicy.setHeightForWidth(self.member_sort_mock_button.sizePolicy().hasHeightForWidth())
        self.member_sort_mock_button.setSizePolicy(sizePolicy)

        self.Sort_by_layout.addWidget(self.member_sort_mock_button)

        self.damage_sort_mock_button = QPushButton(self.mocks_page)
        self.damage_sort_mock_button.setObjectName(u"damage_sort_mock_button")
        sizePolicy.setHeightForWidth(self.damage_sort_mock_button.sizePolicy().hasHeightForWidth())
        self.damage_sort_mock_button.setSizePolicy(sizePolicy)

        self.Sort_by_layout.addWidget(self.damage_sort_mock_button)

        self.show_inactive_mock_checkbox = QCheckBox(self.mocks_page)
        self.show_inactive_mock_checkbox.setObjectName(u"show_inactive_mock_checkbox")
        self.show_inactive_mock_checkbox.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.show_inactive_mock_checkbox.setFont(font)

        self.Sort_by_layout.addWidget(self.show_inactive_mock_checkbox)


        self.verticalLayout_5.addLayout(self.Sort_by_layout)

        self.mock_stacked_widget_1 = QStackedWidget(self.mocks_page)
        self.mock_stacked_widget_1.setObjectName(u"mock_stacked_widget_1")
        self.mock_stacked_widget_1.setFrameShape(QFrame.Shape.NoFrame)
        self.boss_page_1 = QWidget()
        self.boss_page_1.setObjectName(u"boss_page_1")
        self.gridLayout = QGridLayout(self.boss_page_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(-1, 15, 11, 11)
        self.mock_scroll_area_1 = QScrollArea(self.boss_page_1)
        self.mock_scroll_area_1.setObjectName(u"mock_scroll_area_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mock_scroll_area_1.sizePolicy().hasHeightForWidth())
        self.mock_scroll_area_1.setSizePolicy(sizePolicy1)
        self.mock_scroll_area_1.setWidgetResizable(True)
        self.mock_scroll_area_content_1 = QWidget()
        self.mock_scroll_area_content_1.setObjectName(u"mock_scroll_area_content_1")
        self.mock_scroll_area_content_1.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_2 = QVBoxLayout(self.mock_scroll_area_content_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 9, -1, -1)
        self.mock_scroll_area_1.setWidget(self.mock_scroll_area_content_1)

        self.gridLayout.addWidget(self.mock_scroll_area_1, 0, 0, 1, 1)

        self.mock_stacked_widget_1.addWidget(self.boss_page_1)
        self.boss_page_2 = QWidget()
        self.boss_page_2.setObjectName(u"boss_page_2")
        self.verticalLayout_8 = QVBoxLayout(self.boss_page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mock_scroll_area_2 = QScrollArea(self.boss_page_2)
        self.mock_scroll_area_2.setObjectName(u"mock_scroll_area_2")
        sizePolicy1.setHeightForWidth(self.mock_scroll_area_2.sizePolicy().hasHeightForWidth())
        self.mock_scroll_area_2.setSizePolicy(sizePolicy1)
        self.mock_scroll_area_2.setWidgetResizable(True)
        self.mock_scroll_area_content_2 = QWidget()
        self.mock_scroll_area_content_2.setObjectName(u"mock_scroll_area_content_2")
        self.mock_scroll_area_content_2.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_3 = QVBoxLayout(self.mock_scroll_area_content_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 9, -1, -1)
        self.mock_scroll_area_2.setWidget(self.mock_scroll_area_content_2)

        self.verticalLayout_8.addWidget(self.mock_scroll_area_2)

        self.mock_stacked_widget_1.addWidget(self.boss_page_2)
        self.boss_page_3 = QWidget()
        self.boss_page_3.setObjectName(u"boss_page_3")
        self.verticalLayout_9 = QVBoxLayout(self.boss_page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.mock_scroll_area_3 = QScrollArea(self.boss_page_3)
        self.mock_scroll_area_3.setObjectName(u"mock_scroll_area_3")
        sizePolicy1.setHeightForWidth(self.mock_scroll_area_3.sizePolicy().hasHeightForWidth())
        self.mock_scroll_area_3.setSizePolicy(sizePolicy1)
        self.mock_scroll_area_3.setWidgetResizable(True)
        self.mock_scroll_area_content_3 = QWidget()
        self.mock_scroll_area_content_3.setObjectName(u"mock_scroll_area_content_3")
        self.mock_scroll_area_content_3.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_14 = QVBoxLayout(self.mock_scroll_area_content_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.mock_scroll_area_3.setWidget(self.mock_scroll_area_content_3)

        self.verticalLayout_9.addWidget(self.mock_scroll_area_3)

        self.mock_stacked_widget_1.addWidget(self.boss_page_3)
        self.boss_page_4 = QWidget()
        self.boss_page_4.setObjectName(u"boss_page_4")
        self.verticalLayout_12 = QVBoxLayout(self.boss_page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.mock_scroll_area_4 = QScrollArea(self.boss_page_4)
        self.mock_scroll_area_4.setObjectName(u"mock_scroll_area_4")
        sizePolicy1.setHeightForWidth(self.mock_scroll_area_4.sizePolicy().hasHeightForWidth())
        self.mock_scroll_area_4.setSizePolicy(sizePolicy1)
        self.mock_scroll_area_4.setWidgetResizable(True)
        self.mock_scroll_area_content_4 = QWidget()
        self.mock_scroll_area_content_4.setObjectName(u"mock_scroll_area_content_4")
        self.mock_scroll_area_content_4.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_15 = QVBoxLayout(self.mock_scroll_area_content_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mock_scroll_area_4.setWidget(self.mock_scroll_area_content_4)

        self.verticalLayout_12.addWidget(self.mock_scroll_area_4)

        self.mock_stacked_widget_1.addWidget(self.boss_page_4)
        self.boss_page_5 = QWidget()
        self.boss_page_5.setObjectName(u"boss_page_5")
        self.verticalLayout_13 = QVBoxLayout(self.boss_page_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.mock_scroll_area_5 = QScrollArea(self.boss_page_5)
        self.mock_scroll_area_5.setObjectName(u"mock_scroll_area_5")
        sizePolicy1.setHeightForWidth(self.mock_scroll_area_5.sizePolicy().hasHeightForWidth())
        self.mock_scroll_area_5.setSizePolicy(sizePolicy1)
        self.mock_scroll_area_5.setWidgetResizable(True)
        self.mock_scroll_area_content_5 = QWidget()
        self.mock_scroll_area_content_5.setObjectName(u"mock_scroll_area_content_5")
        self.mock_scroll_area_content_5.setGeometry(QRect(0, 0, 1014, 347))
        self.verticalLayout_16 = QVBoxLayout(self.mock_scroll_area_content_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.mock_scroll_area_5.setWidget(self.mock_scroll_area_content_5)

        self.verticalLayout_13.addWidget(self.mock_scroll_area_5)

        self.mock_stacked_widget_1.addWidget(self.boss_page_5)

        self.verticalLayout_5.addWidget(self.mock_stacked_widget_1)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.main_stacked_widget.addWidget(self.mocks_page)
        self.current_attempts_page = QWidget()
        self.current_attempts_page.setObjectName(u"current_attempts_page")
        self.gridLayout_4 = QGridLayout(self.current_attempts_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 600, -1)
        self.sort_by_label_attempt = QLabel(self.current_attempts_page)
        self.sort_by_label_attempt.setObjectName(u"sort_by_label_attempt")
        sizePolicy.setHeightForWidth(self.sort_by_label_attempt.sizePolicy().hasHeightForWidth())
        self.sort_by_label_attempt.setSizePolicy(sizePolicy)
        self.sort_by_label_attempt.setAutoFillBackground(False)
        self.sort_by_label_attempt.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.sort_by_label_attempt)

        self.member_sort_attempt_button_2 = QPushButton(self.current_attempts_page)
        self.member_sort_attempt_button_2.setObjectName(u"member_sort_attempt_button_2")
        sizePolicy.setHeightForWidth(self.member_sort_attempt_button_2.sizePolicy().hasHeightForWidth())
        self.member_sort_attempt_button_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.member_sort_attempt_button_2)

        self.attempt_sort_button_2 = QPushButton(self.current_attempts_page)
        self.attempt_sort_button_2.setObjectName(u"attempt_sort_button_2")
        sizePolicy.setHeightForWidth(self.attempt_sort_button_2.sizePolicy().hasHeightForWidth())
        self.attempt_sort_button_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.attempt_sort_button_2)

        self.spacing_label_5 = QLabel(self.current_attempts_page)
        self.spacing_label_5.setObjectName(u"spacing_label_5")

        self.horizontalLayout_8.addWidget(self.spacing_label_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.member_title_label = QLabel(self.current_attempts_page)
        self.member_title_label.setObjectName(u"member_title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.member_title_label.sizePolicy().hasHeightForWidth())
        self.member_title_label.setSizePolicy(sizePolicy2)
        self.member_title_label.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.member_title_label)

        self.spacing_label_4 = QLabel(self.current_attempts_page)
        self.spacing_label_4.setObjectName(u"spacing_label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spacing_label_4.sizePolicy().hasHeightForWidth())
        self.spacing_label_4.setSizePolicy(sizePolicy3)
        self.spacing_label_4.setMaximumSize(QSize(30, 10))

        self.horizontalLayout_5.addWidget(self.spacing_label_4)

        self.boss_name_label_att_1 = QLabel(self.current_attempts_page)
        self.boss_name_label_att_1.setObjectName(u"boss_name_label_att_1")
        self.boss_name_label_att_1.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.boss_name_label_att_1)

        self.boss_weak_label_attempt_1 = QLabel(self.current_attempts_page)
        self.boss_weak_label_attempt_1.setObjectName(u"boss_weak_label_attempt_1")
        self.boss_weak_label_attempt_1.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_attempt_1.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.boss_weak_label_attempt_1)

        self.boss_name_label_att_2 = QLabel(self.current_attempts_page)
        self.boss_name_label_att_2.setObjectName(u"boss_name_label_att_2")
        self.boss_name_label_att_2.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.boss_name_label_att_2)

        self.boss_weak_label_attempt_2 = QLabel(self.current_attempts_page)
        self.boss_weak_label_attempt_2.setObjectName(u"boss_weak_label_attempt_2")
        self.boss_weak_label_attempt_2.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_attempt_2.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.boss_weak_label_attempt_2)

        self.boss_name_label_att_3 = QLabel(self.current_attempts_page)
        self.boss_name_label_att_3.setObjectName(u"boss_name_label_att_3")
        self.boss_name_label_att_3.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.boss_name_label_att_3)

        self.boss_weak_label_attempt_3 = QLabel(self.current_attempts_page)
        self.boss_weak_label_attempt_3.setObjectName(u"boss_weak_label_attempt_3")
        self.boss_weak_label_attempt_3.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_attempt_3.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.boss_weak_label_attempt_3)

        self.boss_name_label_att_4 = QLabel(self.current_attempts_page)
        self.boss_name_label_att_4.setObjectName(u"boss_name_label_att_4")
        self.boss_name_label_att_4.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.boss_name_label_att_4)

        self.boss_weak_label_attempt_4 = QLabel(self.current_attempts_page)
        self.boss_weak_label_attempt_4.setObjectName(u"boss_weak_label_attempt_4")
        self.boss_weak_label_attempt_4.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_attempt_4.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.boss_weak_label_attempt_4)

        self.boss_name_label_att_5 = QLabel(self.current_attempts_page)
        self.boss_name_label_att_5.setObjectName(u"boss_name_label_att_5")
        self.boss_name_label_att_5.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.boss_name_label_att_5)

        self.boss_weak_label_attempt_5 = QLabel(self.current_attempts_page)
        self.boss_weak_label_attempt_5.setObjectName(u"boss_weak_label_attempt_5")
        self.boss_weak_label_attempt_5.setMinimumSize(QSize(31, 31))
        self.boss_weak_label_attempt_5.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.boss_weak_label_attempt_5)

        self.attempts_left_label = QLabel(self.current_attempts_page)
        self.attempts_left_label.setObjectName(u"attempts_left_label")
        self.attempts_left_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_5.addWidget(self.attempts_left_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.attempts_scroll_area = QScrollArea(self.current_attempts_page)
        self.attempts_scroll_area.setObjectName(u"attempts_scroll_area")
        self.attempts_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1185, 332))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.attempts_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.attempts_scroll_area, 2, 0, 1, 1)

        self.main_stacked_widget.addWidget(self.current_attempts_page)
        self.ranking_page = QWidget()
        self.ranking_page.setObjectName(u"ranking_page")
        self.gridLayout_6 = QGridLayout(self.ranking_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.ranking_layout = QHBoxLayout()
        self.ranking_layout.setSpacing(15)
        self.ranking_layout.setObjectName(u"ranking_layout")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.boss_name_rank_label_1 = QLabel(self.ranking_page)
        self.boss_name_rank_label_1.setObjectName(u"boss_name_rank_label_1")

        self.horizontalLayout_6.addWidget(self.boss_name_rank_label_1)

        self.boss_weak_rank_label_1 = QLabel(self.ranking_page)
        self.boss_weak_rank_label_1.setObjectName(u"boss_weak_rank_label_1")
        self.boss_weak_rank_label_1.setMinimumSize(QSize(41, 31))
        self.boss_weak_rank_label_1.setMaximumSize(QSize(41, 31))
        self.boss_weak_rank_label_1.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.boss_weak_rank_label_1)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.ranking_page)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.ranking_page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.boss_rank_table_1 = QTableView(self.ranking_page)
        self.boss_rank_table_1.setObjectName(u"boss_rank_table_1")

        self.verticalLayout_11.addWidget(self.boss_rank_table_1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.avg_rank_label_1 = QLabel(self.ranking_page)
        self.avg_rank_label_1.setObjectName(u"avg_rank_label_1")

        self.horizontalLayout_27.addWidget(self.avg_rank_label_1)

        self.average_mock_number_1 = QLabel(self.ranking_page)
        self.average_mock_number_1.setObjectName(u"average_mock_number_1")

        self.horizontalLayout_27.addWidget(self.average_mock_number_1)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)


        self.ranking_layout.addLayout(self.verticalLayout_11)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.boss_name_rank_label_2 = QLabel(self.ranking_page)
        self.boss_name_rank_label_2.setObjectName(u"boss_name_rank_label_2")

        self.horizontalLayout_18.addWidget(self.boss_name_rank_label_2)

        self.boss_weak_rank_label_2 = QLabel(self.ranking_page)
        self.boss_weak_rank_label_2.setObjectName(u"boss_weak_rank_label_2")
        self.boss_weak_rank_label_2.setMinimumSize(QSize(41, 31))
        self.boss_weak_rank_label_2.setMaximumSize(QSize(41, 31))
        self.boss_weak_rank_label_2.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.boss_weak_rank_label_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_11 = QLabel(self.ranking_page)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_19.addWidget(self.label_11)

        self.label_12 = QLabel(self.ranking_page)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_19.addWidget(self.label_12)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)

        self.boss_rank_table_2 = QTableView(self.ranking_page)
        self.boss_rank_table_2.setObjectName(u"boss_rank_table_2")

        self.verticalLayout_20.addWidget(self.boss_rank_table_2)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.avg_rank_label_2 = QLabel(self.ranking_page)
        self.avg_rank_label_2.setObjectName(u"avg_rank_label_2")

        self.horizontalLayout_28.addWidget(self.avg_rank_label_2)

        self.average_mock_number_2 = QLabel(self.ranking_page)
        self.average_mock_number_2.setObjectName(u"average_mock_number_2")

        self.horizontalLayout_28.addWidget(self.average_mock_number_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_28)


        self.ranking_layout.addLayout(self.verticalLayout_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.boss_name_rank_label_3 = QLabel(self.ranking_page)
        self.boss_name_rank_label_3.setObjectName(u"boss_name_rank_label_3")

        self.horizontalLayout_20.addWidget(self.boss_name_rank_label_3)

        self.boss_weak_rank_label_3 = QLabel(self.ranking_page)
        self.boss_weak_rank_label_3.setObjectName(u"boss_weak_rank_label_3")
        self.boss_weak_rank_label_3.setMinimumSize(QSize(41, 31))
        self.boss_weak_rank_label_3.setMaximumSize(QSize(41, 31))
        self.boss_weak_rank_label_3.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.boss_weak_rank_label_3)


        self.verticalLayout_23.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_13 = QLabel(self.ranking_page)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_21.addWidget(self.label_13)

        self.label_14 = QLabel(self.ranking_page)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_21.addWidget(self.label_14)


        self.verticalLayout_23.addLayout(self.horizontalLayout_21)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)

        self.boss_rank_table_3 = QTableView(self.ranking_page)
        self.boss_rank_table_3.setObjectName(u"boss_rank_table_3")

        self.verticalLayout_22.addWidget(self.boss_rank_table_3)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.avg_rank_label_3 = QLabel(self.ranking_page)
        self.avg_rank_label_3.setObjectName(u"avg_rank_label_3")

        self.horizontalLayout_29.addWidget(self.avg_rank_label_3)

        self.average_mock_number_3 = QLabel(self.ranking_page)
        self.average_mock_number_3.setObjectName(u"average_mock_number_3")

        self.horizontalLayout_29.addWidget(self.average_mock_number_3)


        self.verticalLayout_22.addLayout(self.horizontalLayout_29)


        self.ranking_layout.addLayout(self.verticalLayout_22)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.boss_name_rank_label_4 = QLabel(self.ranking_page)
        self.boss_name_rank_label_4.setObjectName(u"boss_name_rank_label_4")

        self.horizontalLayout_22.addWidget(self.boss_name_rank_label_4)

        self.boss_weak_rank_label_4 = QLabel(self.ranking_page)
        self.boss_weak_rank_label_4.setObjectName(u"boss_weak_rank_label_4")
        self.boss_weak_rank_label_4.setMinimumSize(QSize(41, 31))
        self.boss_weak_rank_label_4.setMaximumSize(QSize(41, 31))
        self.boss_weak_rank_label_4.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.boss_weak_rank_label_4)


        self.verticalLayout_25.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_15 = QLabel(self.ranking_page)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_23.addWidget(self.label_15)

        self.label_16 = QLabel(self.ranking_page)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_23.addWidget(self.label_16)


        self.verticalLayout_25.addLayout(self.horizontalLayout_23)


        self.verticalLayout_24.addLayout(self.verticalLayout_25)

        self.boss_rank_table_4 = QTableView(self.ranking_page)
        self.boss_rank_table_4.setObjectName(u"boss_rank_table_4")

        self.verticalLayout_24.addWidget(self.boss_rank_table_4)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.avg_rank_label_4 = QLabel(self.ranking_page)
        self.avg_rank_label_4.setObjectName(u"avg_rank_label_4")

        self.horizontalLayout_30.addWidget(self.avg_rank_label_4)

        self.average_mock_number_4 = QLabel(self.ranking_page)
        self.average_mock_number_4.setObjectName(u"average_mock_number_4")

        self.horizontalLayout_30.addWidget(self.average_mock_number_4)


        self.verticalLayout_24.addLayout(self.horizontalLayout_30)


        self.ranking_layout.addLayout(self.verticalLayout_24)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.boss_name_rank_label_5 = QLabel(self.ranking_page)
        self.boss_name_rank_label_5.setObjectName(u"boss_name_rank_label_5")

        self.horizontalLayout_24.addWidget(self.boss_name_rank_label_5)

        self.boss_weak_rank_label_5 = QLabel(self.ranking_page)
        self.boss_weak_rank_label_5.setObjectName(u"boss_weak_rank_label_5")
        self.boss_weak_rank_label_5.setMinimumSize(QSize(41, 31))
        self.boss_weak_rank_label_5.setMaximumSize(QSize(41, 31))
        self.boss_weak_rank_label_5.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.boss_weak_rank_label_5)


        self.verticalLayout_27.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_17 = QLabel(self.ranking_page)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_25.addWidget(self.label_17)

        self.label_18 = QLabel(self.ranking_page)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_25.addWidget(self.label_18)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)

        self.boss_rank_table_5 = QTableView(self.ranking_page)
        self.boss_rank_table_5.setObjectName(u"boss_rank_table_5")

        self.verticalLayout_26.addWidget(self.boss_rank_table_5)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.avg_rank_label_5 = QLabel(self.ranking_page)
        self.avg_rank_label_5.setObjectName(u"avg_rank_label_5")

        self.horizontalLayout_31.addWidget(self.avg_rank_label_5)

        self.average_mock_number_5 = QLabel(self.ranking_page)
        self.average_mock_number_5.setObjectName(u"average_mock_number_5")

        self.horizontalLayout_31.addWidget(self.average_mock_number_5)


        self.verticalLayout_26.addLayout(self.horizontalLayout_31)


        self.ranking_layout.addLayout(self.verticalLayout_26)


        self.gridLayout_6.addLayout(self.ranking_layout, 1, 0, 1, 1)

        self.show_inactive_table_checkbox = QCheckBox(self.ranking_page)
        self.show_inactive_table_checkbox.setObjectName(u"show_inactive_table_checkbox")
        self.show_inactive_table_checkbox.setMinimumSize(QSize(150, 0))
        self.show_inactive_table_checkbox.setFont(font)

        self.gridLayout_6.addWidget(self.show_inactive_table_checkbox, 0, 0, 1, 1)

        self.main_stacked_widget.addWidget(self.ranking_page)

        self.gridLayout_2.addWidget(self.main_stacked_widget, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(8, -1, 9, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.Current_Raid_label = QLabel(self.centralwidget)
        self.Current_Raid_label.setObjectName(u"Current_Raid_label")
        self.Current_Raid_label.setMaximumSize(QSize(200, 16777215))
        self.Current_Raid_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.Current_Raid_label)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, -1, 1, -1)
        self.select_raid_cbox_main = QComboBox(self.centralwidget)
        self.select_raid_cbox_main.setObjectName(u"select_raid_cbox_main")
        sizePolicy1.setHeightForWidth(self.select_raid_cbox_main.sizePolicy().hasHeightForWidth())
        self.select_raid_cbox_main.setSizePolicy(sizePolicy1)
        self.select_raid_cbox_main.setMinimumSize(QSize(0, 0))
        self.select_raid_cbox_main.setMaximumSize(QSize(200, 24))
        self.select_raid_cbox_main.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.select_raid_cbox_main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.select_raid_cbox_main.setEditable(True)

        self.gridLayout_5.addWidget(self.select_raid_cbox_main, 0, 0, 1, 1)

        self.spacing_label_2 = QLabel(self.centralwidget)
        self.spacing_label_2.setObjectName(u"spacing_label_2")

        self.gridLayout_5.addWidget(self.spacing_label_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.mock_home_button = QPushButton(self.centralwidget)
        self.mock_home_button.setObjectName(u"mock_home_button")
        self.mock_home_button.setMinimumSize(QSize(181, 51))

        self.horizontalLayout_2.addWidget(self.mock_home_button)

        self.Attempt_tracker_button = QPushButton(self.centralwidget)
        self.Attempt_tracker_button.setObjectName(u"Attempt_tracker_button")
        self.Attempt_tracker_button.setMinimumSize(QSize(171, 51))

        self.horizontalLayout_2.addWidget(self.Attempt_tracker_button)

        self.ranking_button = QPushButton(self.centralwidget)
        self.ranking_button.setObjectName(u"ranking_button")
        self.ranking_button.setMinimumSize(QSize(181, 51))

        self.horizontalLayout_2.addWidget(self.ranking_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1223, 21))
        self.menuAdd = QMenu(self.menubar)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menudamage = QMenu(self.menubar)
        self.menudamage.setObjectName(u"menudamage")
        self.menuRaid = QMenu(self.menubar)
        self.menuRaid.setObjectName(u"menuRaid")
        self.menuMembers = QMenu(self.menubar)
        self.menuMembers.setObjectName(u"menuMembers")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMembers.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menudamage.menuAction())
        self.menubar.addAction(self.menuRaid.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuAdd.addAction(self.actionAdd_Nikke)
        self.menuAdd.addAction(self.actionEdit_Nikke)
        self.menudamage.addAction(self.actionAdd_Mock_Damage)
        self.menudamage.addAction(self.actionAdd_Damage)
        self.menudamage.addAction(self.actionEdit_Mocks)
        self.menuRaid.addAction(self.actionAdd_Raid_2)
        self.menuRaid.addAction(self.actionEdit_Raid)
        self.menuMembers.addAction(self.actionAdd_Member)
        self.menuMembers.addAction(self.actionEdit_Member)
        self.menuOptions.addAction(self.actionServer)

        self.retranslateUi(MainWindow)

        self.main_stacked_widget.setCurrentIndex(0)
        self.mock_stacked_widget_1.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Raid.setText(QCoreApplication.translate("MainWindow", u"Add Raid", None))
        self.actionAdd_Nikke.setText(QCoreApplication.translate("MainWindow", u"Add Nikke", None))
        self.actionEdit_Nikke.setText(QCoreApplication.translate("MainWindow", u"Edit Nikke", None))
        self.actionAdd_Mock_Damage.setText(QCoreApplication.translate("MainWindow", u"Add Mock Damage", None))
        self.actionAdd_Damage.setText(QCoreApplication.translate("MainWindow", u"Add Damage", None))
        self.actionEdit_Mocks.setText(QCoreApplication.translate("MainWindow", u"Edit Mocks", None))
        self.actionEdit_Damage_Records.setText(QCoreApplication.translate("MainWindow", u"Edit Damage Records", None))
        self.actionAdd_Raid_2.setText(QCoreApplication.translate("MainWindow", u"Add Raid", None))
        self.actionEdit_Raid.setText(QCoreApplication.translate("MainWindow", u"Edit Raid", None))
        self.actionAdd_Raid_Boss.setText(QCoreApplication.translate("MainWindow", u"Add Raid Boss", None))
        self.actionEdit_Raid_Boss.setText(QCoreApplication.translate("MainWindow", u"Edit Raid Boss", None))
        self.actionAdd_Member.setText(QCoreApplication.translate("MainWindow", u"Add Member", None))
        self.actionEdit_Member.setText(QCoreApplication.translate("MainWindow", u"Edit Member", None))
        self.actionServer.setText(QCoreApplication.translate("MainWindow", u"Select Server", None))
#if QT_CONFIG(tooltip)
        self.boss_push_button_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Boss 1</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.boss_push_button_1.setText(QCoreApplication.translate("MainWindow", u"Boss 1", None))
        self.boss_push_button_1.setProperty(u"role", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_2.setText(QCoreApplication.translate("MainWindow", u"Boss 2", None))
        self.boss_push_button_2.setProperty(u"role", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_3.setText(QCoreApplication.translate("MainWindow", u"Boss 3", None))
        self.boss_push_button_3.setProperty(u"boss_button", QCoreApplication.translate("MainWindow", u"boss_buton", None))
        self.boss_push_button_3.setProperty(u"role", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_4.setText(QCoreApplication.translate("MainWindow", u"Boss 4", None))
        self.boss_push_button_4.setProperty(u"boss_button", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_4.setProperty(u"role", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_5.setText(QCoreApplication.translate("MainWindow", u"Boss 5", None))
        self.boss_push_button_5.setProperty(u"boss_button", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.boss_push_button_5.setProperty(u"role", QCoreApplication.translate("MainWindow", u"boss_button", None))
        self.spacing_label_3.setText("")
        self.sort_by_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Sort by:</span></p></body></html>", None))
        self.member_sort_mock_button.setText(QCoreApplication.translate("MainWindow", u"Member \u2193", None))
        self.damage_sort_mock_button.setText(QCoreApplication.translate("MainWindow", u"Damage \u2193", None))
        self.show_inactive_mock_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Inactive", None))
        self.sort_by_label_attempt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Sort by:</span></p></body></html>", None))
        self.member_sort_attempt_button_2.setText(QCoreApplication.translate("MainWindow", u"Member \u2193", None))
        self.attempt_sort_button_2.setText(QCoreApplication.translate("MainWindow", u"Attempts Left \u2193", None))
        self.spacing_label_5.setText("")
        self.member_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Member</span></p></body></html>", None))
        self.spacing_label_4.setText("")
        self.boss_name_label_att_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_label_att_1.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_label_attempt_1.setText("")
        self.boss_name_label_att_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_label_att_2.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_label_attempt_2.setText("")
        self.boss_name_label_att_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_label_att_3.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_label_attempt_3.setText("")
        self.boss_name_label_att_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_label_att_4.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_label_attempt_4.setText("")
        self.boss_name_label_att_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_label_att_5.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_label_attempt_5.setText("")
        self.attempts_left_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Attempts Left</span></p></body></html>", None))
        self.attempts_left_label.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_name_rank_label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_rank_label_1.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_rank_label_1.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Damage</span></p></body></html>", None))
        self.avg_rank_label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Average:</span></p></body></html>", None))
        self.average_mock_number_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_rank_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_rank_label_2.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_rank_label_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Damage</span></p></body></html>", None))
        self.avg_rank_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Average:</span></p></body></html>", None))
        self.average_mock_number_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_rank_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_rank_label_3.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_rank_label_3.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Damage</span></p></body></html>", None))
        self.avg_rank_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Average:</span></p></body></html>", None))
        self.average_mock_number_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_rank_label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_rank_label_4.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_rank_label_4.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Damage</span></p></body></html>", None))
        self.avg_rank_label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Average:</span></p></body></html>", None))
        self.average_mock_number_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.boss_name_rank_label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.boss_name_rank_label_5.setProperty(u"role", QCoreApplication.translate("MainWindow", u"title", None))
        self.boss_weak_rank_label_5.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Damage</span></p></body></html>", None))
        self.avg_rank_label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Average:</span></p></body></html>", None))
        self.average_mock_number_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\"><br/></span></p></body></html>", None))
        self.show_inactive_table_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Inactive", None))
        self.Current_Raid_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Current Raid:</span></p></body></html>", None))
        self.spacing_label_2.setText("")
        self.mock_home_button.setText(QCoreApplication.translate("MainWindow", u"Mocks", None))
        self.mock_home_button.setProperty(u"role", QCoreApplication.translate("MainWindow", u"page_button", None))
        self.Attempt_tracker_button.setText(QCoreApplication.translate("MainWindow", u"Current Attempts", None))
        self.Attempt_tracker_button.setProperty(u"role", QCoreApplication.translate("MainWindow", u"page_button", None))
        self.ranking_button.setText(QCoreApplication.translate("MainWindow", u"Ranking", None))
        self.ranking_button.setProperty(u"role", QCoreApplication.translate("MainWindow", u"page_button", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"Nikke", None))
        self.menudamage.setTitle(QCoreApplication.translate("MainWindow", u"Damage", None))
        self.menuRaid.setTitle(QCoreApplication.translate("MainWindow", u"Raid", None))
        self.menuMembers.setTitle(QCoreApplication.translate("MainWindow", u"Members", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

