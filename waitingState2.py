import AbstractState
import GameFactory
import enums
import connectionWithClients
import waitingState1

class waitingState2(AbstractState.AbstractState):
    """"handles appearance of the second TicTakToe player by starting TicTackToe game
    and changing current state"""
    def newTicTackToePlayer(self, factory: GameFactory.GameFactory, server: connectionWithClients, state):
        factory.getGame(enums.game_type.TicTackToe).start(server)
        server.servedPlayer()
        server.servedPlayer()

        print("back to state 1")
        return waitingState1.waitingState1()

    def newNumberGuesserPlayer(self, factory: GameFactory, server: connectionWithClients):
        """"handles appearance of the number GuesserPlayer by starting the game"""
        factory.getGame(enums.game_type.gameGuesser).start(server)
        server.servedPlayer()