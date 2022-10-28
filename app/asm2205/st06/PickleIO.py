import pickle, os
from .Trainer import Trainer
from .TrainerMaster import TrainerMaster

path = 'data/asm2205/st06/'


class PickleIO:

    def __init__(self, staff):
        self.staff = staff
        try:
            self.load()
        except:
            self.items = {}
            self.last_id = 0

    def store(self):
        with open(path+'staff.dat', 'wb') as f:
            pickle.dump((self.last_id, self.items), f)

    def load(self):
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+'staff.dat', 'rb') as f:
            (self.last_id, self.items) = pickle.load(f)

    def getItem(self, id, isMaster=False):
        if id <= 0 and isMaster is True:
            return TrainerMaster()
        elif id <= 0 and isMaster is False:
            return Trainer()
        else:
            return self.items[id]

    def add(self, item):
        if item.id <= 0:
            self.last_id += 1
            item.id = self.last_id
            self.items[item.id] = item

    def delete(self, id):
        del self.items[id]

    def clear(self):
        self.items.clear()
        self.last_id = 0

    def getItems(self):
        for id, item in self.items.items():
            yield(item)