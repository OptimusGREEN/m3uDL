# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import logging
import urllib.request

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

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def _validate_url(self, url):
        code = urllib.request.urlopen(url).getcode()
        if code == 200:
            return True
        logging.debug("{}: {}".format(code, type(code)))
        return


    @Slot()
    def _search(self):
        search_str = self.ui.lineEdit_search.text()
        m3u = self.ui.lineEdit_url.text()
        results = []
        if not self._validate_url(m3u):
            raise Exception("invalid m3u url")
        with open(r"{}".format(m3u), 'r') as fp:
            url_line_no = None
            current_dict = {}
            for l_no, line in enumerate(fp):
                if url_line_no == l_no:
                    current_dict["url"] = line.strip()
                    results.append(current_dict)
                    url_line_no = None
                    current_dict = {}
                    continue
                if search_str in line.lower():
                    split1 = line.split('tvg-name="')[1]
                    split2 = split1.split('" tvg-logo="')
                    logo = split2[1].split('" ')[0]
                    title = split2[0]
                    current_dict["title"] = title
                    current_dict["logo"] = logo
                    url_line_no = l_no + 1
        return results

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
