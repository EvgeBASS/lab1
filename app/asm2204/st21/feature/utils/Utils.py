class Utils:
    @staticmethod
    def input_check(value, type='int', min_value=0, max_value=100):
        if type == 'int':
            try:
                if int(value) >= min_value or int(value) <= max_value:
                    return True
                print(f"{value} не входит в интервал от {min_value} до {max_value}")
                return False
            except:
                return False
        else:
            return True
