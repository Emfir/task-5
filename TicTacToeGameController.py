import enums
import random
import connectionWithClients
from connection import message
import TicTacToe

class TicTacToeGameController:
    def start(self,server: connectionWithClients):
        gameObject = TicTacToe.TicTacToe()
        var = random.randint(0, 1)
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
            server.sendMessage(var % 2 + 1,
                               message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse, gameObject.getBoard() ))
            server.sendMessage(var % 2 + 1,
                               message.message(enums.typeOfMessage.informationRequireResponse, "next move ?"))

            try:

                first, second = map(int, server.receiveMessage(var % 2 + 1).getData().split())


            except Exception as error:
                server.sendMessage(var % 2 + 1,
                                   message.message(enums.typeOfMessage.informationRequireResponse,
                                                   "write proper position") )
                continue

            anser = gameObject.nextMove([first, second])
            server.sendMessage(var % 2 + 1,
                               message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                               gameObject.getBoard()))
            var += 1

            if enums.game_state.game_is_not_finished == anser: continue
            if enums.game_state.draw == anser:

                server.sendMessage(var % 2 + 1,
                                   message.message(enums.typeOfMessage.finalMessageFromTheGame, enums.game_state.draw) )
                server.sendMessage( (var - 1) % 2 + 1,
                                   message.message(enums.typeOfMessage.finalMessageFromTheGame, enums.game_state.draw))

                print("draw")
                break
            elif anser in {enums.game_state.o_won, enums.game_state.x_won}:
                server.sendMessage(var % 2 + 1,
                                   message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                                   gameObject.getBoard()))
                server.sendMessage( (var - 1) % 2 + 1,
                                   message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                                   gameObject.getBoard()))

                server.sendMessage( var % 2 + 1,
                                   message.message(enums.typeOfMessage.finalMessageFromTheGame,
                                                   anser))

                server.sendMessage( (var - 1) % 2 + 1,
                               message.message(enums.typeOfMessage.finalMessageFromTheGame,
                                               anser))


                print(anser.value)
                break
            else:
                var -= 1

                server.sendMessage(var % 2 + 1,
                                   message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                                   anser))


