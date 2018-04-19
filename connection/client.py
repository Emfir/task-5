import socket
import pickle
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



        message = s.recv(10240)
        print(message.decode())

        while 1:
            message = pickle._loads(s.recv(10240))
            if isinstance(message, list):
                self.printBoard(message)
                continue
            elif message in {"x", "o"}:
                print (message + " won")
                break
            elif message == enums.error:
                print (message)
                continue
            else:
                print(message)


            s.send(str(input()).encode())


