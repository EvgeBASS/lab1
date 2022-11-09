from .wolf import Wolf

class Dog(Wolf):
    isTrained: bool = False

    def __str__(self):
        return super(self.id).__str__() + "\n Тренирован? " + str(self.isTrained)

    def add(self):
        self.baseAdd()
        self.id = self.iD()

    def baseAdd(self):
        super().baseAdd()
        self.isTrained = bool(self.refIO.responseContext('isTrained'))

    def getFromDB(self, row):
        Wolf.getFromDB(self, row)
        self.isTrained = bool(row['isTrained'])

    def input(self, io):
        Wolf.input(self, io)
        self.isTrained = bool(io.input('isTrained'))

    def insertToDB(self, db):
        Wolf.insertToDB(self, db)
        db.execute("update zoo set name=?, race=?, age=?, isAggressive=?, isTrained=? where id=?",
                   (self.name, self.race, self.age, self.isAggressive, self.isTrained, self.id))

    def iD(self):
        return int("1" + str(super().iD() +id(self.isTrained)))