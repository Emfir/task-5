import pickle
import socket
import message
import enums

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


class client():
    def printBoard(sefl, board):
        print(*range(3), sep="     ")

        for x in range(3):
            print(board[x], x)

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))


        while 1:
            messageObj = pickle._loads(s.recv(10240))

            if messageObj.getTittle() == enums.typeOfMessage.gameInformationDoNotExpectResponse:
                if   isinstance( messageObj.getData(), list):
                    self.printBoard(messageObj.getData())
                else:
                    print(messageObj.getData())
            elif messageObj.getTittle() == enums.typeOfMessage.informationRequireResponse:
                print(messageObj.getData())
                s.send(pickle.dumps(message.message(enums.typeOfMessage.informationRequireResponse, str(input()))))
            else:
                print(messageObj.getData())
                break




