from abc import abstractmethod, ABC


class IOStrategy(ABC):
    def __init__(self, notes):
        self.notes = notes

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
