import json
import requests

from .IO import *
from .model import *
from .storage import *
from .utils import *


class Hospital:
    def __init__(self):
        self.storage = DBStorage()
        # self.storage = PickleStorage()
        self.FlaskAPI = FlaskAPI(self.storage)


class FlaskAPI:
    def __init__(self, stotrage):
        self.storage = stotrage
        self.io = FlaskInputOutput(request)

    def ShowForm(self, id):
        return self.storage.GetItem(id).Output(self.io)

    def ShowHospital(self):
        return render_template('asm2205//st25//hospital.tpl', items=self.storage.GetItems(),
                               selfurl='/' + request.url_rule.rule.split('/')[1])

    def Add(self):
        item = self.storage.GetItem(int(self.io.Input('id')))
        post = request.form.get('post')
        ganarar = request.form.get('ganarar')

        if ganarar != None:
            item.__class__ = HeadDoctor
            item.class_type = 2
        elif post != None:
            item.__class__ = Doctor
            item.class_type = 1
        else:
            item.__class__ = Nurse
            item.class_type = 0

        item.Input(self.io)
        self.storage.Add(item)
        return self.ShowHospital()

    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowHospital()


class ConsoleAPI:
    def __init__(self, storage):
        self.storage = storage
        self.io = ConsoleInputOutput()

    def Add(self):
        print("Добавить 1-медсестру, 2-врача, 3-глав.врача:", end="")
        type = my_int_input(1, 3)
        if type == 3:
            item = HeadDoctor()
        elif type == 2:
            item = Doctor()
        else:
            item = Nurse()
        item.Input(self.io)
        self.storage.Add(item)

    def Edit(self):
        if len(self.storage.items) == 0:
            print('Добавьте сотрудников')
        else:
            print('Введите номер сотрудника требующий изменения:')
            self.Show()
            id = my_int_input(0)
            if id in self.storage.items:
                self.storage.items[id].Input(self.io)
            else:
                print("Ключ не тот")

    def Delete(self):
        if len(self.storage.items) == 0:
            print('Добавьте сотрудников')
        else:
            print('Какой элемент удалить:')
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
