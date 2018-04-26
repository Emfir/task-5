from unittest import TestCase
from unittest import main
import TicTacToe
import enums

class TestTicTacToe(TestCase):
    def test_nextMove_move_if_off_the_board(self):
        TicTac = TicTacToe.TicTacToe()
        self.assertEqual(TicTac.nextMove([50, 50]), enums.error.different_position )
        self.assertEqual(TicTac.nextMove([-2, 1]) , enums.error.different_position )
        self.assertEqual(TicTac.nextMove([-5, -5]) , enums.error.different_position)


    def test_nextMove_move_is_forbidden(self):
        TicTac = TicTacToe.TicTacToe()
        TicTac.nextMove([1,1])
        self.assertEqual(TicTac.nextMove([1, 1]), enums.error.different_position )

    def test_nextMove_if_a_wrong_position(self):
        TicTac = TicTacToe.TicTacToe()
        self.assertEqual(TicTac.nextMove(50), enums.error.proper_position)
        self.assertEqual(TicTac.nextMove('a'), enums.error.proper_position)
        self.assertEqual(TicTac.nextMove(['G', 1]), enums.error.proper_position)
        self.assertEqual(TicTac.nextMove(['G', 'A']), enums.error.proper_position)
        self.assertEqual(TicTac.nextMove([1, 1, 1]), enums.error.proper_position)


    def test_nextMove_if_a_position(self):
        TicTack = TicTacToe.TicTacToe()
        self.assertEqual(TicTack.nextMove(50), enums.error.proper_position)


    def test_nextMove_proper_use(self):
        TicTac = TicTacToe.TicTacToe()
        self.assertEqual(TicTac.nextMove([0,0]), enums.game_state.game_is_not_finished)

    def  test_nextMove_changes_to_board(self):
        TicTac = TicTacToe.TicTacToe()
        TicTac.nextMove([0,0])
        TicTac.nextMove([0,1])
        board =  [[' ' for x in range(3)] for x in range(3)]
        board[0][0] = "x"
        board[0][1] = "o"
        self.assertEqual(TicTac.getBoard(), board)


    def test_checkBoard_full_game_x_win(self):
        TicTac = TicTacToe.TicTacToe()
        TicTac.nextMove([0,0]) #x [0,0]
        TicTac.nextMove([1,0]) #o [1,0]
        TicTac.nextMove([0,1]) #x [0,1]
        TicTac.nextMove([2,0]) #o [2,0]
        TicTac.nextMove([1,1]) #x [1,1]
        TicTac.nextMove([2,1]) #o [2,1]
        TicTac.nextMove([1,2]) #x [1,2]
        TicTac.nextMove([0,2]) #o [0,2]
        self.assertEqual(TicTac.checkBoard('x'),enums.game_state.game_is_not_finished)
        TicTac.nextMove([2,2]) #x [2,2]
        self.assertNotEqual(TicTac.checkBoard('o'), enums.game_state.o_won)
        self.assertNotEqual(TicTac.checkBoard('x'), enums.game_state.o_won)
        self.assertNotEqual(TicTac.checkBoard('x'), enums.game_state.draw)
        self.assertNotEqual(TicTac.checkBoard('o'), enums.game_state.draw)
        self.assertNotEqual(TicTac.checkBoard('x'), enums.game_state.game_is_not_finished)
        self.assertEqual(TicTac.checkBoard('o'), enums.game_state.game_is_not_finished)
        self.assertEqual(TicTac.checkBoard('x'), enums.game_state.x_won)
        self.assertNotEqual(TicTac.checkBoard('o'), enums.game_state.x_won)

    def test_checkBoard_full_game_o_win_with_bad_inputs(self):
        TicTac = TicTacToe.TicTacToe()
        TicTac.nextMove([0,0]) #x [0,0]
        TicTac.nextMove([1,0]) #o [1,0]
        TicTac.nextMove([1,0]) # bad input
        TicTac.nextMove([0,1]) #x [0,1]
        TicTac.nextMove([2,0]) #o [2,0]
        TicTac.nextMove([1,1]) #x [1,1]
        TicTac.nextMove([1, 0])# bad input
        TicTac.nextMove([2,1]) #o [2,1]
        TicTac.nextMove([1,2]) #x [1,2]
        TicTac.nextMove(5)     # bad input
        TicTac.nextMove([5, 0])# bad input
        TicTac.nextMove([2,2]) #o [2,2]
        self.assertEqual(TicTac.checkBoard('x'),enums.game_state.game_is_not_finished)
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.x_won)
        self.assertNotEqual(TicTac.checkBoard('x'),enums.game_state.x_won)
        self.assertNotEqual(TicTac.checkBoard('x'),enums.game_state.draw)
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.draw)
        self.assertNotEqual(TicTac.checkBoard('x'),enums.game_state.game_is_not_finished)
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.game_is_not_finished)
        self.assertNotEqual(TicTac.checkBoard('x'), enums.game_state.o_won)
        self.assertEqual(TicTac.checkBoard('o'),enums.game_state.o_won)

    def test_checkBoard_draw(self):
        TicTac = TicTacToe.TicTacToe()
        TicTac.nextMove([0,0]) #x [0,0]
        TicTac.nextMove([1,0]) #o [1,0]
        TicTac.nextMove([0,1]) #x [0,1]
        TicTac.nextMove([1,1]) #o [2,0]
        TicTac.nextMove([1,2]) #x [1,1]
        TicTac.nextMove([0,2]) #o [2,1]
        TicTac.nextMove([2,2]) #x [1,2]
        TicTac.nextMove([2,1]) #o [1,2]
        TicTac.nextMove([2,0]) #x [1,2]
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.x_won)
        self.assertNotEqual(TicTac.checkBoard('x'),enums.game_state.x_won)
        self.assertNotEqual(TicTac.checkBoard('x'),enums.game_state.game_is_not_finished)
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.game_is_not_finished)
        self.assertNotEqual(TicTac.checkBoard('x'), enums.game_state.o_won)
        self.assertNotEqual(TicTac.checkBoard('o'),enums.game_state.o_won)
        self.assertEqual(TicTac.checkBoard('x'), enums.game_state.draw)
        self.assertEqual(TicTac.checkBoard('o'), enums.game_state.draw)

if __name__ == '__main__':
    main()

