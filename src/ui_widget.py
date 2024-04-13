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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 524)
        MainWindow.setStyleSheet(u"background-color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 181, 31))
        font = QFont()
        font.setFamilies([u"Azo Sans Medium"])
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: white;")
        self.upload_button = QPushButton(self.centralwidget)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setGeometry(QRect(10, 50, 231, 23))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        self.upload_button.setFont(font1)
        self.upload_button.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: black;")
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(250, 50, 51, 23))
        self.clear_button.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: black;")
        self.selected_label = QLabel(self.centralwidget)
        self.selected_label.setObjectName(u"selected_label")
        self.selected_label.setGeometry(QRect(310, 53, 81, 20))
        self.selected_label.setStyleSheet(u"color: rgb(170, 0, 0)")
        self.user_input = QLineEdit(self.centralwidget)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(10, 80, 371, 21))
        self.user_input.setStyleSheet(u"color: white;")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 371, 311))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.shopname_label = QLabel(self.gridLayoutWidget)
        self.shopname_label.setObjectName(u"shopname_label")
        self.shopname_label.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.shopname_label, 0, 0, 1, 1)

        self.description_label = QLabel(self.gridLayoutWidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.description_label, 0, 1, 1, 1)

        self.shopname_list = QListWidget(self.gridLayoutWidget)
        self.shopname_list.setObjectName(u"shopname_list")
        self.shopname_list.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.shopname_list, 1, 0, 1, 1)

        self.toggle_button = QPushButton(self.gridLayoutWidget)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: black;\n"
"\n"
"")

        self.gridLayout.addWidget(self.toggle_button, 2, 0, 1, 1)

        self.description = QPlainTextEdit(self.gridLayoutWidget)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.description, 1, 1, 2, 1)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(10, 430, 371, 23))
        self.submit_button.setStyleSheet(u"background-color: gray;\n"
"color: black;")
        self.action_label = QLabel(self.centralwidget)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setGeometry(QRect(10, 460, 101, 16))
        self.action_label.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.terminal = QListWidget(self.centralwidget)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setGeometry(QRect(390, 50, 371, 421))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"bankSimulator", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"Upload Design", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.selected_label.setText(QCoreApplication.translate("MainWindow", u"0 Selected.", None))
        self.user_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Theme: (e.g. Valentines or Christmas)", None))
        self.shopname_label.setText(QCoreApplication.translate("MainWindow", u"Shop Names:", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Descriptions:", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"Toggle All", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.action_label.setText("")
    # retranslateUi

