import sys
import requests
from PySide6.QtGui import QPixmap

def noImage():
    # return "https://st3.depositphotos.com/1037178/12744/v/600/depositphotos_127449166-stock-illustration-picture-icon-vector.jpg"
    return "https://unsplash.com/photos/qGbo4o77NaM/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTJ8fG1vdmllc3xlbnwwfHx8fDE2ODA4NzY1MDY&force=true&w=640"

def imageFromUrl(url, *args, **kwargs):
    pixmap = QPixmap()
    request = requests.get(url)
    code = request.status_code
    print("Status Code: ", code, " - type: ", type(code))
    if not code == 200:
        request = requests.get(noImage())
    pixmap.loadFromData(request.content)
    return pixmap

