class Cell(object):
    """docstring for Cell"""
    def __init__(self, x, y):
        super(Cell, self).__init__()
        self.x = x
        self.y = y
        self.value = -1

    def coords(self):
        return (self.x, self.y)
