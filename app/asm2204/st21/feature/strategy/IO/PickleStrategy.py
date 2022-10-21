import os
import pickle

from app.asm2204.st21.feature.strategy.IO.IOStrategy import IOStrategy


class PickleStrategy(IOStrategy):
    def read(self):
        try:
            with open(os.getcwd() + '/data/asm2204/st21/notes.dumps', 'rb') as file:
                return pickle.load(file, encoding='bytes')['data']
        except Exception as e:
            print(e)
            print('Файл не найден')

            return list()

    def write(self):
        try:
            with open(os.getcwd() + '/data/asm2204/st21/notes.dumps', 'wb') as file:
                pickle.dump({'data': self.notes}, file)
        except Exception:
            print('Файл не найден')

            return list()
