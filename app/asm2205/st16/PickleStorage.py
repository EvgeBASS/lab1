import pickle, os
from .student import Student
from .headStudent import HeadStudent

selfpath = 'data/asm2205/st16/'


class PickleStorage:

    def __init__(self, group):
        self.group = group
        try:
            self.load()
        except:
            self.items = {}
            self.maxID = 0

    def store(self):
        with open(selfpath+'data16.dat', 'wb') as f:
            pickle.dump((self.maxID, self.items), f)

    def load(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        with open(selfpath+'data16.dat', 'rb') as f:
            (self.maxID, self.items) = pickle.load(f)

    def getItem(self, id, flag=False):
        if id <= 0 and flag is True:
            print('HS')
            return HeadStudent()
        elif id <= 0 and flag is False:
            print('S')
            return Student()
        else:
            return self.items[id]

    def add(self, item):
        if item.id <= 0:
            self.maxID += 1
            item.id = self.maxID
            self.items[item.id] = item

    def delete(self, id):
        del self.items[id]

    def deleteAll(self):
        self.items.clear()
        self.maxID = 0

    def getItems(self):
        for id, item in self.items.items():
            yield(item)