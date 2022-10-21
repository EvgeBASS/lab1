from dataclasses import dataclass
from .ConsoleIO import ConsoleIO


@dataclass
class Student:
    id: int = 0
    name: str = ''
    age: int = 0
    rate: int = 0
    stipend: float = 0.0

    def __str__(self):
        return f"ID: {self.id}\n"\
               f"Name: {self.name}\n"\
               f"Age: {self.age} y.o.\n"\
               f"Rate: {self.rate}/100\n"\
               f"Stipend: {self.stipend} RUB\n"

    def input(self, io):
        #self.id = int(io.input('id', self.id))
        self.name = io.input('Name: ')
        self.age = io.input('Age: ')
        self.rate = io.input('Rate: ')
        self.stipend = io.input('Stipend: ')

    def output(self, io):
        return io.output(self)

