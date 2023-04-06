 # This code is courtesy of:
 # https://pythonassets.com/posts/download-file-with-progress-bar-pyqt-pyside/

from urllib.request import urlopen

from PySide6.QtCore import QThread, Signal

class Downloader(QThread):

    # Signal for the window to establish the maximum value
    # of the progress bar.
    setTotalProgress = Signal(int)
    # Signal to increase the progress.
    setCurrentProgress = Signal(int)
    # Signal to be emitted when the file has been downloaded successfully.
    succeeded = Signal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        readBytes = 0
        chunkSize = 1024
        # Open the URL address.
        with urlopen(self._url) as r:
            # Tell the window the amount of bytes to be downloaded.
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(self._filename, "ab") as f:
                while True:
                    # Read a piece of the file we are downloading.
                    chunk = r.read(chunkSize)
                    # If the result is `None`, that means data is not
                    # downloaded yet. Just keep waiting.
                    if chunk is None:
                        continue
                    # If the result is an empty `bytes` instance, then
                    # the file is complete.
                    elif chunk == b"":
                        break
                    # Write into the local file the downloaded chunk.
                    f.write(chunk)
                    readBytes += chunkSize
                    # Tell the window how many bytes we have received.
                    self.setCurrentProgress.emit(readBytes)
        # If this line is reached then no exception has ocurred in
        # the previous lines.
        self.succeeded.emit()

