import unittest
from app.cell import Cell

class TestCell(unittest.TestCase):
    def test_new_cell(self):
        cell = Cell(x=10, y=20)
        self.assertEqual(cell.x, 10)
        self.assertEqual(cell.y, 20)
        self.assertEqual(cell.value, -1)

        cell.value = 1
        self.assertEqual(cell.value, 1)
        self.assertEqual(cell.coords(), (10, 20))
