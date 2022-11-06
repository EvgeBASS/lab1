from app.asm2205.st25.hospital import *
import requests


class ClientHTTP:
    def __init__(self, API):
        self.st = None
        self.API = API

    def get_st(self):
        if self.st is None:
            data = requests.get("http://127.0.0.1:5000/api/").json()
            for it in data['sts']:
                if "[2205-25]" in it[1]:
                    self.st = it[0]

    def GetAirlines(self):
        if self.st is None:
            self.get_st()
        data = requests.get(f"http://127.0.0.1:5000/st{self.st}/api/").json()
        self.API.storage.DeleteAll()
        for it in data:
            class_type = it['class_type']
            if class_type == 2:
                item = HeadDoctor()
            elif class_type == 1:
                item = Doctor()
            else:
                item = Nurse()
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
        ["Добавить человека", CAPI.Add],
        ["Показать", CAPI.Show],
        ["Изменить", CAPI.Edit],
        ["Сохранить в файл", CAPI.AirlinesTofile],
        ["Загрузить из файла", CAPI.AirlinesFromFile],
        ["Удалить", CAPI.Delete]

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