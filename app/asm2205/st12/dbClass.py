import os, sqlite3
from .wolf import Wolf
from .dog import Dog

selfpath = 'data/asm2205/st12/'


class dbClass:
    def __init__(self):
        self.openDB()

    def openDB(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        self.db = sqlite3.connect(selfpath + 'zoo.sqlite', detect_types=sqlite3.PARSE_DECLTYPES,
                                  check_same_thread=False)
        self.db.execute("""
        				   create table if not exists zoo(
        					   id integer primary key ,
        					   name text,
        					   race text,
        					   age text,
        					   isAggressive text,
        					   isTrained text
        					   )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def store(self):
        self.db.commit()
        self.db.close()

    def getItem(self, id):
        self.dbc.execute("select * from zoo where id=?", (id,))
        row = self.dbc.fetchone()
        item = self.determine(row)
        item.getFromDB(row)
        return item

    def add(self, e):
        e.insertToDB(self.db)

    def edit(self, e):
        e.updateDB(self.db)

    def delete(self, id):
        self.db.execute("delete from zoo where id=?", (id,))

    def deleteAll(self):
        self.db.execute("delete from zoo ")

    def getItems(self):
        self.dbc.execute("select * from zoo order by id desc")
        sl = []
        for row in self.dbc:
            item = self.determine(row)
            item.getFromDB(row)
            sl.append(item)
        return sl

    def determine(self, row):
        if row['isTrained'] == None:
            item = Wolf()
        else:
            item = Dog()
        return item
