from dataclasses import dataclass

@dataclass
class Trainer:
    id: int = 0
    firstname: str = ''
    lastname: str = ''
    age: int = 0
    experience: int = 0

    def ReadFromDb(self, r):
        self.id = r['id']
        self.firstname = r['firstname']
        self.lastname = r['lastname']
        self.age = r['age']
        self.experience = r['experience']
  

    def LoadToDb(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into staff (id, firstname, lastname, age, experience) values(NULL, ?, ?, ?, ?)",
                       (self.firstname, self.lastname, self.age, self.experience))
        else:
            db.execute("update staff set firstname=?, lastname=?, age=?, experience=? where id=?",
                       (self.firstname, self.lastname, self.age, self.experience, self.id))

    def input(self, io):
        self.firstname = io.input('firstname')
        self.lastname = io.input('lastname')
        self.age = io.input('age')
        self.experience = io.input('experience')


    def output(self, io):
        return io.output(self)