import NumberGuesser
import enums
import connectionWithClients
import message


class numberGuesserController :
    def start(self, server: connectionWithClients.connectionWithClients):
        engine = NumberGuesser.NumberGuesser()

        while 1:

            try:
                server.sendMessage(server.numberOfClients(),
                                   message.message(enums.typeOfMessage.informationRequireResponse,
                                                   "whats your guess?"))
                clientNumber = int (server.receiveMessage(server.numberOfClients()).getData())

            except Exception as error:
                server.sendMessage(server.numberOfClients(),
                                   message.message(enums.typeOfMessage.informationRequireResponse,
                                                   "whats your guess?"))
                continue

            output = engine.nextGuess(clientNumber)

            print(output.value)
            if output == enums.resultsOfTheGuess.goodGuess:
                server.sendMessage(server.numberOfClients(),
                                   message.message(enums.typeOfMessage.finalMessageFromTheGame,
                                                   output.value))
                break
            else:
                server.sendMessage(server.numberOfClients(),
                                   message.message(enums.typeOfMessage.gameInformationDoNotExpectResponse,
                                                   output.value))