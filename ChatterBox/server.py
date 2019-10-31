from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import ServerFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineOnlyReceiver
import database


class Handler(LineOnlyReceiver):
    factory: 'Server'

    def connectionMade(self):
        self.factory.clients.append(self)
        self.login: str = None

    def connectionLost(self, reason=ConnectionDone):
        self.factory.clients.remove(self)
        print('disconnected')

    def lineReceived(self, line):
        message = line.decode()
        print(f'got message -> {message}')
        if self.login is not None:
            message = f'<{self.login}>: {message}'
            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(message.encode())
        else:
            if message.startswith('/login '):
                login, password = message.replace('/login ', '').split()[0], message.replace('/login ', '').split()[1]
                if database.check_unique(login, password):
                    self.login = login
                    print(f'user connected -> {login}')
                    self.sendLine(f'Welcome, {login}'.encode())
                else:
                    print('bad attempt to login')
                    self.sendLine('Login or password are incorrect'.encode())
            if message.startswith('/register '):
                login, password = message.replace('/register ', '').split()[0], \
                                  message.replace('/register ', '').split()[1]
                if not database.check_unique(login, password):
                    database.add_user(login, password)
                    self.login = login
                    print(f'new user connected -> {login}')
                    self.sendLine('Welcome in our friendly community'.encode())


class Server(ServerFactory):
    def __init__(self):
        self.clients = list()

    protocol = Handler

    def startFactory(self):
        print('Server started')


reactor.listenTCP(7410, Server())
reactor.run()