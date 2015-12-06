import unittest
from app.figure import Figure

class TestFigure(unittest.TestCase):
    def test_new_figure(self):
        self.assertRaises(TypeError, Figure)
