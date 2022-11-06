import pickle, os, sqlite3
from .model import *


class DBStorage:
    def __init__(self):
        self.path = 'data/asm2205/st24/'
        self.Load()


    def Load(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.db = sqlite3.connect(self.path + 'airlines.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
           create table if not exists worker(
               id integer primary key autoincrement,
               name text,
               age integer,
               salary integer,
               subject text,
               class_type integer
        )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def Store(self):
        self.db.commit()
        self.db.close()

    def GetItem(self, id):
        item = Pilot()
        if id > 0:
            self.dbc.execute("select * from worker where id=?", (id,))
            item.DBLoad(self.dbc.fetchone())
        return item

    def Add(self, item):
        item.DBStore(self.db)

    def Add_2(self, item):
        item.DBinsert(self.db)

    def Delete(self, id):
        self.db.execute("delete from worker where id=?", (id,))

    def GetItems(self):
        self.dbc.execute("select * from worker")
        for r in self.dbc:
            item = Worker() if r[5] == 0 else Pilot()
            item.DBLoad(r)
            yield item

    def DeleteAll(self):
        self.db.execute("DELETE FROM worker WHERE 3 = 3")


class PickleStorage:
    def __init__(self):
        self.path = 'data/asm2205/st24/'
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Load(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.path + 'airlines.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def Store(self):
        with open(self.path + 'airlines.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def GetItem(self, id):
        if id <= 0:
            return Worker()
        else:
            return self.items[id]

    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1
            item.id = self.maxid
        self.items[item.id] = item

    def Add_2(self, item):
        self.Add(item)

    def Delete(self, id):
        del self.items[id]

    def DeleteAll(self):
        self.items.clear()

    def GetItems(self):
        for (id, item) in self.items.items():
            yield (item)

