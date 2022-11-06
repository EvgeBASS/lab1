from dataclasses import dataclass

from clients.asm2204.st25.IO.RestIO import RestIO, dictToModel, serializeMember
from clients.asm2204.st25.models.analyst import Analyst
from clients.asm2204.st25.models.developer import Developer
from clients.asm2204.st25.utilities.utilities import Utilities


@dataclass
class Team:
    def __init__(self):
        self.io = RestIO()
        self.maxID = 0

    def add(self):
        while True:
            print("""
        [0] Назад
        [1] Добавить разработчика
        [2] Добавить аналитика
            """)
            choice = int(input())
            if choice == 0:
                break
            elif choice == 1:
                developer = Developer(id=self.maxID)
                developer.read()
                self.io.addMember(serializeMember(developer))
            elif choice == 2:
                analyst = Analyst(id=self.maxID)
                analyst.read()
                self.io.addMember(serializeMember(analyst))
            else:
                print("Некорректное значение")

    def show(self):
        members = self.io.getTeam()
        for value in members:
                print("-----")
                member = dictToModel(members[value])
                member.write()
                print("-----")

    def save(self):
            self.io.input()
            print("Данные сохранены")

    def load(self):
        self.io.output()
        print("Данные загружены")

    def delete(self):
                self.show()
                while True:
                    index = input('Выберите члена команды: ')
                    if Utilities.input_check(index, 0, 100):
                        self.io.deleteMember(index)
                        print('Успешно удален')
                        break
                    else:
                        self.show()

    def clear(self):
        self.io.clearTeam()
        print("Данные успешно удалены")

    def edit(self):
        self.show()
        index = input('Выберите члена команды: ')
        if Utilities.input_check(index, 0, 100):
                value = self.io.getMember(int(index))
                member = dictToModel(value)
                member.read()
                self.io.editMember(serializeMember(member))
                print('Отредактировано')


