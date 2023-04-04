import sys
import requests
from PySide6.QtGui import QPixmap, QScreen
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class imageBox(QLabel):
    def __init__(self, image_file=None, url=None, *args, **kwargs):
        super(imageBox, self).__init__()

        # self.setScaledContents(True)

        self.pixmap = QPixmap()
        if url:
            request = requests.get(url)
            self.pixmap.loadFromData(request.content)
            self.pixmap.scaled(self.size().width(),self.size().height())
            self.setPixmap(self.pixmap)
        elif image_file:
            self.pixmap.loadFromData(image_file)
            self.setPixmap(self.pixmap)
        else:
            pass

def imageFromUrl(url, *args, **kwargs):
    pixmap = QPixmap()
    request = requests.get(url)
    pixmap.loadFromData(request.content)
    return pixmap