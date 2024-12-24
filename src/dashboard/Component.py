from abc import ABC, abstractmethod

# create abstract class for component
class Component(ABC):
    def __init__(self, position: tuple):
        self.position = position

    @abstractmethod
    def display(self):
        pass
