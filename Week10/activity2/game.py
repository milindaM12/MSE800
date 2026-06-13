from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def play(self):
        pass