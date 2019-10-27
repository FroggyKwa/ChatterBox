from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class Client(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.protocol = self

    def lineReceived(self, line: bytes):
        message = line.decode()
        self.factory.window.messages_history_plain_text.appendPlainText(message)


class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol = Client

    def __init__(self, app_window):
        self.window = app_window
