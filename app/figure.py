from abc import ABCMeta, abstractmethod

class Figure(object):
    def __init__(self, coordX, coordY):
        self.x = coordX
        self.y = coordY

    @abstractmethod
    def attack_coords(self): raise NotImplementedError()

class KingFigure(Figure):
    def attack_coords(self):
        return [
            (self.x-1, self.y),
            (self.x, self.y-1),
            (self.x, self.y+1),
            (self.x+1, self.y)
        ]

class RookFigure(Figure):
    def attack_coords(self, aRange):
        up = [(self.x-(k+1), self.y) for k in range(aRange)]
        left = [(self.x, self.y-(k+1)) for k in range(aRange)]
        right = [(self.x, self.y+(k+1)) for k in range(aRange)]
        down = [(self.x+(k+1), self.y) for k in range(aRange)]

        return up + left + right + down
