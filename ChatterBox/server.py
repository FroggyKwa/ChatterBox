from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import ServerFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineOnlyReceiver
import database


class Handler(LineOnlyReceiver):
    factory: 'Server'

    def connectionMade(self):
        self.factory.clients.append(self)
        print('connected')
        self.login = None

    def connectionLost(self, reason=ConnectionDone):
        self.factory.clients.remove(self)
        print('disconnected')

    def lineReceived(self, line):
        message = line.decode()
        login = message.split('::')[0] if not message.startswith('/') else ''
        message = message.replace(f'{login}::', '')
        print(f'got message from {login} -> {message}')
        if self.login is not None and not (message.startswith('/login') or message.startswith('/register')):
            message = f'<{self.login}>: {message}'
            for user in self.factory.clients:
                # if user is not self: TODO: НЕ ЗАБЫТЬ ЭТО УБРАТЬ
                user.sendLine(message.encode())
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


# TODO: скорректировать работу регистрации


class Server(ServerFactory):
    def __init__(self):
        self.clients = list()

    protocol = Handler

    def startFactory(self):
        print('Server started...')


reactor.listenTCP(7411, Server())
reactor.run()
