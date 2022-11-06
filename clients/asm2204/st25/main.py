from clients.asm2204.st25.containers.team import Team
from clients.asm2204.st25.utilities.menu import Menu

if __name__ == '__main__':
    from group import group
else:
    from .group import group


def main():
    group().f()
    team = Team()
    commands = [
        ['Добавить', team.add],
        ['Удалить', team.delete],
        ['Изменить', team.edit],
        ['Показать', team.show],
        ['Очистить', team.clear],
        ['Выход'],
    ]
    menu = Menu(commands)
    while True:
        if menu.show() is not True:
            break


if __name__ == '__main__':
	main()


