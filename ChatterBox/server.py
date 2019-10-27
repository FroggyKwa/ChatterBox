from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import ServerFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineOnlyReceiver


class Handler(LineOnlyReceiver):
    factory: 'Server'

    def connectionMade(self):
        self.factory.clients.append(self)
        print(f'connected {self}')
        self.login: str = None

    def connectionLost(self, reason=ConnectionDone):
        self.factory.clients.remove(self)
        print('disconnected')

    def lineReceived(self, line):
        message = line.decode()
        if self.login is not None:
            message = f'<{self.login}>: {message}'
            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(message.encode())
        else:
            if message.startswith('/login '):
                login = message.replace('/login', '')
                self.login = login
                print(f'new user -> {login}')
                self.sendLine(f'Welcome, {login}'.encode())
            else:
                self.sendLine('login incorrect'.encode())

            


class Server(ServerFactory):
    def __init__(self):
        self.clients = list()

    protocol = Handler

    def startFactory(self):
        print('Server started')


reactor.listenTCP(7410, Server())
reactor.run()
