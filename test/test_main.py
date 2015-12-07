import unittest
from app.board import Board, BoardOutOfRange
from app.cell import Cell
from app.figure import KingFigure, RookFigure

class TestMain(unittest.TestCase):
    def test_place_figures_on_board(self):
        board = Board(raws=3, cols=3)

        self.assertEqual(board.add_figure(KingFigure), (0, 0))
        print [(cell.x, cell.y, cell.value) for _, cell in board.cells.iteritems()]
        self.assertEqual(board.add_figure(KingFigure), (2, 2))
        print [(cell.x, cell.y, cell.value) for _, cell in board.cells.iteritems()]
        self.assertEqual(board.add_figure(RookFigure), (2, 2))


    # def test_can_place_figures_in_given_orders(self):
    #     board.add_figure(KingFigure)
    #     board.add_figure(KingFigure)
    #     board.add_figure(RookFigure)
