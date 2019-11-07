from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QComboBox


class InfoForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(self)

    def initUI(self, EditForm):
        EditForm.setObjectName("EditForm")
        EditForm.resize(639, 442)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.combo = QComboBox(self)
        self.combo.move(225, 20)
        self.combo.resize(200, 25)
        self.combo.addItem('Select User')

        self.info_label = QLabel(self)
        self.info_label.resize(639, 442)
        self.info_label.move(35, 35)
