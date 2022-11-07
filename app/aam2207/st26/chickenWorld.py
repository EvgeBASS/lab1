import os

from abc import ABC, abstractmethod
from copy import deepcopy
from app.aam2207.st26.chicken import *
from app.aam2207.st26.dataStrat import *

class ChickenWorld(ABC):

    @abstractmethod
    def __init__(self):
        self.isInit = False
        pass

    @abstractmethod
    def selfInit(self):
        if self.isInit:
            return
        self.path = 'data/aam2207/st26/'
        self.chickens = []
        self.dictTypes = {'Chicken': Chicken, 'SuperChicken': SuperChicken, 'BrolBoy': BrolBoy }
        self.types = [['Курица обыкновенная', Chicken], ['Курица необыкновенная!', SuperChicken],
                      ['Бройлер!!!', BrolBoy]]
        self.out_behaviour_types = [['поведение Pickle', PickleBehaviour], ['поведение Shelve', ShelveBehaviour],
                                    ['поведение sqlLite', SQLLiteBehaviour]]
        self.out_behaviour = SQLLiteBehaviour()
        self.con = None
        self.cur = None
        self.isInit = True

    def send_for_sale(self):
        self.chickens.clear()

    def chikens_to_file(self):
        if self.out_behaviour.__class__ == SQLLiteBehaviour:
            self.init_DB()
            self.out_behaviour.obj_to_file(self.cur, self.chickens)
            self.con.commit()
        else:
            if not os.path.exists(self.path):
                os.mkdir(self.path)
            self.out_behaviour.obj_to_file(self.path, self.chickens)

    def chikens_from_file(self):
        if self.out_behaviour.__class__ == SQLLiteBehaviour:
            self.init_DB()
            self.chickens = self.out_behaviour.obj_from_file(self.cur)
        else:
            if not os.path.exists(self.path):
                os.mkdir(self.path)
            self.chickens = self.out_behaviour.obj_from_file(self.path)

    def init_DB(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.con = sqlite3.connect(self.path + 'Chicken.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS [Chiken]
                ([Id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [Name] TEXT,
                [Surname] TEXT,
                [Size] INTEGER,
                [Class_type] TEXT,
                [Color] TEXT,
                [BattleCry] TEXT)
        """)


class FlaskChickenWorld(ChickenWorld):

    def __init__(self):
        ChickenWorld.__init__(self)

    def selfInit(self):
        ChickenWorld.selfInit(self)

    def add_kura(self, class_type):
        kura = class_type()
        self.chickens.append(kura)


class ConsoleChickenWorld(ChickenWorld):

    def __init__(self):
        ChickenWorld.__init__(self)
        self.selfInit()

    def selfInit(self):
        ChickenWorld.selfInit(self)

    def add_kura(self):
        print('Введите тип курицы:')
        print_menu(self.types)
        kura = self.types[my_int_input(0, len(self.types) - 1)][1]()
        kura.input()
        self.chickens.append(kura)

    def delete_kura(self):
        if not len(self.chickens):
            print('Нет куриц :(((')
        else:
            self.print_list()
            print('Введите номер курицы на продажу:')
            del self.chickens[my_int_input(0, len(self.chickens) - 1)]

    def edit_kura(self):
        if not len(self.chickens):
            print('Нет куриц :(((')
        else:
            print('Введите номер курицы для её изменения:')
            self.print_list()
            self.chickens[my_int_input(0, len(self.chickens) - 1)].input()

    def setDataBehaviour(self):
        print('Введите номер поведения:')
        print_menu(self.out_behaviour_types)
        self.out_behaviour = self.out_behaviour_types[my_int_input(0, len(self.out_behaviour_types) - 1)][1]()
        print('Сейчас ' + repr(self.out_behaviour))

    def chikens_to_file(self):
        print('Сейчас ' + repr(self.out_behaviour))
        ChickenWorld.chikens_to_file(self)

    def chikens_from_file(self):
        print('Сейчас ' + repr(self.out_behaviour))
        ChickenWorld.chikens_from_file(self)

    def print_list(self):
        print()
        for i, chicken in enumerate(self.chickens):
            print(f'\033[1m' + repr(chicken) + f'№\033[31m {i}\033[0m')
            chicken.output()
        print()

    def __str__(self):
        return f"\n\033[1mВсего куриц в курятнике: \033[31m{len(self.chickens)} \033[0m\033[1m" \
               f"\nНебычные курицы: \033[31m{list(map(lambda x: isinstance(x, self.types[1][1]), self.chickens)).count(True)}\033[0m\033[1m" \
               f"\nБройлеры: \033[31m{list(map(lambda x: isinstance(x, self.types[2][1]), self.chickens)).count(True)}\033[0m " \
               f"\n " \
               f"\n "

    def output(self):
        if not len(self.chickens):
            print('Нет куриц :(((')
            return
        self.print_list()