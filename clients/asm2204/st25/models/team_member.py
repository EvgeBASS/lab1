from abc import ABC, abstractmethod

from dataclasses import dataclass

from clients.asm2204.st25.IO.ConsoleIO import ConsoleIO


@dataclass
class TeamMember(ABC):
    id: int = 0
    first_name: str = ''
    surname: str = ''
    salary: float = 0
    activity_scope: str = ''

    def __post_init__(self):
        self.io = ConsoleIO()

    def read(self):
        self.first_name = self.io.input('имя \n', 'string')
        self.surname = self.io.input('фамилию \n', 'string')
        self.salary = self.io.input('зарплату \n', 'float')
        self.activity_scope = self.io.input('сферу деятельности \n', 'string')

    def write(self):
        self.io.output('ID', self.id)
        self.io.output('Имя', self.first_name)
        self.io.output('Фамилия', self.surname)
        self.io.output('Зарплата', str(self.salary) + "рублей")
        self.io.output('Сфера деятельности', self.activity_scope)

