# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 590)
        self.actionAdd_Store = QAction(MainWindow)
        self.actionAdd_Store.setObjectName(u"actionAdd_Store")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: black;")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 10, 781, 551))
        self.upload_listing = QWidget()
        self.upload_listing.setObjectName(u"upload_listing")
        self.action_label = QLabel(self.upload_listing)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setGeometry(QRect(10, 490, 91, 16))
        self.action_label.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.upload_button = QPushButton(self.upload_listing)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setGeometry(QRect(10, 60, 231, 31))
        self.upload_button.setStyleSheet(u"background-color: white;\n"
"")
        self.submit_button = QPushButton(self.upload_listing)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(10, 460, 371, 23))
        self.submit_button.setStyleSheet(u"background-color: gray;\n"
"")
        self.user_input = QLineEdit(self.upload_listing)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(10, 100, 371, 21))
        self.user_input.setStyleSheet(u"background-color:white;\n"
"")
        self.gridLayoutWidget = QWidget(self.upload_listing)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 130, 371, 311))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.shopname_list = QListWidget(self.gridLayoutWidget)
        self.shopname_list.setObjectName(u"shopname_list")
        self.shopname_list.setStyleSheet(u"background-color: white;")

        self.gridLayout.addWidget(self.shopname_list, 1, 0, 1, 1)

        self.shopname_label = QLabel(self.gridLayoutWidget)
        self.shopname_label.setObjectName(u"shopname_label")
        self.shopname_label.setStyleSheet(u"color: white\n"
"")

        self.gridLayout.addWidget(self.shopname_label, 0, 0, 1, 1)

        self.description_label = QLabel(self.gridLayoutWidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.description_label, 0, 1, 1, 1)

        self.toggle_button = QPushButton(self.gridLayoutWidget)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setStyleSheet(u"background-color: white;\n"
"")

        self.gridLayout.addWidget(self.toggle_button, 2, 0, 1, 1)

        self.description = QPlainTextEdit(self.gridLayoutWidget)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"background-color: white;\n"
"")
        self.description.setReadOnly(True)

        self.gridLayout.addWidget(self.description, 1, 1, 2, 1)

        self.selected_label = QLabel(self.upload_listing)
        self.selected_label.setObjectName(u"selected_label")
        self.selected_label.setGeometry(QRect(310, 60, 71, 31))
        self.selected_label.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"")
        self.terminal = QListWidget(self.upload_listing)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setGeometry(QRect(390, 60, 371, 421))
        self.terminal.setStyleSheet(u"color:white;\n"
"")
        self.title = QLabel(self.upload_listing)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 241, 31))
        font = QFont()
        font.setFamilies([u"Azo Sans Medium"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: white;\n"
"")
        self.clear_button = QPushButton(self.upload_listing)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(250, 60, 51, 31))
        self.clear_button.setStyleSheet(u"background-color: white;\n"
"")
        self.tab_label_upload = QLabel(self.upload_listing)
        self.tab_label_upload.setObjectName(u"tab_label_upload")
        self.tab_label_upload.setGeometry(QRect(260, 20, 161, 16))
        font1 = QFont()
        font1.setPointSize(9)
        self.tab_label_upload.setFont(font1)
        self.tab_label_upload.setStyleSheet(u"color: white;")
        self.tabs.addTab(self.upload_listing, "")
        self.manage_shops = QWidget()
        self.manage_shops.setObjectName(u"manage_shops")
        self.tab_label_add_shop = QLabel(self.manage_shops)
        self.tab_label_add_shop.setObjectName(u"tab_label_add_shop")
        self.tab_label_add_shop.setGeometry(QRect(260, 20, 161, 16))
        self.tab_label_add_shop.setFont(font1)
        self.tab_label_add_shop.setStyleSheet(u"color: white;")
        self.title_2 = QLabel(self.manage_shops)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(10, 10, 241, 31))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"color: white;\n"
