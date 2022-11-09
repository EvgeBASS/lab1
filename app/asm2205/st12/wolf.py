import sqlite3

from .classIO import classIO

class Wolf:
    name: str
    race: str
    age: str
    isAggressive: bool
    id: int
    refIO = classIO()


    def __str__(self):
        return "Имя " + self.name + "; Возраст" + str(self.age) + \
               ";\nПорода" + self.race + "; Агрессивен? " + str(self.isAggressive)


    def add(self):
        self.baseAdd()
        self.id = self.iD()

    def baseAdd(self):
        self.name = self.refIO.responseContext('name')
        self.race = self.refIO.responseContext('race')
        self.age = self.refIO.responseContext('age')
        self.isAggressive = bool(self.refIO.responseContext('isAggressive'))

    def getFromDB(self, row):
        self.id = row['id']
        self.name = row['name']
        self.race = row['race']
        self.age = row['age']
        self.isAggressive = bool(row['isAggressive'])

    def input(self, io):
        self.id = io.input('id')
        self.name = io.input('name')
        self.race = io.input('race')
        self.age = io.input('age')
        self.isAggressive = bool(io.input('isAggressive'))

    def insertToDB(self, db):
        try:
            db.execute("insert into zoo (id, name, race, age, isAggressive) values(?, ?, ?, ?, ?)",
                    (self.id, self.name, self.race, self.age, self.isAggressive))
        except sqlite3.IntegrityError:
            print('Collision Failed')


    def updateDB(self, db):
        try:
           db.execute("update zoo set name=?, race=?, age=?, isAggressive=? where id=?",
                    (self.name, self.race, self.age, self.isAggressive, self.id))
        except sqlite3.IntegrityError:
            print('Collision Failed')

    def iD(self):
        return int("0" + str(id(self.name)+id(self.race)+id(self.age)+id(self.isAggressive)))