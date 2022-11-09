from flask import *
from .classIO import classIO
from .dbClass import dbClass
from .restIO import RestIO
from .wolf import Wolf
from .dog import Dog

class Depository:

    def __init__(self):
        self.dbStorage = dbClass()
        self.restio = RestIO(request)

    def add(self, entity):
        entity.add()
        self.dbStorage.add(entity)

    def killAll(self):
        self.dbStorage.deleteAll()

    def showZoo(self):
        return render_template('asm2205/st12/storage.tpl', object=object, items=self.dbStorage.getItems(), selfurl='/'+request.url_rule.rule.split('/')[1])

    def show(self, id):
        item = self.dbStorage.getItem(id)
        return render_template('asm2205/st12/editer.tpl', uid=id, object=item, selfurl='/'+request.url_rule.rule.split('/')[1])

    def killEntity(self, id):
        self.dbStorage.delete(id)

    def edit(self):
        id =classIO().responseContext('id')
        for entity in self.dbStorage.getItems():
            if int(entity.id) == int(id):
                entity.baseAdd()
                self.dbStorage.edit(entity)
                break

    def apiStaff(self):
        ids = []
        for item in self.dbStorage.getItems():
            ids.append([item.id])
        return jsonify({'ids': ids})

    def determineById(self, id):
        return Wolf() if str(id)[0].__eq__('0') else Dog()

    def apiAdd(self, id):
        print(request.json)
        item = self.determineById(id)
        item.input(self.restio)
        self.dbStorage.add(item)
        return ''

    def apiGet(self, id):
        item = self.dbStorage.getItem(id)
        print(item.__dict__)
        return jsonify(item.__dict__)

    def apiSet(self, id):
        item = self.determineById(id)
        item.input(self.restio)
        self.dbStorage.edit(item)
        return ''

    def apiDelete(self, id):
        self.dbStorage.delete(id)
        return ''

    def apiClear(self):
        self.dbStorage.deleteAll()
        return ''
