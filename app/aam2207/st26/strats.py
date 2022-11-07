from app.aam2207.st26.utils import *

class ConsoleWorker:
    def console_input_atr(self, atr_name):
        setattr(self, atr_name, functions_in[atr_name]())

    def output(self):
        print('*' * 60)
        print(self)
        print('*' * 60)


def name():
    return input("Имя:")


def surname():
    return input("Фамилия:")


def size():
    print("Размер:", end='.')
    return my_int_input()


def battle_cry():
    return input("Боевой клич:").upper() + '!'


def color():
    colors = ['Красный', 'Зелённый', 'Жёлтый',
              'Синий', 'Фиолетоый', 'Бирюзовый']
    print("Число цвета: ")
    print_menu(colors)
    return colors[my_int_input(0, len(colors) - 1)]


functions_in = { 'name': name, 'surname': surname, 'size': size, 'battle_cry': battle_cry, 'color': color}
