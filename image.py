import sys
import requests
from PySide6.QtGui import QPixmap

def imageFromUrl(url, *args, **kwargs):
    pixmap = QPixmap()
    request = requests.get(url)
    pixmap.loadFromData(request.content)
    return pixmap

def noImage():
    return "https://st3.depositphotos.com/1037178/12744/v/600/depositphotos_127449166-stock-illustration-picture-icon-vector.jpg"