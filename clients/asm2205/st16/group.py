from .RESTStorage import RESTStorage
from .ConsoleIO import ConsoleIO
from .student import Student
from .headStudent import HeadStudent
import requests
import json


class Group:

    def __init__(self):
        self.storage = RESTStorage(self)
        self.io = ConsoleIO()

    def ShowForm(self, id):
        return self.storage.GetItem(id).output(self.io)

    def ShowGroup(self):
        for item in self.storage.GetItems():
            item.output(self.io)

    def add(self):
        item = Student()
        item.input(self.io)
        self.storage.Add(item)

    def add_headStudent(self):
        item = HeadStudent()
        item.input(self.io)
        self.storage.Add(item, 1)

    def edit(self):
        item_edit = self.storage.GetItem(int(self.io.input("id: ")))
        item_edit.output(self.io)
        item_edit.input(self.io)
        self.storage.Add(item_edit)


    def delete(self):
        self.storage.Delete(self.io.input("id: "))

    def deleteAll(self):
        self.storage.Delete()

