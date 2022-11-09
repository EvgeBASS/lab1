from .wolf import *
from .classIO import *


@dataclass
class Dog(Wolf):

    isTrained: bool = False

    def __str__(self):
        return super().__str__() + "\n Тренирован? " + str(self.isTrained)

    def add(self):
        super().add()
        self.isTrained = bool(self.console.inp("Training? "))
        self.id = self.iD()

    def iD(self):
        return int("1" + str(super().iD() +id(self.isTrained)))
