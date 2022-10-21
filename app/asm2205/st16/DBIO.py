import os, sqlite3
from .student import Student
from .headStudent import HeadStudent

selfpath = 'data/asm2205/st16/'

class DBStorage:
    def __init__(self, book):
        self.Load()

    def Load(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        self.db = sqlite3.connect(selfpath + 'gr.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
				   create table if not exists gr(
					   id integer primary key autoincrement,
					   name text,
					   age integer,
					   rate integer,
					   stipend real,
					   phone_number text
					   )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def Store(self):
        self.db.commit()
        self.db.close()

    def GetItem(self, id, flag=False):
        if flag:
            item = HeadStudent()
            print('HS')
        else:
            item = Student()
            print('S')
        if id > 0:
            self.dbc.execute("select * from gr where id=?", (id,))
            item.DBLoad(self.dbc.fetchone())
        return item

    def Add(self, item):
        item.DBStore(self.db)

    def Delete(self, id):
        self.db.execute("delete from gr where id=?", (id,))

    def DeleteAll(self):
        self.db.execute("delete from gr ")

    def GetItems(self):
        self.dbc.execute("select * from gr order by id desc")
        for r in self.dbc:
            if r['phone_number'] is None:
                item = Student()
            else:
                item = HeadStudent()
            item.DBLoad(r)
            print(item)
            yield (item)