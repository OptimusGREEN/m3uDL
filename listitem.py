from PySide6.QtWidgets import QListWidgetItem

class ListItem(QListWidgetItem):
    def __init__(self, *args, **kwargs):
        super(ListItem, self).__init__()

        self.title = None
        self.url = None
        self.logo = None
    def setTitle(self, title):
        self.title = title

    def setUrl(self, url):
        self.url = url

    def setLogo(self, logo):
        self.logo = logo

