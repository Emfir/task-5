import AbstractState
import enums
import waitingState2

class waitingState1(AbstractState.AbstractState):
    def newTicTackToePlayer(self, factory, server, state):
        """"handles appearance of the first TicTakToe player by changing current state"""
        print("changing to state 2")
        return waitingState2.waitingState2()
    def newNumberGuesserPlayer(self, factory, server):
        """"handles appearance of the number GuesserPlayer by starting the game"""
        factory.getGame(enums.game_type.gameGuesser).start(server)
        server.servedPlayer()