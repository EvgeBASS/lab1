from flask import render_template
from flask import request
from flask import jsonify
from .PickleIO import PickleIO
from .WebIO import WebIO
from .DbIO import DbIO
from .RestIO import RestIO


class Staff:

    def __init__(self):
        self.storage = DbIO(self)
        self.io = WebIO(request)
        self.restio = RestIO(request)

    def form(self, id, isMaster=False):
        return self.storage.getItem(id, isMaster).output(self.io)

    def showStaff(self):
        return render_template('asm2205/st06/staff.tpl', items=self.storage.getItems(), selfurl='/'+request.url_rule.rule.split('/')[1])

    def add(self, isMaster):
        item = self.storage.getItem(int(self.io.input('id')), isMaster)
        item.input(self.io)
        self.storage.add(item)
        return self.showStaff()

    def delete(self, id):
        self.storage.delete(id)
        return self.showStaff()

    def clear(self):
        self.storage.clear()
        return self.showStaff()

    def apiStaff(self):
        ids = []
        for item in self.storage.getItems():
            if hasattr(item, 'grade'):
                isMaster = True
            else:
                isMaster = False
            ids.append([item.id, isMaster])
        return jsonify({'ids': ids})

    def apiAdd(self, isMaster):
        print(request.json)
        item = self.storage.getItem(0, bool(isMaster))
        item.input(self.restio)
        self.storage.add(item)
        return ''

    def apiGet(self, id, isMaster):
        item = self.storage.getItem(id, bool(isMaster))
        print(item.__dict__)
        return jsonify(item.__dict__)

    def apiSet(self, id):
        item = self.storage.getItem(id)
        item.input(self.restio)
        self.storage.add(item)
        return ''

    def apiDelete(self, id):
        self.storage.delete(id)
        return ''

    def apiClear(self):
        self.storage.clear()
        return ''
