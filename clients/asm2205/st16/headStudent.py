from .student import Student
from dataclasses import dataclass


@dataclass
class HeadStudent(Student):
    phone_number: str = ""

    def __str__(self):
        return Student.__str__(self) + f"Phone Number: {self.phone_number}\n"

    def input(self, io):
        Student.input(self, io)
        self.phone_number = io.input('Phone number: ')

