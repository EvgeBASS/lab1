from dataclasses import dataclass



@dataclass
class Student:
    id: int = 0
    name: str = ''
    age: int = 0
    rate: int = 0
    stipend: float = 0.0

    def DBLoad(self, r):
        self.id = r['id']
        self.name = r['name']
        self.age = r['age']
        self.rate = r['rate']
        self.stipend = r['stipend']

    def DBStore(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into gr (id, name, age, rate, stipend) values(NULL, ?, ?, ?, ?)",
                       (self.name, self.age, self.rate, self.stipend))
        else:
            db.execute("update gr set name=?, age=?, rate=?, stipend=? where id=?",
                       (self.name, self.age, self.rate, self.stipend, self.id))

    def input(self, io):
        self.name = io.input('name')
        self.age = io.input('age')
        self.rate = io.input('rate')
        self.stipend = io.input('stipend')

    def output(self, io):
        return io.output(self)
