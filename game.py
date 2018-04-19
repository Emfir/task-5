import TicTacToe
import enums

class game:


    def start_game(self):
        game_engine = TicTacToe.TicTacToe()

        while True:
            self.__printBoard(game_engine.getBoard())
            try:
                first, second = map(int, input("next move ?").split())
            except Exception as error:
                print("write proper position")
                continue

            anser = game_engine.nextMove([first, second])

            if enums.game_state.game_is_not_finished == anser: continue
            if  enums.game_state.draw == anser:
                print("draw")
                break
            else:
                print(anser.value)

    def __printBoard(self, board):
        print(*range(3), sep="     ")

        for x in range(3):
            print(board[x], x)