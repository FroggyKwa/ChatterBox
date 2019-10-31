from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QLabel, QApplication, QPushButton


def check_valid(ln: QLineEdit):
    if ln.isspace() or not ln:
        return False
    return True


class SignUpForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(268, 275)
        self.login_ln = QLineEdit(self)
        self.login_ln.setGeometry(QRect(40, 50, 191, 20))

        self.password_ln = QLineEdit(self)
        self.password_ln.setGeometry(QRect(40, 100, 191, 20))
        self.password_ln.setEchoMode(QLineEdit.Password)

        self.confirm_password_ln = QLineEdit(self)
        self.confirm_password_ln.setGeometry(QRect(40, 150, 191, 20))
        self.confirm_password_ln.setEchoMode(QLineEdit.Password)

        self.label1 = QLabel(self)
        self.label1.setText('Login')
        self.label1.setGeometry(QRect(40, 30, 47, 13))

        self.label_2 = QLabel(self)
        self.label_2.setText('Password')
        self.label_2.setGeometry(QRect(40, 80, 47, 13))

        self.label_3 = QLabel(self)
        self.label_3.resize(self.label_3.size())
        self.label_3.setText('Confirm')
        self.label_3.setGeometry(QRect(40, 130, 47, 13))

        self.submit_btn = QPushButton(self)
        self.submit_btn.move(90, 200)
        self.submit_btn.setText('Sign Up')
