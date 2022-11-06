import pickle
from .IOStrategy import IOStrategy

import os

class FileIO(IOStrategy):

    def __init__(self, team):
        self.team = team

    def input(self):
        pickle.dump(self.team.members, open(os.getcwd()+"/data/asm2204/st25/data.dat", "wb"))

    def output(self):
        self.team.members = pickle.load(open(os.getcwd()+"/data/asm2204/st25/data.dat", "rb"))
