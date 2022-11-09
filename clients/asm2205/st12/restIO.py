from .wolf import Wolf
from .dog import Dog
import requests
import json


def DoRequest(method, st="", cmd="", data=""):
    try:
        url = 'http://localhost:5000/'+st+'api/'
        header = None
        if(len(data)):
            header = {"Content-type": 'application/json'}
        res = method(url+cmd, headers=header, data=json.dumps(data))
        if res.status_code == 200:
            return json.loads(res.content)
    except Exception as e:
        pass


def getlist():
    res = DoRequest(requests.get)
    for i,title in res['sts']:
        if '[2205-12]' in title:
            myst = 'st' + str(i) + '/'
            print('My(st):', myst)
            return myst

def determineById(id):
    return Wolf() if str(id)[0].__eq__('0') else Dog()

class restIO:
    def __init__(self, storage):
        self.storage = storage
        self.st = getlist()

    def getItem(self, id):
        item = determineById(id)
        res = DoRequest(requests.get, self.st, str(id))
        item.__dict__.update(res)
        return item

    def add(self, item):
        if item.id != item.iD():
            DoRequest(requests.post, self.st, str(item.id), item.__dict__)
        else:
            DoRequest(requests.put, self.st, str(item.id), item.__dict__)

    def delete(self, id):
        DoRequest(requests.delete, self.st, id)

    def getItems(self):
        res = DoRequest(requests.get, self.st)
        s =[]
        for (id) in res['ids']:
            s.append(self.getItem(id[0]))
        return s