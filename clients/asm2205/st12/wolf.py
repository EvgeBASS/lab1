from dataclasses import dataclass

from .classIO import *

@dataclass
class Wolf:

    id: int = 0
    name: str = ''
    age: str = 0
    race: str = 0
    isAggressive: bool = False
    console = classIO()

    def __str__(self):
        return "Имя " + self.name + "; Возраст" + self.age + \
               ";\nПорода" + self.race + "; Агрессивен? " + str(self.isAggressive) + \
               "; ID " + str(self.id)+ "\n"


    def add(self):
        self.input()
        self.id = self.iD()

    def input(self):
        self.name = self.console.inp('name ->',)
        self.race = self.console.inp('race ->',)
        self.age = self.console.inp('age ->',)
        self.isAggressive = bool(self.console.inp('isAggressive? ',))

    def iD(self):
        return int("0" + str(id(self.name)+id(self.race)+id(self.age)+id(self.isAggressive)))