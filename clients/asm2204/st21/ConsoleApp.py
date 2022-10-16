import json

import requests

from app.asm2204.st21 import JsonStrategy, CustomEncoder
from app.asm2204.st21.feature.models.Creature import Creature
from app.asm2204.st21.feature.models.Note import Note
from app.asm2204.st21.feature.strategy.simple.ConsoleStrategy import ConsoleStrategy
from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy
from app.asm2204.st21.feature.utils.Menu import Menu


class ConsoleApp:
    st: str = ""
    strategy: SimpleStrategy

    def __init__(self):
        self.get_st()

    note_types = {
        'NOTE': Note,
        'CREATURE': Creature
    }

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_request(self, method, cmd="", data=""):
        try:
            url = 'http://localhost:5000/' + self.st + 'api/'

            header = None

            if (len(data)):
                header = {"Content-type": 'application/json'}

            res = method(url + cmd, headers=header, data=json.dumps(data, cls=CustomEncoder))

            if res.status_code == 200:
                return json.loads(res.content)
            else:
                print("Ошибка при отправке запроса ", res.status_code)
        except Exception as e:
            print('Error: ',e)
            pass

    def get_st(self):
        res = self.do_request(requests.get)

        for i, title in res['sts']:
            if '[2204-21]' in title:
                self.st = 'st' + str(i) + '/'

                break

    def print_notes(self, notes):
        for index, note in enumerate(notes):
            print('Index: ', index, ' ', note.__str__())

    def show_notes(self):
        res = self.do_request(requests.get)

        notes = []

        try:
            for note in res:
                note = self.note_types[note['type']](JsonStrategy(note))

                note.set_note()

                notes.append(note)
        except Exception as e:
            print(e)

        self.print_notes(notes)

        return notes

    def add_note(self):
        options = list([str(item) for item in self.note_types])

        menu = Menu('Выберите тип: ', list([str(item) for item in self.note_types]))

        note = self.note_types[options[menu.show_menu() - 1]](ConsoleStrategy(''))
        note.set_note()

        res = self.do_request(requests.post, data=json.dumps(note.__dict__, cls=CustomEncoder))

        if res:
            print(res['message'])

    def edit_note(self):
        notes = self.show_notes()

        index = self.strategy.read_param('int', 'Index')

        note = self.note_types[notes[index].type](ConsoleStrategy(''))
        note.set_note()
        note.id = notes[index].id

        res = self.do_request(requests.put, data=json.dumps(note.__dict__, cls=CustomEncoder))

        if res:
            print(res['message'])

    def delete_note(self):
        notes = self.show_notes()

        index = self.strategy.read_param('int', 'Index')

        res = self.do_request(requests.delete, cmd=f'?id={notes[index].id}&type={notes[index].type}')

        if res:
            print(res['message'])

    def load_from_file(self):
        res = self.do_request(requests.get, cmd='load_from_file')

        if res:
            print(res['message'])