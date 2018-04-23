import AbstractState
import GameFactory
import enums
import connectionWithClients
import waitingState1

class waitingState2(AbstractState.AbstractState):
    def newTicTackToePlayer(self, factory: GameFactory.GameFactory, server: connectionWithClients, state):
        factory.getGame(enums.game_type.TicTackToe).start(server)
        server.servedPlayer()
        server.servedPlayer()

        print("back to state 1")
        return waitingState1.waitingState1()

    def newNumberGuesserPlayer(self, factory: GameFactory, server: connectionWithClients):
        factory.getGame(enums.game_type.gameGuesser).start(server)
        server.servedPlayer()