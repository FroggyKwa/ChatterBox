from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QLabel, QApplication, QPushButton


def check_valid_login(ln):
    import re
    flag = 0
    if len(ln) < 3:
        flag = -1
    elif re.search('\s', ln):
        flag = -1
    if flag == -1:
        return 'Login must be longer than two characters and must not contain whitespace characters'


def check_valid_password(ps):
    import re
    flag = 0
    if len(ps) < 6:
        flag = -1
    elif not re.search("[a-z]", ps):
        flag = -1
    elif not re.search("[0-9]", ps):
        flag = -1
    elif re.search("\s", ps):
        flag = -1
    if flag == -1:
        return 'Password must be at least 6 characters and contain both letters and numbers'

class SignUpForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(268, 275)
        self.setWindowTitle('Sign up')
        self.login_ln = QLineEdit(self)
        self.login_ln.setGeometry(QRect(40, 70, 191, 20))

        self.password_ln = QLineEdit(self)
        self.password_ln.setGeometry(QRect(40, 120, 191, 20))
        self.password_ln.setEchoMode(QLineEdit.Password)

        self.confirm_password_ln = QLineEdit(self)
        self.confirm_password_ln.setGeometry(QRect(40, 170, 191, 20))
        self.confirm_password_ln.setEchoMode(QLineEdit.Password)

        self.error_label = QLabel(self)
        self.error_label.setWordWrap(True)
        self.error_label.setGeometry(QRect(10, 10, 200, 40))

        self.label1 = QLabel(self)
        self.label1.setText('Login')
        self.label1.setGeometry(QRect(40, 50, 47, 13))

        self.label_2 = QLabel(self)
        self.label_2.setText('Password')
        self.label_2.setGeometry(QRect(40, 100, 47, 13))

        self.label_3 = QLabel(self)
        self.label_3.resize(self.label_3.size())
        self.label_3.setText('Confirm')
        self.label_3.setGeometry(QRect(40, 150, 47, 13))

        self.submit_btn = QPushButton(self)
        self.submit_btn.move(90, 220)
        self.submit_btn.setText('Sign Up')
