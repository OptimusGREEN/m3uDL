# This Python file uses the following encoding: utf-8
import os
import sys
import logging
import re
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, url2pathname, urlopen

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, QRunnable, QThreadPool, Qt, QSettings
from ui_mainwindow import Ui_MainWindow

from listitem import ListItem
from image import imageFromUrl, noImage
from downloader import Downloader
from parser import getID, getLogo, getTitle

home_directory = os.path.expanduser( '~' )

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()  # QtCore.Slot
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 600)
        self.threadpool = QThreadPool()
        self.settings = QSettings("OptimusGREEN", "m3uDL")
        self.dl_dir = os.path.join(home_directory, "Downloads")

        self.load_ui()
        self._load_persisted_inputs()
        self.ui.progressBar_search.setVisible(False)
        self.ui.groupBox_2.setVisible(False)
        self.ui.progressBar_dl.setVisible(False)
        self.ui.label_dl_status.setVisible(False)

        self.ui.pushButton_search.clicked.connect(self._search)
        self.ui.lineEdit_download_path.textChanged.connect(self._set_dl)
        self.ui.lineEdit_url.textChanged.connect(self._save_url)
        self.ui.lineEdit_search.textChanged.connect(self._save_search)
        self.ui.toolButton_download_path.clicked.connect(self._browse_dl)
        self.ui.listWidget_results.currentItemChanged.connect(self.printItemData)
        self.ui.listWidget_results.currentItemChanged.connect(self.showSelection)
        self.ui.pushButton_download.clicked.connect(self._download)

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Adjust geometry of existing widgets to make room for Xtream Codes inputs
        self.ui.groupBox.setFixedHeight(230)
        self.ui.groupBox_2.setGeometry(10, 260, 471, 320)
        self.ui.label_url.setGeometry(20, 35, 25, 16)
        self.ui.lineEdit_url.setGeometry(133, 35, 301, 21)
        self.ui.label_search.setGeometry(20, 65, 90, 16)
        self.ui.lineEdit_search.setGeometry(133, 65, 301, 21)
        self.ui.label_download_path.setGeometry(20, 95, 101, 16)
        self.ui.lineEdit_download_path.setGeometry(133, 95, 301, 21)
        self.ui.toolButton_download_path.setGeometry(440, 95, 26, 22)
        
        # Move search button and progress bar
        self.ui.pushButton_search.setGeometry(210, 160, 100, 32)
        self.ui.progressBar_search.setGeometry(200, 195, 118, 23)
        
        # Add Radio Buttons for Mode Selection
        from PySide6.QtWidgets import QRadioButton, QButtonGroup, QLineEdit, QLabel
        
        self.radio_m3u = QRadioButton("M3U URL", self.ui.groupBox)
        self.radio_m3u.setGeometry(133, 8, 90, 20)
        self.radio_m3u.setChecked(True)
        
        self.radio_xtream = QRadioButton("Xtream API", self.ui.groupBox)
        self.radio_xtream.setGeometry(240, 8, 120, 20)
        
        self.source_group = QButtonGroup(self)
        self.source_group.addButton(self.radio_m3u)
        self.source_group.addButton(self.radio_xtream)
        
        # Add Username and Password widgets
        self.label_username = QLabel("Username", self.ui.groupBox)
        self.label_username.setGeometry(20, 125, 80, 16)
        self.lineEdit_username = QLineEdit(self.ui.groupBox)
        self.lineEdit_username.setGeometry(133, 125, 120, 21)
        self.lineEdit_username.setPlaceholderText("username")
        
        self.label_password = QLabel("Password", self.ui.groupBox)
        self.label_password.setGeometry(265, 125, 60, 16)
        self.lineEdit_password = QLineEdit(self.ui.groupBox)
        self.lineEdit_password.setGeometry(325, 125, 109, 21)
        self.lineEdit_password.setPlaceholderText("password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        
        # Hide Xtream widgets by default
        self.label_username.hide()
        self.lineEdit_username.hide()
        self.label_password.hide()
        self.lineEdit_password.hide()
        
        # Connect toggle signals
        self.radio_m3u.toggled.connect(self._toggle_mode)

    def _toggle_mode(self):
        from PySide6.QtWidgets import QLineEdit
        if self.radio_m3u.isChecked():
            self.ui.label_url.setText("URL")
            self.ui.lineEdit_url.setPlaceholderText("http://myurl.com/myfile.m3u")
            self.label_username.hide()
            self.lineEdit_username.hide()
            self.label_password.hide()
            self.lineEdit_password.hide()
        else:
            self.ui.label_url.setText("Host")
            self.ui.lineEdit_url.setPlaceholderText("http://myhost.com:8080")
            self.label_username.show()
            self.lineEdit_username.show()
            self.label_password.show()
            self.lineEdit_password.show()

    def _validate_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            logging.debug("Invalid URL format: %s", url)
            return False

        request = Request(url, headers={"User-Agent": "m3uDL/1.0"})
        try:
            code = urlopen(request).getcode()
        except HTTPError as exc:
            code = exc.code
        except URLError as exc:
            logging.debug("Validation request failed: %s", exc)
            return False

        if 200 <= code < 400:
            return True
        logging.debug("{}: {}".format(code, type(code)))
        return False

    def _populate_results(self, results):
        pass
        for i in results:
            title = i.get('title')
            item = ListItem(self.ui.listWidget_results)
            item.setText(title)
            item.setUrl(i.get('url'))
            item.setLogo(i.get('logo'))
            self.ui.listWidget_results.addItem(item)

        # for i in results:
        #     txt = i.get('title')
        #     link = i.get('url')
        #     item = QListWidgetItem(self.ui.listWidget_results)
        #     item.setText(txt)
        #     self.ui.listWidget_results.addItem(item)

    def printItemData(self, *args, **kwargs):
        if not self.ui.listWidget_results.currentItem():
            return
        print(self.ui.listWidget_results.currentRow())
        print(self.ui.listWidget_results.currentItem().text())
        print(self.ui.listWidget_results.currentItem().url)

    def showSelection(self, *args, **kwargs):
        if not self.ui.listWidget_results.currentItem():
            return
        self.ui.label_selected_title.setText(self.ui.listWidget_results.currentItem().text())
        pixmap = imageFromUrl(url=self.ui.listWidget_results.currentItem().logo)
        pixmap = pixmap.scaled(self.ui.label_art.width(), self.ui.label_art.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_art.setPixmap(pixmap)
        self.ui.groupBox_2.setVisible(True)

    @Slot()
    def _download(self, *args, **kwargs):
        self.ui.label_dl_status.setText("Downloading file...")
        self.ui.pushButton_download.setEnabled(False)
        self.ui.progressBar_dl.setValue(0)
        self.ui.progressBar_dl.setVisible(True)
        self.ui.label_dl_status.setVisible(True)
        title = self.ui.listWidget_results.currentItem().text()
        url = self.ui.listWidget_results.currentItem().url
        ext = os.path.splitext(url)[-1]
        out_file = "{}{}".format(title, ext)
        dl_path = os.path.join(self.dl_dir, out_file)
        self.downloader = Downloader(url, dl_path)
        self.downloader.setTotalProgress.connect(self.ui.progressBar_dl.setMaximum)
        self.downloader.setCurrentProgress.connect(self.ui.progressBar_dl.setValue)
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()

    def downloadSucceeded(self):
        # Set the progress at 100%.
        self.ui.progressBar_dl.setValue(self.ui.progressBar_dl.maximum())
        self.ui.label_dl_status.setText("The file has been downloaded!")

    def downloadFinished(self):
        # Restore the button.
        self.ui.pushButton_download.setEnabled(True)
        # Delete the thread when no longer needed.
        del self.downloader

    @Slot()
    def _search(self):
        search_str = self.ui.lineEdit_search.text()
        url = self.ui.lineEdit_url.text()
        if self.radio_xtream.isChecked():
            host = url.rstrip('/')
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()
            url = f"{host}/get.php?username={username}&password={password}&type=m3u_plus&output=ts"
        m3u = os.path.join(self.dl_dir, "tmp", "tmp.m3u")
        def run():
            # self.ui.progressBar_search.setVisible(True)
            if not os.path.exists(os.path.join(self.dl_dir, "tmp")):
                os.makedirs(os.path.join(self.dl_dir, "tmp"))
            request = Request(url, headers={"User-Agent": "m3uDL/1.0"})
            with urlopen(request) as response, open(m3u, "wb") as playlist_file:
                playlist_file.write(response.read())
            results = []
            with open(r"{}".format(m3u), 'r') as fp:
                url_line_no = None
                current_dict = {}
                for l_no, line in enumerate(fp):
                    if url_line_no == l_no:
                        u = re.sub(r'^.*?http', 'http', line)
                        dlurl = u.strip()
                        current_dict["url"] = dlurl
                        results.append(current_dict)
                        print("URL: ", dlurl)
                        url_line_no = None
                        current_dict = {}
                        continue
                    if search_str.lower() in line.lower():
                        print(line)
                        try:
                            title = getTitle(line)
                            print("Title: ", title)
                        except:
                            title = getID(line)
                            print("Title: ", title)
                        logo = getLogo(line)
                        print("Logo: ", logo)
                        current_dict["title"] = title
                        current_dict["logo"] = logo
                        url_line_no = l_no + 1


            print("Total Results: ", len(results))
            if len(results) < 1:
                restxt = "No results found."
                self._populate_results([{"title": restxt,
                                         "logo": noImage(),
                                         "url": ""}])
                self.ui.progressBar_search.setVisible(False)
                self.ui.pushButton_search.setEnabled(True)
            else:
                for r in results:
                    logging.debug(r)
                self._populate_results(results)
                self.ui.progressBar_search.setVisible(False)
                self.ui.pushButton_search.setEnabled(True)

        #### Start Here ####
        self.ui.listWidget_results.clear()
        self.ui.progressBar_search.setVisible(True)
        self.ui.pushButton_search.setEnabled(False)
        if not len(self.ui.lineEdit_search.text()) > 1:
            print("search too short")
            d = QMessageBox()
            d.setText("Insufficient Search Criteria")
            d.exec()
            self.ui.progressBar_search.setVisible(False)
            self.ui.pushButton_search.setEnabled(True)
        elif not self._validate_url(url):
            print("invalid url: {}".format(url))
            d = QMessageBox()
            d.setText("URL seems invalid, Please check and try again.\nurl: {} ".format(url))
            d.exec()
            self.ui.progressBar_search.setVisible(False)
            self.ui.pushButton_search.setEnabled(True)
        else:
            worker = Worker(run)
            self.threadpool.start(worker)


    @Slot()
    def _set_dl(self, dl_dir=None):
        if dl_dir and isinstance(dl_dir, str):
            dl_dir = self._normalize_dl_dir(dl_dir)
        elif dl_dir is not None and not isinstance(dl_dir, str):
            dl_dir = str(dl_dir)

        if not dl_dir:
            dl_dir = self.ui.lineEdit_download_path.text()
        if not dl_dir:
            dl_dir = self.dl_dir

        if self.ui.lineEdit_download_path.text() != dl_dir:
            self.ui.lineEdit_download_path.setText(dl_dir)
        self.dl_dir = dl_dir
        self.settings.setValue("download_path", self.dl_dir)
        print("Download path set to: {}".format(self.dl_dir))

    def _normalize_dl_dir(self, dl_dir):
        if dl_dir and isinstance(dl_dir, str):
            parsed_dl_dir = urlparse(dl_dir)
            if parsed_dl_dir.scheme == "file":
                path = unquote(parsed_dl_dir.path or "")
                if parsed_dl_dir.netloc:
                    path = "//{}{}".format(parsed_dl_dir.netloc, path)
                path = url2pathname(path)
                if os.name == "nt" and re.match(r"^/[A-Za-z]:", path):
                    path = path[1:]
                return path or dl_dir
        return dl_dir

    @Slot()
    def _save_url(self, url):
        self.settings.setValue("url", url)

    @Slot()
    def _save_search(self, search):
        self.settings.setValue("search", search)

    def _load_persisted_inputs(self):
        saved_url = self.settings.value("url", "", type=str)
        saved_search = self.settings.value("search", "", type=str)
        saved_download_path = self.settings.value("download_path", self.dl_dir, type=str)
        self.ui.lineEdit_url.setText(saved_url)
        self.ui.lineEdit_search.setText(saved_search)
        self._set_dl(saved_download_path)

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
