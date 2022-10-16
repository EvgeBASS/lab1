from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy


class ConsoleStrategy(SimpleStrategy):
    def __init__(self, source):
        self.__source = source

    def read_param(self, param_type, param_name):
        if param_type == 'str':
            return str(input(param_name + ' : '))

        if param_type == 'int':
            while True:
                try:
                    param = int(input(param_name + ' : '))

                    break
                except Exception:
                    print('Некорректное значение')

            return param

        return None

    def write_params(self, param_names):
        if self.__source == '' or self.__source is None:
            print('Nothing to write')

        print(self.__source.__str__())

