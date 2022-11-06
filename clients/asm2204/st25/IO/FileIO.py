import pickle
from asm2204.st25.IO.IOStrategy import IOStrategy


class FileIO(IOStrategy):

    def __init__(self, team):
        self.team = team

    def input(self):
        pickle.dump((self.team.maxID, self.team.members), open("asm2204/st25/data.dat", "wb"))

    def output(self):
        (self.team.maxID, self.team.members) = pickle.load(open("asm2204/st25/data.dat", "rb"))
