def my_int_input(min_int=0, max_int=0xffff):
    while True:
        try:
            string_int = int(input())
            if not (min_int <= string_int <= max_int):
                raise ValueError('Выход за интервал')
            return string_int
        except ValueError:
            print('Ошибка при вводе числа')