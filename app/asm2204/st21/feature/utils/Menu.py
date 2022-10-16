from app.asm2204.st21.feature.utils.Utils import Utils


class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

        self.selected = 1
        self.menuLength = len(options)

    def show_menu(self):
        self.print_menu()

        while True:
            index = input('\nЧто делаем?: ', )

            if Utils.input_check(index, "int", 0, len(self.options) - 1):
                try:
                    self.selected = int(index)
                except Exception:
                    print('Некорректное значение')

                break
            else:
                self.print_menu()

        return self.selected

    def print_menu(self):
        print('\n')
        print(self.title)
        for i, item in enumerate(self.options):
            print(
                "{0}. {1}".format(i+1, item))
