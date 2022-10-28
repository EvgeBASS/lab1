from .Trainer import Trainer
from dataclasses import dataclass


@dataclass
class TrainerMaster(Trainer):
    grade: int = 0

    def __str__(self):
        return Trainer.__str__(self) + f"Grade: {self.grade}\n"

    def input(self, io):
        Trainer.input(self, io)
        self.grade = io.input('Grade: ')

