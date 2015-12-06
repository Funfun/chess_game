class Board(object):
    """docstring for Board"""
    def __init__(self, raws, cols):
        super(Board, self).__init__()
        self.raws = raws
        self.cols = cols
        self.cells = []
