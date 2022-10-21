import pickle, os
from .student import Student


selfpath = "asm2205/st16/data16.dat"


class PickleStorage:

    def __init__(self, book):
        self.book = book
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Load(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        with open(selfpath, 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def Store(self):
        with open(selfpath, 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def GetItem(self, id):
        if id <= 0:
            return Student()
        else:
            return self.items[id]

    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1;
            item.id = self.maxid
            self.items[item.id] = item

    def Delete(self, id):
        del self.items[id]

    def GetItems(self):
        for (id, item) in self.items.items():
            yield (item)
