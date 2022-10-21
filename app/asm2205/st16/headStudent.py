from .student import Student
from dataclasses import dataclass


@dataclass
class HeadStudent(Student):
    phone_number: str = ""

    def DBLoad(self, r):
        Student.DBLoad(self, r)
        self.phone_number = r['phone_number']

    def DBStore(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into gr (id, name, age, rate, stipend, phone_number) values(NULL, ?, ?, ?, ?, ?)",
                       (self.name, self.age, self.rate, self.stipend, self.phone_number))
        else:
            db.execute("update gr set name=?, age=?, rate=?, stipend=?, phone_number=? where id=?",
                       (self.name, self.age, self.rate, self.stipend, self.phone_number, self.id))
        # Student.DBStore(self, db)
        # print(self.name, self.rate, self.age, self.stipend, self.phone_number, self.id)
        # db.execute("update gr set name=?, age=?, rate=?, stipend=?, phone_number=? where id=max(id)",
        #            (self.name, self.rate, self.age, self.stipend, self.phone_number, self.id))

    def input(self, io):
        Student.input(self, io)
        self.phone_number = io.input('phone_number')
