import sys
import datetime
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver
from hashlib import md5
from PyQt5.QtWidgets import QApplication

sys.path.append('../')
from gui.MainForm import ChatterBox
from gui.signup import check_valid_login, check_valid_password


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.client = self

    def lineReceived(self, line: bytes):
        message = line.decode()
        if message == '<user already exists>':
            window.reg_form.error_label.setText('User with this username already exists')
            window.reg_form.error_label.resize(window.reg_form.error_label.sizeHint())
            return
        elif message == '<login or password is incorrect>':
            window.login_form.error_label.setText('Login or password is incorrect')
        elif message.startswith('successful'):
            login = message.replace('successful ', '')
            window.current_user_lbl.setText(login)
            window.login = login
            window.edit.setVisible(True)
            window.reg_form.close()
            window.login_form.close()
        elif message.startswith('Online now: '):
            window.online_label.setText(message)
        elif message.startswith('nickname changed'):
            self.factory.window.login = message.replace('nickname changed ', '')
            self.factory.window.current_user_lbl.setText(window.login)
            self.factory.window.messages_history_plain_text.appendPlainText(f'Nickname changed to {window.login}')
        elif message.startswith('password changed'):
            self.factory.window.login = message.replace('password changed ', '')
            self.factory.window.current_user_lbl.setText(window.login)
            self.factory.window.messages_history_plain_text.appendPlainText(f'Password changed')

        else:
            self.factory.window.messages_history_plain_text.appendPlainText(message)

    def send_message(self, message):
        try:
            self.sendLine(message.encode())
        except:
            window.messages_history_plain_text.appendPlainText('<ERROR 522>\nCONNECTION TIMED OUT')


class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol = Client

    def __init__(self, app_window):
        self.window = app_window


class ChatWindow(ChatterBox):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.client = Client()
        self.reactor = None
        self.send_btn.pressed.connect(self.send_message)
        self.login_form.submit_btn.pressed.connect(self.login_user)
        self.reg_form.submit_btn.pressed.connect(self.create_user)
        self.login = None
        self.edit_form.submit_btn.pressed.connect(self.save_user_data)

    def keyPressEvent(self, event):
        from PyQt5.QtCore import Qt
        if event.key == Qt.Key_Enter:
            self.send_message()

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)

    def send_message(self, message=None):
        if message:
            self.client.send_message(message)
        else:
            if self.messagebox_text_edit.toPlainText().strip():
                message = self.messagebox_text_edit.toPlainText()
                dt = str(datetime.datetime.now()).split('.')[0]
                date, time = dt.split()[0], dt.split()[1]
                self.client.send_message(f'{message}::{self.login}::{date} {time}')
                self.messagebox_text_edit.clear()
            else:
                return

    def create_user(self):
        login = self.reg_form.login_ln.text()
        password = self.reg_form.password_ln.text()
        confirm = self.reg_form.confirm_password_ln.text()
        if not check_valid_login(login):
            if not check_valid_password(password):
                if password == confirm:
                    self.send_message(f'/register {login} {md5(password.encode()).hexdigest()}')
                else:
                    self.reg_form.error_label.setText('Passwords do not match')
            else:
                self.reg_form.error_label.setText(check_valid_password(password))
                return
        else:
            self.reg_form.error_label.setText(check_valid_login(login))

    def login_user(self):
        login = self.login_form.login_ln.text()
        password = self.login_form.password_ln.text()
        if not check_valid_login(login) and not check_valid_password(password):
            self.send_message(f'/login {login} {md5(password.encode()).hexdigest()}')
            self.login = login
        else:
            self.login_form.error_label.setText('Login or password is incorrect')

    def save_user_data(self):
        password = self.edit_form.password_ln.text()
        login = self.edit_form.login_ln.text()
        author = self.edit_form.author_ln.text()
        country = self.edit_form.country_ln.text()
        phone = self.edit_form.phone_ln.text()
        website = self.edit_form.website_ln.text()
        quote = self.edit_form.quote_plain_text.toPlainText()
        if password and not check_valid_password(password):
            self.send_message(f'/change_user_data password {md5(password.encode()).hexdigest()}')
        else:
            pass  # TODO: вывод текста в error label
        if login and not check_valid_login(login):
            self.send_message(f'/change_user_data login {login}')
        else:
            pass  # TODO: вывод текста в error label

        self.send_message(f'/change_user_data author {author}')
        self.send_message(f'/change_user_data country {country}')
        self.send_message(f'/change_user_data phone {phone}')
        self.send_message(f'/change_user_data website {website}')
        self.send_message(f'/change_user_data quote {quote}')


app = QApplication(sys.argv)
import qt5reactor

window = ChatWindow()
window.show()
qt5reactor.install()
from twisted.internet import reactor

reactor.connectTCP("localhost", 7410, Connector(window))
window.reactor = reactor
reactor.run()

# TODO: СДЕЛАТЬ ДОБАВЛЕНИЕ И ПРОСМОТР ИНФО О ПОЛЬЗОВАТЕЛЕ
