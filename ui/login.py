from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QDialog


class LoginForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(268, 213)
        self.setWindowTitle('Sign in')
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.login_ln = QLineEdit(self)
        self.login_ln.setGeometry(QRect(40, 50, 191, 20))

        self.password_ln = QLineEdit(self)
        self.password_ln.setGeometry(QRect(40, 100, 191, 20))
        self.password_ln.setEchoMode(QLineEdit.Password)

        self.label1 = QLabel(self)
        self.label1.setText('Login')
        self.label1.setGeometry(QRect(40, 30, 47, 13))

        self.label_2 = QLabel(self)
        self.label_2.setText('Password')
        self.label_2.setGeometry(QRect(40, 80, 47, 13))

        self.submit_btn = QPushButton(self)
        self.submit_btn.move(90, 140)
        self.submit_btn.setText('Sign In')

        self.error_label = QLabel(self)
        self.error_label.setGeometry(10, 10, 100, 50)
        self.error_label.setWordWrap(True)
