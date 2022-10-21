from app.asm2204.st21.feature.strategy.simple.ConsoleStrategy import ConsoleStrategy
from app.asm2204.st21.feature.utils.Menu import Menu
from clients.asm2204.st21.ConsoleApp import ConsoleApp


def main():
    app = ConsoleApp()

    app.set_strategy(ConsoleStrategy(''))

    menu_options = [
        {'title': 'Вывести на экран весь список', 'command': app.show_notes},
        {'title': 'Добавить объект выбранного типа', 'command': app.add_note},
        {'title': 'Редактировать', 'command': app.edit_note},
        {'title': 'Удалить объект', 'command': app.delete_note},
        {'title': 'Загрузить из файла', 'command': app.load_from_file},
        {'title': 'Выход', 'command': None}
    ]

    menu = Menu('Меню:', list([str(item['title']) for item in menu_options]))

    while True:
        command = menu.show_menu()

        if command == len(menu_options):
            break
        else:
            try:
                menu_options[command - 1]['command']()
            except Exception as e:
                print('Некорректное значение')


if __name__ == '__main__':
    main()
