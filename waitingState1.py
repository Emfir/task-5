import AbstractState
import enums
import waitingState2

class waitingState1(AbstractState.AbstractState):
    def newTicTackToePlayer(self, factory, server, state):
        print("changing to state 2")
        return waitingState2.waitingState2()
    def newNumberGuesserPlayer(self, factory, server):
        factory.getGame(enums.game_type.gameGuesser).start(server)
        server.servedPlayer()