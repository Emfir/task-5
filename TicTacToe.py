import enums

class TicTacToe:
    def __init__(self):
        self.__board = [[' ' for x in range(3)] for x in range(3)]
        self.__counterOfTurns = 0
        self.getBoard()

    def getBoard(self):
        return self.__board

    def getNumberOfTurns(self):
        return self.__counterOfTurns
    def nextMove(self, position):

        if isinstance(position, list) and len(position) == 2:
            if position[0] > 2 or position[1] > 2 or self.__board[ position[0] ][position[1]] != ' ':
                return enums.error.different_position

            turn = self.__counterOfTurns % 2
            self.__counterOfTurns += 1
            self.__board[ position[0] ][ position[1] ] = enums.players(turn).name

            if self.__counterOfTurns == 9:
                return enums.game_state.draw

            if   self.checkBoard(enums.players(turn).name) != enums.game_state.game_is_not_finished:
                return self.checkBoard(enums.players(turn).name)



            return enums.game_state.game_is_not_finished
        else:
            return enums.error.proper_position



    def checkBoard(self, character):
        skos1 = 0
        skos2 = 0
        pion = 0
        poziom = 0

        x = 1
        if self.__board[x][x] == character:
            for y in [-1, 1]:
                if self.__board[x + y][x] == character:
                    pion += 1
                if self.__board[x][x + y] == character:
                    poziom += 1
                if self.__board[x + y][x + y] == character:
                    skos1 += 1
                if self.__board[x + y][x - y] == character:
                    skos2 += 1

        if pion == 2 or poziom == 2 or skos1 == 2 or skos2 == 2:
            return enums.game_state(character)

        pion = 0
        poziom = 0

        x = 0

        if self.__board[0][0] == character:
            for y in [-1, 1]:
                if self.__board[x + y][x] == character:
                    pion += 1
                if self.__board[x][x + y] == character:
                    poziom += 1

        if pion == 2 or poziom == 2:
            return enums.game_state(character)

        x = 2

        pion = 0
        poziom = 0

        if self.__board[2][2] == character:
            for y in [-1, -2]:
                if self.__board[x + y][x] == character:
                    pion += 1
                if self.__board[x][x + y] == character:
                    poziom += 1

        if pion == 2 or poziom == 2:
            return enums.game_state(character)

        return enums.game_state(3)