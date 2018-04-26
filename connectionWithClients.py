import select
import socket
import pickle
import enums
import message

host = '127.0.0.1'
port = 5005
backlog = 2
maxsize = 1024


class connectionWithClients():
    """"class responsible for connection with clients"""
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(backlog)
        self.input = [self.server, ]
        self.var = 1


    def findPlayer(self):
        """"finds client"""


        self.inputready, self.outputready, self.exceptready = select.select(self.input, [], [])
        for s in self.inputready:

            if s == self.server:
                client, address = self.server.accept()
                self.input.append(client)
                print('new client added%s' % str(address))
                self.sendMessage(self.var,
                                 message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                                 "I see YOU"))

                self.var += 1

    def servedPlayer(self):
        """"removes newest client from the list """
        self.input[-1].close()
        self.input.pop()
        self.var -= 1

    def sendMessage(self, client, letter):

        self.input[client].send(pickle.dumps(letter))

    def receiveMessage(self, client):
        return pickle.loads( self.input[client].recv(10240) )

    def numberOfClients(self):
        """"returns current number of clients"""
        return self.var - 1

