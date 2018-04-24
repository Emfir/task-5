import AbstractGameFactory
import enums
import TicTacToeGameController
import numberGuesserController

class GameFactory(AbstractGameFactory.AbstractGameFactory):
    """creates and returns game controllers"""
    def getGame(self, gameName):
        if gameName == enums.game_type.gameGuesser:
            return numberGuesserController.numberGuesserController()
        elif gameName == enums.game_type.TicTackToe:
            return TicTacToeGameController.TicTacToeGameController()
