from app.aam2207.st26.chickenWorld import *
import requests, sys, json


class ClientHTTP:
    def __init__(self, API):
        self.st = None
        self.API = API

    def get_st(self):
        if self.st is None:
            data = requests.get("http://127.0.0.1:5000/api/").json()
            for it in data['sts']:
                if "[2207-26]" in it[1]:
                    self.st = it[0]

    def GetItems(self):
        if self.st is None:
            self.get_st()
        data = requests.get(f"http://127.0.0.1:5000/st{self.st}/api/").json()
        self.API.send_for_sale()
        for it in data:
            item = self.API.dictTypes[it['class_type']]()
            for key in it:
                item.__setattr__(key, it[key])
            self.API.chickens.append(item)

    def PostItems(self):
        ndata = []
        for it in self.API.chickens:
            ndata.append(it.__dict__)
        print(ndata)
        requests.post(f"http://127.0.0.1:5000/st{self.st}/api/", data=json.dumps(ndata), headers={"Content-type": 'application/json'})

def main():
    kuriatnik = ConsoleChickenWorld()
    kuriatnik.path = "data/aam2207/st26/"
    if __name__ == '__main__':
        kuriatnik.path = '../../../data/aam2207/st26/'

    CHTTP = ClientHTTP(kuriatnik)
    commands = [
        ["Добавить курицу", kuriatnik.add_kura],
        ["Редактировать курицу", kuriatnik.edit_kura],
        ["Продать курицу", kuriatnik.delete_kura],
        ["Вывести кур в курятнике", kuriatnik.output],
        ["Сохранить курятник в файл", kuriatnik.chikens_to_file],
        ["Выгрузить курятник из файла", kuriatnik.chikens_from_file],
        ["Изменить поведения сохранения/загрузки куриц", kuriatnik.setDataBehaviour],
        ["Выйти", kuriatnik.send_for_sale]
    ]
    while True:
        print_menu(commands)
        index = my_int_input(0, len(commands) - 1)
        try:
            if index == len(commands) - 1:
                break
            CHTTP.GetItems()
            commands[index][1]()
            CHTTP.PostItems()
        except Exception as ex:
            print(ex, "Error.\n")


if __name__ == '__main__':
    main()