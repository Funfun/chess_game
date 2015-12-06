import unittest
from app.figure import Figure, KingFigure, RookFigure, KnightFigure

class TestFigure(unittest.TestCase):
    def test_figure(self):
        f = Figure(0, 0)

        self.assertEqual(f.x, 0)
        self.assertEqual(f.y, 0)

    def test_king_figure_attack_coords(self):
        king = KingFigure(5, 5)
        expectedList = [(4, 5), (5, 4), (5, 6), (6, 5)]

        self.assertListEqual(king.attack_coords(), expectedList)

    def test_rook_figure_attack_coords(self):
        figure = RookFigure(5, 5)
        inRange = 2
        expectedList = [
            (4, 5), (3, 5), (5, 4), (5, 3), (5, 6), (5, 7), (6, 5), (7, 5)
        ]

        self.assertListEqual(figure.attack_coords(inRange), expectedList)

    def test_knight_figure_attack_coords(self):
        figure = KnightFigure(5, 5)
        inRange = 2
        expectedList = [
            (3, 4), (3, 6), (5, 3), (5, 3), (4, 7), (6, 7), (7, 4), (7, 6)
        ]

        self.assertListEqual(figure.attack_coords(), expectedList)
