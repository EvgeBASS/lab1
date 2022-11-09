import pickle

class FileIO:
    def writeNotes(self, staff):
        with open('storage.dat', 'wb') as f:
            pickle.dump(staff, f)

    def readNotes(self):
        with open('storage.dat', 'rb') as f:
            return pickle.load(f)