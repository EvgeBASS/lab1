from abc import ABC, abstractmethod


class SimpleStrategy(ABC):
    __source = None

    @abstractmethod
    def read_param(self, param_type, param_name):
        pass

    @abstractmethod
    def write_params(self, param_names):
        pass
