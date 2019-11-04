from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import ServerFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineOnlyReceiver
import database


class Handler(LineOnlyReceiver):
    factory: 'Server'

    def connectionMade(self):
        self.factory.clients.append(self)
        self.login = None
        print('connected')
        self.sendLine(f'Online now: {len(self.factory.clients)}'.encode())

    def connectionLost(self, reason=ConnectionDone):
        self.factory.clients.remove(self)
        print('disconnected')

    def lineReceived(self, line):
        message = line.decode()
        if self.login and not (message.startswith('/login') or
                                           message.startswith('/register') or
                                           message.startswith('/change_user_data')):
            login = message.split('::')[1]
            date_time = message.split('::')[2]
            date, time = date_time.split()[0], date_time.split()[1]

            message = message.replace(f'{login}::', '')
            message = message.replace(f'::{date_time}', '')
            print(f'got message from {login} -> {message}')
            database.add_message(message, self.login, date_time)
            message = f'[{date} {time}]      <{self.login}>: {message}'
            for user in self.factory.clients:
                user.sendLine(message.encode())
        elif self.login and message.startswith('/change_user_data'):
            message = message.replace('/change_user_data ', '').split()
            if len(message) == 2:
                edit_field = message[0]
                new_val = message[1]
                if edit_field == 'login':
                    database.edit_user_info(self.login, new_login=new_val)
                    self.login = new_val
                    self.sendLine(f'nickname changed {self.login}'.encode())
                if edit_field == 'password':
                    database.edit_user_info(self.login, password=new_val)
                    self.sendLine('password changed'.encode())
                if edit_field == 'country':
                    database.edit_user_info(self.login, country=new_val)
                if edit_field == 'phone':
                    database.edit_user_info(self.login, phone=new_val)
                if edit_field == 'website':
                    database.edit_user_info(self.login, website=new_val)
                if edit_field == 'author':
                    database.edit_user_info(self.login, author=new_val)
                if edit_field == 'quote':
                    database.edit_user_info(self.login, quote=new_val)

        else:
            if message.startswith('/login '):
                login, password = message.replace('/login ', '').split()[0], message.replace('/login ', '').split()[1]
                if database.check_auth(login, password):
                    self.login = login
                    print(f'user connected -> {login}')
                    self.sendLine(f'successful {login}'.encode())
                    self.sendLine(f'Welcome, {login}'.encode())
                else:
                    print('bad attempt to login')
                    self.sendLine('<login or password is incorrect>'.encode())
            elif message.startswith('/register '):
                login, password = message.replace('/register ', '').split()[0], \
                                  message.replace('/register ', '').split()[1]
                if not database.check_unique(login):
                    database.add_user(login, password.encode())
                    self.login = login
                    print(f'new user connected -> {login}')
                    self.sendLine(f'successful {login}'.encode())
                    self.sendLine('Welcome in our friendly community'.encode())
                else:
                    self.sendLine('<user already exists>'.encode())


class Server(ServerFactory):
    def __init__(self):
        self.clients = list()

    protocol = Handler

    def startFactory(self):
        print('Server started...')


reactor.listenTCP(7410, Server())
reactor.run()
