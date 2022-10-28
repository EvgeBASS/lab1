from .RestIO import RestIO
from .ConsoleIO import ConsoleIO
from .Trainer import Trainer
from .TrainerMaster import TrainerMaster

class Staff:

    def __init__(self):
        self.storage = RestIO(self)
        self.io = ConsoleIO()

    def form(self, id):
        return self.storage.getItem(id).output(self.io)

    def showStaff(self):
        for item in self.storage.getItems():
            item.output(self.io)

    def add(self):
        item = Trainer()
        item.input(self.io)
        self.storage.add(item)

    def addMaster(self):
        item = TrainerMaster()
        item.input(self.io)
        self.storage.add(item, 1)

    def edit(self):
        item_edit = self.storage.getItem(int(self.io.input("id: ")))
        item_edit.output(self.io)
        item_edit.input(self.io)
        self.storage.add(item_edit)


    def delete(self):
        self.storage.delete(self.io.input("id: "))

    def clear(self):
        self.storage.clear()

