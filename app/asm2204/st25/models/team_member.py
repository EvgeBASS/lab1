from abc import ABC
from dataclasses import dataclass
from app.asm2204.st25.IO.ConsoleIO import ConsoleIO
from app.asm2204.st25.IO.RestIO import RestIO


@dataclass
class TeamMember(ABC):
    id: int = 0
    first_name: str = ''
    surname: str = ''
    salary: float = 0
    activity_scope: str = ''

    def __post_init__(self):
        self.io = RestIO()

    def read(self, flag):
        if flag:
            self.first_name = self.io.input('first_name')
            self.surname = self.io.input('surname')
            self.salary = self.io.input('salary')
            self.activity_scope = self.io.input('activity_scope')
        else:
            self.first_name = self.io.input('first_name_edit'+str(self.id))
            self.surname = self.io.input('surname_edit'+str(self.id))
            self.salary = self.io.input('salary_edit'+str(self.id))
            self.activity_scope = self.io.input('activity_scope_edit'+str(self.id))

    def write(self):
        self.io.output('ID', self.id)
        self.io.output('Имя', self.first_name)
        self.io.output('Фамилия', self.surname)
        self.io.output('Зарплата', str(self.salary) + "рублей")
        self.io.output('Сфера деятельности', self.activity_scope)

