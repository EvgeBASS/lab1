from .utilities import Utilities

class Menu:
    def __init__(self, commands):
        self.commands = commands

    def show(self):
        for i, menuItem in enumerate(self.commands, 1):
            print(f"{i}. {menuItem[0]}")
        index = int(input())
        if index != 8:
            self.commands[index - 1][1]()
            return True
        else:
            return False
