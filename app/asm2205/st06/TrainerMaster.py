from .Trainer import Trainer
from dataclasses import dataclass


@dataclass
class TrainerMaster(Trainer):
    grade: int = 0

    def ReadFromDb(self, r):
        Trainer.ReadFromDb(self, r)
        self.grade = r['grade']

    def LoadToDb(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into staff (id, firstname, lastname, age, experience, grade) values(NULL, ?, ?, ?, ?, ?)",
                       (self.firstname, self.lastname, self.age, self.experience, self.grade))
        else:
            db.execute("update staff set firstname=?, lastname=?, age=?, experience=?, grade=? where id=?",
                       (self.firstname, self.lastname, self.age, self.experience, self.grade, self.id))

    def input(self, io):
        Trainer.input(self, io)
        self.grade = io.input('grade')
