import sys
sys.path.append('../')
from ui.MainForm import *


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ChatterBox()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
