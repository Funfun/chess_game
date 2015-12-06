import unittest
from app.figure import KingFigure

class TestKingFigure(unittest.TestCase):
    def test_king_figure(self):
        king = KingFigure(0, 0)

        self.assertEqual(king.x, 0)
        self.assertEqual(king.y, 0)

    def test_king_figure_attack_coords(self):
        king = KingFigure(5, 5)
        expectedList = [(4, 5), (5, 4), (5, 6), (6, 5)]

        self.assertListEqual(king.attack_coords(), expectedList)
