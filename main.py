# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

        self.dl_dir = "~/Downloads"

        self.ui.pushButton_search.clicked.connect(self._search)
        self.ui.lineEdit_download_path.textChanged.connect(self._set_dl)
        # self.ui.lineEdit_url.setFocus()

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def _search(self):
        print(self.ui.lineEdit_search.text())

    @Slot()
    def _set_dl(self):
        if self.ui.lineEdit_download_path.text():
            self.dl_dir = self.ui.lineEdit_download_path.text()
        print("Download path set to: {}".format(self.dl_dir))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
