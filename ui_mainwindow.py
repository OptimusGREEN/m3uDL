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
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(u"m3uDL")
        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 471, 211))
        self.label_search = QLabel(self.groupBox)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setGeometry(QRect(20, 57, 90, 16))
        self.lineEdit_download_path = QLineEdit(self.groupBox)
        self.lineEdit_download_path.setObjectName(u"lineEdit_download_path")
        self.lineEdit_download_path.setGeometry(QRect(133, 90, 301, 21))
        self.lineEdit_download_path.setFocusPolicy(Qt.ClickFocus)
        self.label_url = QLabel(self.groupBox)
        self.label_url.setObjectName(u"label_url")
        self.label_url.setGeometry(QRect(20, 24, 25, 16))
        self.lineEdit_url = QLineEdit(self.groupBox)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        self.lineEdit_url.setGeometry(QRect(133, 24, 301, 21))
        self.lineEdit_url.setFocusPolicy(Qt.StrongFocus)
        self.label_download_path = QLabel(self.groupBox)
        self.label_download_path.setObjectName(u"label_download_path")
        self.label_download_path.setGeometry(QRect(20, 90, 101, 16))
        self.lineEdit_search = QLineEdit(self.groupBox)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(133, 57, 301, 21))
        self.lineEdit_search.setFocusPolicy(Qt.ClickFocus)
        self.toolButton_download_path = QToolButton(self.groupBox)
        self.toolButton_download_path.setObjectName(u"toolButton_download_path")
        self.toolButton_download_path.setGeometry(QRect(440, 90, 26, 22))
        self.pushButton_search = QPushButton(self.groupBox)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(210, 127, 100, 32))
        self.progressBar_search = QProgressBar(self.groupBox)
        self.progressBar_search.setObjectName(u"progressBar_search")
        self.progressBar_search.setEnabled(True)
        self.progressBar_search.setGeometry(QRect(200, 157, 118, 23))
        self.progressBar_search.setMaximum(0)
        self.progressBar_search.setValue(-1)
        self.progressBar_search.setTextVisible(False)
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(490, 20, 301, 561))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 299, 559))
        self.listWidget_results = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_results.setObjectName(u"listWidget_results")
        self.listWidget_results.setGeometry(QRect(0, 0, 301, 561))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QGroupBox(MainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 240, 471, 341))
        self.pushButton_download = QPushButton(self.groupBox_2)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.setGeometry(QRect(300, 200, 100, 32))
        self.pushButton_download.setAutoFillBackground(False)
        self.label_selected_title = QLabel(self.groupBox_2)
        self.label_selected_title.setObjectName(u"label_selected_title")
        self.label_selected_title.setGeometry(QRect(250, 39, 201, 71))
        self.label_selected_title.setAlignment(Qt.AlignCenter)
        self.label_selected_title.setWordWrap(True)
        self.label_art = QLabel(self.groupBox_2)
        self.label_art.setObjectName(u"label_art")
        self.label_art.setGeometry(QRect(17, 15, 200, 300))
        self.progressBar_dl = QProgressBar(self.groupBox_2)
        self.progressBar_dl.setObjectName(u"progressBar_dl")
        self.progressBar_dl.setGeometry(QRect(250, 280, 201, 23))
        self.progressBar_dl.setValue(0)
        self.label_dl_status = QLabel(self.groupBox_2)
        self.label_dl_status.setObjectName(u"label_dl_status")
        self.label_dl_status.setGeometry(QRect(250, 250, 201, 20))
        self.label_dl_status.setAlignment(Qt.AlignCenter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.groupBox.setTitle("")
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search Phrase", None))
        self.lineEdit_download_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"~/Downloads", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lineEdit_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://myurl.com/myfile.m3u", None))
        self.label_download_path.setText(QCoreApplication.translate("MainWindow", u"Download Path", None))
        self.toolButton_download_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_2.setTitle("")
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.label_selected_title.setText(QCoreApplication.translate("MainWindow", u"title here", None))
        self.label_art.setText("")
        self.label_dl_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        pass
    # retranslateUi

