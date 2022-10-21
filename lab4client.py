import clients.asm2204.st00.main
import clients.asm2204.st08.main
import clients.asm2205.st00.main
import clients.aam2207.st00.main
import clients.asm2204.st21.main
import clients.asm2205.st16.main
# добавить импорт своего модуля по шаблону
# import clients.asm<код группы>.st<номер по журналу>.main

MENU = [
    ["[2204-00] Образец 2204", clients.asm2204.st00.main.main],
    ["[2204-08] Довиденков 2204", clients.asm2204.st08.main.main],
    ["[2205-00] Образец 2205", clients.asm2205.st00.main.main],
    ["[2207-00] Образец 2207", clients.aam2207.st00.main.main],
    ["[2204-00] Мельников 2204", clients.asm2204.st21.main.main],
    ["[2205-00] Матвеев 2205", clients.asm2205.st16.main.main],
]


def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


try:
    while True:
        sorted(MENU)[menu()][1]()
except Exception as ex:
    print(ex, "\nbye")
