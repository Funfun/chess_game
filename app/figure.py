from abc import ABCMeta, abstractmethod

class Figure(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attack_coords(self): raise NotImplementedError()

class KingFigure(Figure):
    def __init__(self, coordX, coordY):
        self.x = coordX
        self.y = coordY

    def attack_coords(self):
        return [
            (self.x-1, self.y),
            (self.x, self.y-1),
            (self.x, self.y+1),
            (self.x+1, self.y)
        ]
