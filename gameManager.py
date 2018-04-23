import connectionWithClients
import waitingState1
import message
import enums
import GameFactory


class gameManager():
    def __init__(self ):
        self.__gameFactory = GameFactory.GameFactory()
        self.serverState = waitingState1.waitingState1()

    def start(self):
        server = connectionWithClients.connectionWithClients()
        while 1:
            server.findPlayer()
            print("cos")
            while 1:

                server.sendMessage(server.numberOfClients(),
                                   message.message(enums.typeOfMessage.informationRequireResponse,
                                                            "What Game Do you want to play? (G)the Number Guesser or the (T)TickTackToe?"))
                response = server.receiveMessage(server.numberOfClients())

                if response.getData() == "T":
                    self.serverState = self.serverState.newTicTackToePlayer(self.__gameFactory,
                                                                            server,
                                                                            self.serverState)
                    break
                elif response.getData() == "G":
                    try:

                        self.serverState.newNumberGuesserPlayer(self.__gameFactory,
                                                                            server)
                    except Exception as error:
                        print(error)
                    break


