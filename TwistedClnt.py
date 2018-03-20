from twisted.internet import protocol, reactor

HOST = '120.78.197.158'
PORT = 21567

class TSClntProtocal(protocol.Protocol):
    def sendDta(self):
        data = input('> ')
        if data:
            print('...sending data %s...' % data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendDta()

    def dataReceived(self, data):
        print(data)
        self.sendDta()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocal
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()