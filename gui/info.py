from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox


class InfoForm(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, EditForm):
        EditForm.setObjectName("EditForm")
        EditForm.resize(639, 442)
        self.setWindowTitle('Info')
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.combo = QComboBox(self)
        self.combo.move(225, 20)
        self.combo.resize(200, 25)
        self.combo.addItem('Select User')

        self.info_label = QLabel(self)
        self.info_label.resize(639, 442)
        self.info_label.move(35, 35)
