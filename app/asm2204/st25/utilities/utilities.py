class Utilities:

    @staticmethod
    def float_check(value):
        try:
            return float(value)
        except:
            return None

    @staticmethod
    def int_check(value):
        try:
            return int(value)
        except:
            return None

    @staticmethod
    def input_check(value, min_value, max_value):
        try:
            if int(value) >= min_value or int(value) <= max_value:
                    return True
            else:
                print(f"{value} не входит в интервал от {min_value} до {max_value}")
                return False
        except:
            return False