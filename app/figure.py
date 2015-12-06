from abc import ABCMeta, abstractmethod

class Figure(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attack_coords(self): raise NotImplementedError()
