from dataclasses import dataclass
from .ConsoleIO import ConsoleIO


@dataclass
class Trainer:
    id: int = 0
    firstname: str = ''
    lastname: str = ''
    age: int = 0
    experience: int = 0

    def __str__(self):
        return f"Id: {self.id}\n"\
               f"First name: {self.firstname}\n"\
               f"Last name: {self.lastname}\n"\
               f"Age: {self.age}\n"\
               f"Experience: {self.experience}\n"\


    def input(self, io):
        self.firstname = io.input('First name: ')
        self.lastname = io.input('Last name: ')
        self.age = io.input('Age: ')
        self.experience = io.input('Experience: ')

    def output(self, io):
        return io.output(self)

