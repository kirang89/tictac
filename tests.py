# -*- coding: utf-8 -*-
from tictac import Engine, Player
import unittest


class EngineTestCase(unittest.TestCase):

    def test_now_win(self):
        board = ['X', 'X',  '',
                 'O',  '',  '',
                 'O',  '',  '']
        self.assertFalse(Engine(None, None).has_won(board, Player.X))

    def test_row_win(self):
        board = ['X', 'X', 'X',
                 'O',  '',  '',
                 'O',  '',  '']
        self.assertTrue(Engine(None, None).has_won(board, Player.X))

    def test_column_win(self):
        board = ['',  '', 'X',
                 'O', '', 'X',
                 'O', '', 'X']
        self.assertTrue(Engine(None, None).has_won(board, Player.X))

    def test_left_diagonal_win(self):
        board = ['X',  '',  '',
                 'O', 'X',  '',
                 'O',  '',  'X']
        self.assertTrue(Engine(None, None).has_won(board, Player.X))

    def test_right_diagonal_win(self):
        board = ['O',  '', 'X',
                 'O', 'X',  '',
                 'X',  '',  '']
        self.assertTrue(Engine(None, None).has_won(board, Player.X))

    def test_best_move(self):
        samples = [
            (["", "O", "", "",  "", "X", "O", "X", "X"], 2),
            (["O", "", "", "",  "", "X", "O", "X", "X"], 3),
            (["",  "", "", "", "X", "", "O", "", "X"], 0)
        ]

        for board, move in samples:
            self.assertEquals(Engine(board).best_move(), move)


if __name__ == '__main__':
    unittest.main()
