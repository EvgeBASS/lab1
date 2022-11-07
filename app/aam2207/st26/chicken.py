from app.aam2207.st26.strats import *
from dataclasses import dataclass

@dataclass
class Chicken(ConsoleWorker):
    name: str = None
    surname: str = None
    size: str = None
    class_type: str = None

    def __init__(self):
        self.atrs = ["name", "surname", "size"]
        self.class_type = self.__class__.__name__

    def __repr__(self):
        return "Курица обыкновенная"

    def __str__(self):
        return f"Имя:{self.name} Фамилия:{self.surname} Размер:{self.size} "

    def input(self):
        ConsoleWorker.console_input_atr(self, "name")
        ConsoleWorker.console_input_atr(self, "surname")
        ConsoleWorker.console_input_atr(self, "size")

    def DBInsertStr(self):
        return self.name, self.surname, self.size, "Chicken", None, None

    def DBLoad(self, r):
        self.name = r['name']
        self.surname = r['surname']
        self.size = r['size']

@dataclass
class SuperChicken(Chicken):
    color: str = None

    def __init__(self):
        super().__init__()
        self.atrs.append("color")

    def __repr__(self):
        return repr('Курица необыкновенная!')

    def __str__(self):
        return Chicken.__str__(self) + f"Цвет: {self.color} "

    def input(self):
        Chicken.input(self)
        ConsoleWorker.console_input_atr(self, 'color')

    def DBInsertStr(self):
        return self.name, self.surname, self.size, "SuperChicken", self.color, None

    def DBLoad(self, r):
        Chicken.DBLoad(self, r)
        self.color = r['color']


@dataclass
class BrolBoy(Chicken):
    battle_cry: str = None

    def __init__(self):
        super().__init__()
        self.atrs.append("battle_cry")

    def __repr__(self):
        return repr("Бройлер!!!")

    def __str__(self):
        return Chicken.__str__(self) + f"Боевой клич:{self.battle_cry} "

    def input(self):
        Chicken.input(self)
        ConsoleWorker.console_input_atr(self, 'battle_cry')

    def DBInsertStr(self):
        return self.name, self.surname, self.size, "BrolBoy", None, self.battle_cry

    def DBLoad(self, r):
        Chicken.DBLoad(self, r)
        self.battle_cry = r['battleCry']
