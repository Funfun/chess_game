from app.cell import Cell

class BoardOutOfRange(Exception):
    pass

class Board(object):
    """docstring for Board"""
    def __init__(self, raws, cols):
        super(Board, self).__init__()
        self.raws = raws
        self.cols = cols
        self.cells = {}

    def cell_at(self, x, y):
        if self.raws >= x and self.cols >= y:
            return self.cells.setdefault(x+y, Cell(x, y))
        else:
            raise BoardOutOfRange()
