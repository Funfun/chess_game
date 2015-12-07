from app.cell import Cell

class BoardOutOfRange(Exception):
    pass

class Board(object):
    """docstring for Board"""
    def __init__(self, raws, cols):
        super(Board, self).__init__()
        self.raws = raws-1
        self.cols = cols-1
        self.cells = {}

    def cell_at(self, x, y):
        if (self.raws >= x and self.cols >= y) and (x >= 0 and y >= 0):
            return self.cells.setdefault(str(x)+','+str(y), Cell(x, y))
        else:
            raise BoardOutOfRange()
    def has_interseptions_cells(self, figureClass, coords):
        hasInterseptions = False
        for acoords in figureClass(coords[0], coords[1]).attack_coords(max(self.raws, self.cols)):
            try:
                acell = self.cell_at(acoords[0], acoords[1])
            except BoardOutOfRange:
                continue

            if acell.value == 0:
                hasInterseptions = True

        return hasInterseptions

    def add_figure(self, figureClass):
        if bool(self.cells):
            a = None
            b = None

            items = self.cells.copy()
            for coords, cell in items.iteritems():
                if (cell.x + 1 <= self.raws and cell.y + 1 <= self.cols):
                    acell = self.cell_at(cell.x + 1, cell.y + 1)
                    if self.has_interseptions_cells(figureClass, acell.coords()):
                        continue
                    else:
                        if acell.value == -1:
                            acell.value = 0
                            a = acell.x
                            b = acell.y
                            return (a, b)
                elif (cell.x + 1 <= self.raws and cell.y - 1 >= 0):
                    acell = self.cell_at(cell.x - 1, cell.y - 1)
                    if self.has_interseptions_cells(figureClass, acell.coords()):
                        continue
                    else:
                        if acell.value == -1:
                            acell.value = 0
                            a = acell.x
                            b = acell.y
                            return (a, b)
                elif (cell.x - 1 >= 0 and cell.y + 1 <= self.cols):
                    acell = self.cell_at(cell.x - 1, cell.y - 1)
                    if self.has_interseptions_cells(figureClass, acell.coords()):
                        continue
                    else:
                        if acell.value == -1:
                            acell.value = 0
                            a = acell.x
                            b = acell.y
                            return (a, b)
                elif (cell.x - 1 >= 0 and cell.y - 1 >= 0):
                    acell = self.cell_at(cell.x - 1, cell.y - 1)
                    if self.has_interseptions_cells(figureClass, acell.coords()):
                        continue
                    else:
                        if acell.value == -1:
                            acell.value = 0
                            a = acell.x
                            b = acell.y
                            return (a, b)
                else:
                    continue
            return (a, b)
        else:
            a = 0
            b = 0
            for coords in figureClass(a, b).attack_coords():
                try:
                    acell = self.cell_at(coords[0], coords[1])
                except BoardOutOfRange as e:
                    continue

                if acell.value == -1:
                    acell.value = 1
            self.cell_at(a, b).value = 0
            return (a, b)
