from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class ChatterBox(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/MainForm.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatterBox()
    sys.exit(app.exec_())
