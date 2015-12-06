import unittest
from app.board import Board, BoardOutOfRange
from app.cell import Cell

class TestBoard(unittest.TestCase):
    def test_new_board(self):
        board = Board(raws=10, cols=20)
        self.assertEqual(board.raws, 10)
        self.assertEqual(board.cols, 20)

    def test_board_cells(self):
        board = Board(raws=10, cols=10)
        self.assertTrue(isinstance(board.cells, dict))

    def test_board_cell_at(self):
        board = Board(raws=10, cols=10)
        self.assertTrue(isinstance(board.cell_at(10, 10), Cell))

    def test_board_cell_at_out_of_range(self):
        board = Board(raws=10, cols=10)
        self.assertRaises(BoardOutOfRange, board.cell_at, 11, 11)

        board = Board(raws=10, cols=10)
        self.assertRaises(BoardOutOfRange, board.cell_at, 10, 11)
