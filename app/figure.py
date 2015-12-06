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

class KnightFigure(Figure):
    def attack_coords(self):
        up = [(self.x-2, self.y - 1), (self.x-2, self.y + 1)]
        left = [(self.x, self.y - 2), (self.x, self.y - 2)]
        right = [(self.x-1, self.y + 2), (self.x+1, self.y + 2)]
        down = [(self.x+2, self.y-1), (self.x+2, self.y+1)]

        return up + left + right + down

class BishopFigure(Figure):
    def attack_coords(self, aRange):
        up_right = [(self.x - (k+1), self.y + (k+1)) for k in range(aRange)]
        up_left = [(self.x - (k+1), self.y - (k+1)) for k in range(aRange)]
        down_right = [(self.x+(k+1), self.y + (k+1)) for k in range(aRange)]
        down_left = [(self.x+(k+1), self.y - (k-1)) for k in range(aRange)]

        return up_right + up_left + down_right + down_left

class QueenFigure(Figure):
    def attack_coords(self, aRange):
        up_right = [(self.x - (k+1), self.y + (k+1)) for k in range(aRange)]
        up_left = [(self.x - (k+1), self.y - (k+1)) for k in range(aRange)]
        down_right = [(self.x+(k+1), self.y + (k+1)) for k in range(aRange)]
        down_left = [(self.x+(k+1), self.y - (k-1)) for k in range(aRange)]

        up = [(self.x-(k+1), self.y) for k in range(aRange)]
        left = [(self.x, self.y-(k+1)) for k in range(aRange)]
        right = [(self.x, self.y+(k+1)) for k in range(aRange)]
        down = [(self.x+(k+1), self.y) for k in range(aRange)]

        return up + left + right + down + up_right + up_left + down_right + down_left
