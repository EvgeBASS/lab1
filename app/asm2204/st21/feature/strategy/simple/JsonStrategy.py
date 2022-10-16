from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy


class JsonStrategy(SimpleStrategy):
    def __init__(self, source):
        self.__source = source

    def read_param(self, param_type, param_name):
        if self.__source == '' or self.__source is None:
            return None

        if param_type == 'str':
            return str(self.__source[param_name])

        if param_type == 'int':
            try:
                return int(self.__source[param_name])
            except Exception:
                return int(0)

        return None

    def write_params(self, param_names):
        return ''
