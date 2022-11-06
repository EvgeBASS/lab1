from clients.asm2204.st25.IO.IOStrategy import IOStrategy
from clients.asm2204.st25.utilities.utilities import Utilities


class ConsoleIO(IOStrategy):

    def input(self, field, data_type):
        while True:
            result = input(f"Введите {field}")
            if data_type == 'float':
                result = Utilities.float_check(result)
            elif data_type == 'int':
                result = Utilities.int_check(result)
            if result is not None:
                return result
            else:
                print("Введите корректное значение")

    def output(self, title, field=""):
        print(f"{title}: {field}")
