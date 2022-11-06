from dataclasses import dataclass

@dataclass
class Worker:
    id: int = 0
    name: str = ''
    age: int = 0
    salary: int = 0
    class_type: int = 0

    def Show(self):
        return "Правки работника"

    def Input(self, io):
        self.name = io.Input('name')
        self.age = int(io.Input('age'))
        self.salary = int(io.Input('salary'))

    def Output(self, io):
        return io.Output(self)

    def DBLoad(self, r):
        self.id = r['id']
        self.name = r['name']
        self.age = r['age']
        self.salary = r['salary']

    def DBStore(self, db):
        if not self.id or int(self.id) == -1:
            db.execute("insert into worker values(NULL, ?, ?, ?, NULL, 0)",
                       (self.name, self.age, self.salary))
        else:
            db.execute("update worker set name=?, age=?, salary=?, subject=NULL, class_type=0 where id=?",
                       (self.name, self.age, self.salary, self.id))

    def DBinsert(self, db):
        db.execute("insert into worker values(?, ?, ?, ?, NULL, 0)",
                   (self.id, self.name, self.age, self.salary))


@dataclass
class Pilot(Worker):
    subject: str = ''
    class_type: int = 1

    def Show(self):
        return "Правки пилота"

    def Input(self, io):
        Worker.Input(self, io)
        self.subject = io.Input('subject')

    def DBLoad(self, r):
        Worker.DBLoad(self, r)
        self.subject = r['subject']

    def DBStore(self, db):
        if not self.id or int(self.id) == -1:
            db.execute("insert into worker values(NULL, ?, ?, ?, ?, 1)",
                       (self.name, self.age, self.salary, self.subject))
        else:
            db.execute("update worker set name=?, age=?, salary=?, subject=?, class_type =1 where id=?",
                       (self.name, self.age, self.salary, self.subject, self.id))

    def DBinsert(self, db):
        db.execute("insert into worker values(?, ?, ?, ?, ?, 1)", (self.id, self.name, self.age, self.salary, self.subject))


