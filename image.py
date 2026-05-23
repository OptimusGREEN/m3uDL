import sys
import requests
from PySide6.QtGui import QPixmap

def noImage():
    # return "https://st3.depositphotos.com/1037178/12744/v/600/depositphotos_127449166-stock-illustration-picture-icon-vector.jpg"
    return "https://unsplash.com/photos/qGbo4o77NaM/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTJ8fG1vdmllc3xlbnwwfHx8fDE2ODA4NzY1MDY&force=true&w=640"

def imageFromUrl(url, *args, **kwargs):
    pixmap = QPixmap()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        request = requests.get(url, headers=headers, timeout=10, verify=False)
        code = request.status_code
    except Exception as e:
        print("Error fetching image: ", e)
        code = None

    print("Status Code: ", code, " - type: ", type(code))
    if not code == 200:
        try:
            request = requests.get(noImage(), headers=headers, timeout=10, verify=False)
        except Exception as e:
            print("Error fetching fallback image: ", e)
            return pixmap
    pixmap.loadFromData(request.content)
    return pixmap

