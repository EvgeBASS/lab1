from dataclasses import dataclass

@dataclass
class Nurse:
    id: int = 0
    name: str = ''
    surname: str = ''
    cabinet: int = 0
    class_type: int = 0

    def Input(self, io):
        self.name = io.Input('name')
        self.surname = io.Input('surname')
        self.cabinet = io.Input('cabinet')

    def Output(self, io):
        return io.Output(self)

    def DBLoad(self, r):
        self.id = r['id']
        self.name = r['name']
        self.surname = r['surname']
        self.cabinet = r['cabinet']

    def DBStore(self, db):
        if not self.id or int(self.id) == -1:
            db.execute("insert into hospital (id, name, surname, cabinet, class_type) values(NULL, ?, ?, ?, ?)",
                       (self.name, self.surname, self.cabinet, self.class_type))
        else:
            db.execute("update hospital set name=?, surname=?, cabinet=?, class_type=0 where id=?",
                       (self.name, self.surname, self.cabinet, self.id))

    def DBinsert(self, db):
        db.execute("insert into hospital (id, name, surname, cabinet, class_type) values(?, ?, ?, ?, 0)",
                   (self.id, self.name, self.surname, self.cabinet))


@dataclass
class Doctor(Nurse):
    salary: float = 0.0
    experience: int = 0
    post: str = ""
    class_type: int = 1

    def Input(self, io):
        Nurse.Input(self, io)
        self.salary = io.Input('salary')
        self.experience = io.Input('experience')
        self.post = io.Input('post')

    def DBLoad(self, r):
        Nurse.DBLoad(self, r)
        self.salary = r['salary']
        self.experience = r['experience']
        self.post = r['post']

    def DBStore(self, db):
        if not self.id or int(self.id) == -1:
            db.execute(
                "insert into hospital (id, name, surname, cabinet, salary, experience, post, class_type) values(NULL, ?, ?, ?, ?, ?, ?, 1)",
                (self.name, self.surname, self.cabinet, self.salary, self.experience, self.post))
        else:
            db.execute("update hospital set name=?, surname=?, cabinet=?, salary=?, experience=?, post=?, class_type = 1 where id=?",
                       (self.name, self.surname, self.cabinet, self.salary, self.experience, self.post, self.id))

    def DBinsert(self, db):
        db.execute("insert into hospital (id, name, surname, cabinet, salary, experience, post, class_type) values(?, ?, ?, ?, ?, ?, ?, 1)",
                   (self.id, self.name, self.surname, self.cabinet, self.salary, self.experience, self.post))


@dataclass
class HeadDoctor(Doctor):
    ganarar: float = 0.0
    class_type: int = 2

    def Input(self, io):
        Doctor.Input(self, io)
        self.ganarar = io.Input('ganarar')

    def DBLoad(self, r):
        Doctor.DBLoad(self, r)
        self.ganarar = r['ganarar']

    def DBStore(self, db):
        if not self.id or int(self.id) == -1:
            db.execute(
                "insert into hospital (id, name, surname, cabinet, salary, experience, post, ganarar, class_type) values(NULL, ?, ?, ?, ?, ?, ?, ?, 2)",
                (self.name, self.surname, self.cabinet, self.salary, self.experience, self.post, self.ganarar))
        else:
            db.execute("update hospital set name=?, surname=?, cabinet=?, salary=?, experience=?, post=?, ganarar=?, class_type = 2 where id=?",
                (self.name, self.surname, self.cabinet, self.salary, self.experience, self.post, self.ganarar, self.id))

    def DBinsert(self, db):
        db.execute("insert into hospital (id, name, surname, cabinet, salary, experience, post, ganarar, class_type) values(?, ?, ?, ?, ?, ?, ?, ?, 2)",
                   (self.id, self.name, self.surname, self.cabinet, self.salary, self.experience, self.post, self.ganarar))

