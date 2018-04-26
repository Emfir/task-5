import select
import socket
import TicTacToe
import pickle
import random
import enums
from connection import message

host = '127.0.0.1'
port = 5005
backlog = 2
maxsize = 1024


class server():
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(backlog)
        input = [server,]

        var = 1
        for x in range(2):
            inputready,outputready,exceptready = select.select(input,[],[])

            for s in inputready:

                if s == server:
                    client, address = server.accept()
                    input.append(client)
                    print ( 'new client added%s'%str(address) )
                    input[var].send(str.encode("I see YOU"))
                    var += 1



        gameObject = TicTacToe.TicTacToe()

        var = random.randint(0,1)
        print(var)

        # while 1:
        #     try:
        #         input[1].send(pickle._dumps("chose game"))
        #         cos = input[1].recv(10240)
        #         a =  ( cos.decode() )
        #         print(a)
        #     except Exception as error:
        #         print(error)

        while 1:
            input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,  gameObject.getBoard())))
            input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.informationRequireResponse,  "next move ?")))


            try:
                first, second = map(int, pickle.loads(input[var % 2 + 1].recv(10240)).getData().split())


            except Exception as error:
                input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.informationRequireResponse,  "write proper position")))
                continue

            anser = gameObject.nextMove([first, second])
            input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,  gameObject.getBoard())))
            var += 1

            if enums.game_state.game_is_not_finished == anser: continue
            if enums.game_state.draw == anser:

                input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.finalMessageFromTheGame,  enums.game_state.draw)))
                input[(var - 1) % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.finalMessageFromTheGame,  enums.game_state.draw)))
                print("draw")
                break
            elif anser in {enums.game_state.o_won, enums.game_state.x_won}:
                input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,  gameObject.getBoard())))

                input[(var - 1)% 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,  gameObject.getBoard())))

                input[(var - 1) % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.finalMessageFromTheGame,  anser)))
                input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.finalMessageFromTheGame,  anser)))

                print(anser.value)
                break
            else:
                var -= 1
                input[var % 2 + 1].send(pickle._dumps(message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,  anser)))




