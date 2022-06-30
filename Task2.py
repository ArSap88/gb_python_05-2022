from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, par):
        self.par = par

    @abstractmethod
    def consumption(self):
        pass

class Coat(Cloth):
    @property
    def consumption(self):
        return f'For coat - {self.par / 6.5 + 0.5 :.2f} meters of cloth is needed'

class Costume(Cloth):
    @property
    def consumption(self):
        return f'For costume - {2 * self.par + 0.3 :.2f} meters of cloth is needed'

coat = Coat(100)
costume = Costume(50)
print(coat.consumption, '\n' + costume.consumption)
