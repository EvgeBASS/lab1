from .dog import *
from .wolf import *
from .restIO import *
from .consoleIO import *

class Storage:
    def __init__(self):
        self.storage = restIO(self)
        self.io = consoleIO()

    def add(self):
        print('0 is adding WOLF \n'
              '1 is adding DOG')
        try:
            if int(input()=='0'):
                entity = Wolf()
                entity.add()
                self.storage.add(entity)
            else:
                entity = Dog()
                entity.add()
                self.storage.add(entity)
        except ValueError:
            print('Interrupted')
            return
        print('Entity added')


    def showZoo(self):
        for item in self.storage.getItems():
            consoleIO.output(item)

    def edit(self):
        item = self.storage.getItem(int(self.io.input("id: ")))
        consoleIO.output(item)
        item.input()
        self.storage.add(item)


    def kill(self):
        self.storage.delete(self.io.input("id: "))

    def killAll(self):
        self.storage.delete("0")
