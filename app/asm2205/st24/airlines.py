import json
import requests

from .IO import *
from .model import Pilot
from .storage import *
from .utils import *


class Airlines:
    def __init__(self):
        # self.storage = DBStorage()
        self.storage = PickleStorage()
        self.FlaskAPI = FlaskAPI(self.storage)


class FlaskAPI:
    def __init__(self, stotrage):
        self.storage = stotrage
        self.io = FlaskInputOutput(request)

    def ShowForm(self, id):
        return self.storage.GetItem(id).Output(self.io)

    def ShowAirlines(self):
        return render_template('asm2205//st24//airlines.tpl', items=self.storage.GetItems(),
                               selfurl='/' + request.url_rule.rule.split('/')[1])

    def Add(self):
        item = self.storage.GetItem(int(self.io.Input('id')))
        item.class_type = 1 if request.form.get('Pilot') else 0
        item.__class__ = Pilot if item.class_type else Worker
        item.Input(self.io)
        self.storage.Add(item)
        return self.ShowAirlines()

    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowAirlines()

class ConsoleAPI:
    def __init__(self, storage):
        self.storage = storage
        self.io = ConsoleInputOutput()

    def Add(self):
        print("Добавить 1-рабочего, 2-пилота:", end="")
        item = Pilot() if my_int_input(1, 2) == 2 else Worker()
        item.Input(self.io)
        self.storage.Add(item)

    def Edit(self):
        if len(self.storage.items) == 0:
            print('Нет работников')
        else:
            print('Введите Id работника для изменения:')
            self.Show()
            id = my_int_input(0)
            if id in self.storage.items:
                self.storage.items[id].Input(self.io)
            else:
                print("Ключ не тот")

    def Delete(self):
        if len(self.storage.items) == 0:
            print('Нет работников')
        else:
            print('Введите Id работника для удаления:')
            self.Show()
            id = my_int_input(0)
            if id in self.storage.items:
                del self.storage.items[id]
            else:
                print("Ключ не тот")

    def Show(self):
        for item in self.storage.GetItems():
            item.Output(self.io)

    def AirlinesTofile(self):
        self.storage.Store()

    def AirlinesFromFile(self):
        self.storage.Load()
