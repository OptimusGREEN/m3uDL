# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QScrollBar, QSizePolicy, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(u"m3uDL")
        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 471, 231))
        self.label_search = QLabel(self.groupBox)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setGeometry(QRect(10, 100, 90, 16))
        self.lineEdit_download_path = QLineEdit(self.groupBox)
        self.lineEdit_download_path.setObjectName(u"lineEdit_download_path")
        self.lineEdit_download_path.setGeometry(QRect(123, 133, 301, 21))
        self.lineEdit_download_path.setFocusPolicy(Qt.ClickFocus)
        self.label_url = QLabel(self.groupBox)
        self.label_url.setObjectName(u"label_url")
        self.label_url.setGeometry(QRect(10, 67, 25, 16))
        self.lineEdit_url = QLineEdit(self.groupBox)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        self.lineEdit_url.setGeometry(QRect(123, 67, 301, 21))
        self.lineEdit_url.setFocusPolicy(Qt.StrongFocus)
        self.label_download_path = QLabel(self.groupBox)
        self.label_download_path.setObjectName(u"label_download_path")
        self.label_download_path.setGeometry(QRect(10, 133, 101, 16))
        self.lineEdit_search = QLineEdit(self.groupBox)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(123, 100, 301, 21))
        self.lineEdit_search.setFocusPolicy(Qt.ClickFocus)
        self.toolButton_download_path = QToolButton(self.groupBox)
        self.toolButton_download_path.setObjectName(u"toolButton_download_path")
        self.toolButton_download_path.setGeometry(QRect(430, 133, 26, 22))
        self.pushButton_search = QPushButton(self.groupBox)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(200, 170, 100, 32))
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(490, 17, 281, 511))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 279, 509))
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 281, 511))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalScrollBar = QScrollBar(MainWindow)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(780, 20, 16, 511))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fill in the blanks", None))
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search Phrase", None))
        self.lineEdit_download_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"~/Downloads", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lineEdit_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://myurl.com/myfile.m3u", None))
        self.label_download_path.setText(QCoreApplication.translate("MainWindow", u"Download Path", None))
        self.toolButton_download_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        pass
    # retranslateUi