"")
        self.clear_button_2 = QPushButton(self.manage_shops)
        self.clear_button_2.setObjectName(u"clear_button_2")
        self.clear_button_2.setGeometry(QRect(250, 80, 51, 31))
        self.clear_button_2.setStyleSheet(u"background-color: white;\n"
"")
        self.user_input_shopname = QLineEdit(self.manage_shops)
        self.user_input_shopname.setObjectName(u"user_input_shopname")
        self.user_input_shopname.setGeometry(QRect(10, 160, 371, 21))
        self.user_input_shopname.setStyleSheet(u"background-color:white;\n"
"")
        self.upload_button_mockups = QPushButton(self.manage_shops)
        self.upload_button_mockups.setObjectName(u"upload_button_mockups")
        self.upload_button_mockups.setGeometry(QRect(10, 80, 231, 31))
        self.upload_button_mockups.setStyleSheet(u"background-color: white;\n"
"")
        self.selected_label_2 = QLabel(self.manage_shops)
        self.selected_label_2.setObjectName(u"selected_label_2")
        self.selected_label_2.setGeometry(QRect(310, 80, 71, 31))
        self.selected_label_2.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"")
        self.terminal_2 = QListWidget(self.manage_shops)
        self.terminal_2.setObjectName(u"terminal_2")
        self.terminal_2.setGeometry(QRect(390, 70, 371, 411))
        self.terminal_2.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"")
        self.upload_button_mockups_2 = QPushButton(self.manage_shops)
        self.upload_button_mockups_2.setObjectName(u"upload_button_mockups_2")
        self.upload_button_mockups_2.setGeometry(QRect(10, 120, 231, 31))
        self.upload_button_mockups_2.setStyleSheet(u"background-color: white;\n"
"")
        self.selected_label_3 = QLabel(self.manage_shops)
        self.selected_label_3.setObjectName(u"selected_label_3")
        self.selected_label_3.setGeometry(QRect(310, 120, 71, 31))
        self.selected_label_3.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"")
        self.user_input_shopname_2 = QLineEdit(self.manage_shops)
        self.user_input_shopname_2.setObjectName(u"user_input_shopname_2")
        self.user_input_shopname_2.setGeometry(QRect(10, 190, 371, 21))
        self.user_input_shopname_2.setStyleSheet(u"background-color:white;\n"
"")
        self.clear_button_3 = QPushButton(self.manage_shops)
        self.clear_button_3.setObjectName(u"clear_button_3")
        self.clear_button_3.setGeometry(QRect(250, 120, 51, 31))
        self.clear_button_3.setStyleSheet(u"background-color: white;\n"
"")
        self.shopname_label_2 = QLabel(self.manage_shops)
        self.shopname_label_2.setObjectName(u"shopname_label_2")
        self.shopname_label_2.setGeometry(QRect(10, 50, 201, 21))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.shopname_label_2.setFont(font2)
        self.shopname_label_2.setStyleSheet(u"color: white\n"
"")
        self.submit_button_2 = QPushButton(self.manage_shops)
        self.submit_button_2.setObjectName(u"submit_button_2")
        self.submit_button_2.setGeometry(QRect(10, 220, 371, 23))
        self.submit_button_2.setStyleSheet(u"background-color: gray;\n"
"")
        self.shopname_label_3 = QLabel(self.manage_shops)
        self.shopname_label_3.setObjectName(u"shopname_label_3")
        self.shopname_label_3.setGeometry(QRect(10, 260, 201, 21))
        self.shopname_label_3.setFont(font2)
        self.shopname_label_3.setStyleSheet(u"color: white\n"
"")
        self.user_input_shopname_3 = QLineEdit(self.manage_shops)
        self.user_input_shopname_3.setObjectName(u"user_input_shopname_3")
        self.user_input_shopname_3.setGeometry(QRect(10, 290, 191, 21))
        self.user_input_shopname_3.setStyleSheet(u"background-color:white;\n"
"")
        self.submit_button_3 = QPushButton(self.manage_shops)
        self.submit_button_3.setObjectName(u"submit_button_3")
        self.submit_button_3.setGeometry(QRect(210, 290, 171, 23))
        self.submit_button_3.setStyleSheet(u"background-color: gray;\n"
"")
        self.listView = QListView(self.manage_shops)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 320, 371, 161))
        self.shopname_label_4 = QLabel(self.manage_shops)
        self.shopname_label_4.setObjectName(u"shopname_label_4")
        self.shopname_label_4.setGeometry(QRect(390, 50, 181, 16))
        self.shopname_label_4.setStyleSheet(u"color: white\n"
"")
        self.tabs.addTab(self.manage_shops, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.pushButton = QPushButton(self.settings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 60, 91, 23))
        self.pushButton.setStyleSheet(u"background-color: white;\n"
"")
        self.title_3 = QLabel(self.settings)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 10, 241, 31))
        self.title_3.setFont(font)
        self.title_3.setStyleSheet(u"color: white;\n"
"")
        self.tab_label_settings = QLabel(self.settings)
        self.tab_label_settings.setObjectName(u"tab_label_settings")
        self.tab_label_settings.setGeometry(QRect(260, 20, 161, 16))
        self.tab_label_settings.setFont(font1)
        self.tab_label_settings.setStyleSheet(u"color: white;")
        self.label = QLabel(self.settings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 60, 91, 21))
        self.label.setStyleSheet(u"color: white\n"
"")
        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 60, 201, 21))
        self.label_2.setStyleSheet(u"color: white\n"
"")
        self.tabs.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Store.setText(QCoreApplication.translate("MainWindow", u"Add Store", None))
        self.action_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"Upload Design", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.user_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Theme: (e.g. Valentines or Christmas)", None))
        self.shopname_label.setText(QCoreApplication.translate("MainWindow", u"Shop Name", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"Toggle All", None))
        self.description.setPlainText("")
        self.selected_label.setText(QCoreApplication.translate("MainWindow", u"None Selected", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Make Bank Simulator", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tab_label_upload.setText(QCoreApplication.translate("MainWindow", u">>   Upload Listing", None))
        self.tabs.setTabText(self.tabs.indexOf(self.upload_listing), QCoreApplication.translate("MainWindow", u"Upload Listing", None))
        self.tab_label_add_shop.setText(QCoreApplication.translate("MainWindow", u">>   Manage Shops", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Make Bank Simulator", None))
        self.clear_button_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.user_input_shopname.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Shop Name: (e.g. customizedblankets4u)", None))
        self.upload_button_mockups.setText(QCoreApplication.translate("MainWindow", u"Upload Mockups", None))
        self.selected_label_2.setText(QCoreApplication.translate("MainWindow", u"None Selected", None))
        self.upload_button_mockups_2.setText(QCoreApplication.translate("MainWindow", u"Upload Supporting Images", None))
        self.selected_label_3.setText(QCoreApplication.translate("MainWindow", u"None Selected", None))
        self.user_input_shopname_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Product Type: (e.g. blankets, phone cases, puzzles)", None))
        self.clear_button_3.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.shopname_label_2.setText(QCoreApplication.translate("MainWindow", u"Add Shop:", None))
        self.submit_button_2.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.shopname_label_3.setText(QCoreApplication.translate("MainWindow", u"Remove Shop:", None))
        self.user_input_shopname_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Shop Name: (e.g. customizedblankets4u)", None))
        self.submit_button_3.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.shopname_label_4.setText(QCoreApplication.translate("MainWindow", u"Shop List:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.manage_shops), QCoreApplication.translate("MainWindow", u"Manage Shops", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save To", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Make Bank Simulator", None))
        self.tab_label_settings.setText(QCoreApplication.translate("MainWindow", u">>   Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Directory:", None))
        self.label_2.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

