import sys
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver
from ui.MainForm import ChatterBox
from hashlib import md5
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.signup import check_valid


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.client = self

    def lineReceived(self, line: bytes):
        message = line.decode()
        self.factory.window.messages_history_plain_text.appendPlainText(message)

    def send_message(self, message):
        self.sendLine(message.encode())


class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol = Client

    def __init__(self, app_window):
        self.window = app_window


class ChatWindow(QMainWindow, ChatterBox):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.client = Client()
        self.reactor = None
        self.send_btn.pressed.connect(self.send_message)
        self.login_form.submit_btn.pressed.connect(self.login_user)
        self.reg_form.submit_btn.pressed.connect(self.create_user)
        self.login = None

    def keyPressEvent(self, event):
        from PyQt5.QtCore import Qt
        if event.key == Qt.Key_Enter:
            self.send_message()

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)

    def send_message(self, message=None):
        if message:
            self.client.send_message(self.login + '::' + message)
        else:
            if not self.messagebox_text_edit.toPlainText().isspace():
                message = self.messagebox_text_edit.toPlainText()
                self.client.send_message(self.login + '::' + message)
                self.messagebox_text_edit.clear()
            else:
                return

    def create_user(self):
        login = self.reg_form.login_ln.text()
        password = self.reg_form.password_ln.text()
        confirm = self.reg_form.confirm_password_ln.text()
        if check_valid(login) and check_valid(password) and password == confirm:
            self.login = login
            self.send_message(f'/register {login} {md5(password.encode()).hexdigest()}')
            self.current_user_lbl.setText(login)

    def login_user(self):
        login = self.login_form.login_ln.text()
        password = self.login_form.password_ln.text()
        if check_valid(login) and check_valid(password):
            self.login = login
            self.send_message(f'/login {login} {md5(password.encode()).hexdigest()}')


app = QApplication(sys.argv)
import qt5reactor

window = ChatWindow()
window.show()
qt5reactor.install()
from twisted.internet import reactor

reactor.connectTCP("localhost", 7411, Connector(window))
window.reactor = reactor
reactor.run()
# TODO: запилить нормальный text_history_box
