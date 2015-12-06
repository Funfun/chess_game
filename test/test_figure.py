import unittest
from app.figure import Figure

class TestFigure(unittest.TestCase):
    def test_figure(self):
        f = Figure(0, 0)

        self.assertEqual(f.x, 0)
        self.assertEqual(f.y, 0)
