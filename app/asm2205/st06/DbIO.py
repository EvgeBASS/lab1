import os, sqlite3
from .Trainer import Trainer
from .TrainerMaster import TrainerMaster

path = 'data/asm2205/st06/'

class DbIO:
    def __init__(self, staff):
        self.load()

    def load(self):
        if not os.path.exists(path):
            os.mkdir(path)
        self.db = sqlite3.connect(path + 'staff.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
				   create table if not exists staff(
					   id integer primary key autoincrement,
					   firstname text,
					   lastname text,
					   age integer,
					   experience integer,
					   grade integer
					   )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def store(self):
        self.db.commit()
        self.db.close()

    def getItem(self, id, isMaster=False):
        if isMaster:
            item = TrainerMaster()
        else:
            item = Trainer()
        if id > 0:
            self.dbc.execute("select * from staff where id=?", (id,))
            item.ReadFromDb(self.dbc.fetchone())
        return item

    def getItems(self):
        self.dbc.execute("select * from staff order by id desc")
        for r in self.dbc:
            if r['grade'] is None:
                item = Trainer()
            else:
                item = TrainerMaster()
            item.ReadFromDb(r)
            print(item)
            yield (item)

    def add(self, item):
        item.LoadToDb(self.db)

    def delete(self, id):
        self.db.execute("delete from staff where id=?", (id,))

    def clear(self):
        self.db.execute("delete from staff ")

