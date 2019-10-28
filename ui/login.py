from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QLabel, QApplication, QPushButton


class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(268, 213)
        self.password_ln = QLineEdit(self)
        self.password_ln.setGeometry(QRect(40, 100, 191, 20))
        self.password_ln.setEchoMode(QLineEdit.Password)
        self.login_ln = QLineEdit(self)
        self.login_ln.setGeometry(QRect(40, 50, 191, 20))
        self.label1 = QLabel(self)
        self.label1.setText('Login')
        self.label1.setGeometry(QRect(40, 30, 47, 13))
        self.label_2 = QLabel(self)
        self.label_2.setText('Password')
        self.label_2.setGeometry(QRect(40, 80, 47, 13))
        self.submit_btn = QPushButton(self)
        self.submit_btn.move(90, 140)
        self.submit_btn.setText('Sign In')

    def login(self):
        login = self.login_ln.text()
        password = self.login_ln.text()

