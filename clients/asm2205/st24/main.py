from app.asm2205.st24.airlines import *
import requests


class ClientHTTP:
    def __init__(self, API):
        self.st = None
        self.API = API

    def get_st(self):
        if self.st is None:
            data = requests.get("http://127.0.0.1:5000/api/").json()
            for it in data['sts']:
                if "[2205-24]" in it[1]:
                    self.st = it[0]

    def GetAirlines(self):
        if self.st is None:
            self.get_st()
        data = requests.get(f"http://127.0.0.1:5000/st{self.st}/api/").json()
        self.API.storage.DeleteAll()
        for it in data:
            item = Pilot() if it['class_type'] else Worker()
            for key in it:
                item.__setattr__(key, it[key])
            self.API.storage.Add(item)

    def PostAirlines(self):
        data = list(self.API.storage.GetItems())
        ndata = []
        for it in data:
            ndata.append(it.__dict__)
        requests.post(f"http://127.0.0.1:5000/st{self.st}/api/", data=json.dumps(ndata), headers={"Content-type": 'application/json'})

def main():
    storage = PickleStorage()
    CAPI = ConsoleAPI(storage)
    CHTTP = ClientHTTP(CAPI)

    menu = [
        ["Добавить", CAPI.Add],
        ["Показать", CAPI.Show],
        ["Редактировать", CAPI.Edit],
        ["Удалить", CAPI.Delete],
        ["Загрузить из файла", CAPI.AirlinesFromFile],
        ["Сохранить в файл", CAPI.AirlinesTofile]
    ]

    while True:
        for i, menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        try:
            m = int(input())
            CHTTP.GetAirlines()
            menu[m-1][1]()
            CHTTP.PostAirlines()
        except Exception as ex:
            print(ex, "Error.\n")



if __name__ == '__main__':
    main()