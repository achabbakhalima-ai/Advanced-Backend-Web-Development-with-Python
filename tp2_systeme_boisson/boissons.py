from abc import ABC, abstractmethod
class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass
    @abstractmethod
    def description(self):
        pass

    def __add__(self, other):
        return BoissonCombinee(self, other)
class Cafe(Boisson):
    def cout(self):
        return 2.0
    def description(self):
        return "Café simple"
class The(Boisson):
    def cout(self):
        return 1.8
    def description(self):
        return "Thé"
class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def cout(self):
        return self.b1.cout() + self.b2.cout()
    def description(self):
        return self.b1.description() + " + " + self.b2.description()