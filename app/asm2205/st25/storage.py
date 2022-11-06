import pickle, os, sqlite3
from .model import *


class DBStorage:
    def __init__(self):
        self.path = 'data/asm2205/st25/'
        self.Load()


    def Load(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.db = sqlite3.connect(self.path + 'hospital.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
           create table if not exists [hospital](
               id integer primary key autoincrement,
               name text,
               surname text,
               cabinet integer,
               salary real,
               experience integer,
               post text,
               ganarar real,
               class_type integer
        )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def Store(self):
        self.db.commit()
        self.db.close()

    def GetItem(self, id):
        item = HeadDoctor()
        if id > 0:
            self.dbc.execute("select * from [hospital] where id=?", (id,))
            item.DBLoad(self.dbc.fetchone())
        return item

    def Add(self, item):
        item.DBStore(self.db)


    def Add_2(self, item):
        item.DBinsert(self.db)

    def Delete(self, id):
        self.db.execute("delete from [hospital] where id=?", (id,))

    def GetItems(self):
        self.dbc.execute("select * from [hospital]")
        for r in self.dbc:
            type = r['class_type']
            if type == 2:
                item = HeadDoctor()
            elif type == 1:
                item = Doctor()
            else:
                item = Nurse()
            item.DBLoad(r)
            yield item

    def DeleteAll(self):
        self.db.execute("DELETE FROM hospital WHERE 3 = 3")


class PickleStorage:
    def __init__(self):
        self.path = 'data/asm2205/st25/'
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Load(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.path + 'hospital.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def Store(self):
        with open(self.path + 'hospital.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def GetItem(self, id):
        if id <= 0:
            return Nurse()
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

