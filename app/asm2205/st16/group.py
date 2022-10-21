from flask import render_template
from flask import request
from .PickleStorage import PickleStorage
from .FlaskIO import FlaskIO
from .RestIO import RESTInputOutput
from .DBIO import DBStorage
from flask import jsonify


class Group:

    def __init__(self):
        self.storage = DBStorage(self)
        self.io = FlaskIO(request)
        self.restio = RESTInputOutput(request)

    def showForm(self, id, flag=False):
        return self.storage.GetItem(id, flag).output(self.io)

    def showGroup(self):
        return render_template('asm2205/st16/group.tpl', items=self.storage.GetItems(), selfurl='/'+request.url_rule.rule.split('/')[1])

    def add(self, flag):
        item = self.storage.GetItem(int(self.io.input('id')), flag)
        item.input(self.io)
        self.storage.Add(item)
        return self.showGroup()

    def delete(self, id):
        self.storage.Delete(id)
        return self.showGroup()

    def deleteAll(self):
        self.storage.DeleteAll()
        return self.showGroup()

    def APIGroup(self):
        ids = []
        for item in self.storage.GetItems():
            if hasattr(item, 'phone_number'):
                flag = True
            else:
                flag = False
            ids.append([item.id, flag])
        return jsonify({'ids': ids})

    def APIAdd(self, flag):
        print('**********************')
        print(request.json)
        item = self.storage.GetItem(0, bool(flag))
        item.input(self.restio)
        self.storage.Add(item)
        return ''

    def APIGet(self, id, flag):
        item = self.storage.GetItem(id, bool(flag))
        print(item.__dict__)
        return jsonify(item.__dict__)

    def APISet(self, id):
        item = self.storage.GetItem(id)
        item.input(self.restio)
        self.storage.Add(item)
        return ''

    def APIDelete(self, id):
        self.storage.Delete(id)
        return ''

    def APIDeleteAll(self):
        self.storage.DeleteAll()
        return ''
