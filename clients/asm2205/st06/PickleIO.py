import pickle, os
from .Trainer import Trainer

path = "asm2205/st06/staff.dat"


class PickleIO:

    def __init__(self, staff):
        self.staff = staff
        try:
            self.load()
        except:
            self.items = {}
            self.last_id = 0

    def store(self):
        with open(path, 'wb') as f:
            pickle.dump((self.last_id, self.items), f)


    def load(self):
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path, 'rb') as f:
            (self.last_id, self.items) = pickle.load(f)
    
    
    def getItem(self, id):
        if id <= 0:
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
