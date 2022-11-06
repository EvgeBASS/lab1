from abc import abstractmethod, ABC


class IOStrategy(ABC):
    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self):
        pass
