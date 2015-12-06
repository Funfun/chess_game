import unittest
from app.figure import RookFigure

class TestRooksFigure(unittest.TestCase):
    def test_rook_figure_attack_coords(self):
        figure = RookFigure(5, 5)
        inRange = 2
        expectedList = [
            (4, 5),
            (3, 5),
            (5, 4),
            (5, 3),
            (5, 6),
            (5, 7),
            (6, 5),
            (7, 5)
        ]

        self.assertListEqual(figure.attack_coords(inRange), expectedList)
