# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

        self.dl_dir = "~/Downloads"

        self.ui.pushButton_search.clicked.connect(self._search)
        self.ui.lineEdit_download_path.textChanged.connect(self._set_dl)
        self.ui.toolButton_download_path.clicked.connect(self._browse_dl)
        # self.ui.lineEdit_search.textChange.connect(self._search)
        # self.ui.lineEdit_url.setFocus()

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def _search(self):
        print(self.ui.lineEdit_search.text())

    @Slot()
    def _set_dl(self, dl_dir=None):
        if not dl_dir:
            if self.ui.lineEdit_download_path.text():
                self.dl_dir = self.ui.lineEdit_download_path.text()
        else:
            self.ui.lineEdit_download_path.setText(dl_dir)
            self.dl_dir = dl_dir
        print("Download path set to: {}".format(self.dl_dir))

    @Slot()
    def _browse_dl(self):
        dialog = QFileDialog(self, directory="~")
        dialog.setWindowTitle("Select Download Directory")
        selection = dialog.getExistingDirectory()
        self._set_dl(selection)
        # print(selection)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
