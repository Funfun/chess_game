import unittest
from app.figure import Figure

class TestFigure(unittest.TestCase):
    def test_new_figure(self):
        figure = Figure(1, 2, 3)
        self.assertEqual(figure.x_range, 1)
        self.assertEqual(figure.y_range, 2)
        self.assertEqual(figure.z_range, 3)
