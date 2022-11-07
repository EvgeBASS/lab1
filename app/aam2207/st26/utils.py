def my_int_input(min_int=0, max_int=0xffff):
    while True:
        try:
            string_int = int(input())
            if not (min_int <= string_int <= max_int):
                raise ValueError('Выход за интервал')
            return string_int
        except ValueError:
            print('Ошибка при вводе числа')


def print_menu(commands):
    print('-' * 60)
    if isinstance(commands[0], list | tuple):
        for i, item in enumerate(commands):
            print(f'{i}. {item[0]}')
    else:
        for i, item in enumerate(commands):
            print(f'{i}. {item}')
    print('-' * 60)
