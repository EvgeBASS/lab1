from .Trainer import Trainer
from .TrainerMaster import TrainerMaster
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
        if '[2205-06]' in title:
            myst = 'st' + str(i) + '/'
            print('My(st):', myst)
            return myst


class RestIO:
    def __init__(self, staff):
        self.staff = staff
        self.st = getlist()

    def getItem(self, id, isMaster=False):
        if isMaster:
            item = TrainerMaster()
        else:
            item = Trainer()
        if id > 0:
            res = DoRequest(requests.get, self.st, str(id) +"/"+str(int(isMaster)))
            item.__dict__.update(res)
        return item

    def add(self, item, isMaster=0):
        if item.id <= 0:
            DoRequest(requests.post, self.st, str(isMaster), item.__dict__)
        else:
            DoRequest(requests.put, self.st, str(item.id), item.__dict__)

    def delete(self, id='0'):
        DoRequest(requests.delete, self.st, id)

    def getItems(self):
        res = DoRequest(requests.get, self.st)
        for (id, isMaster) in res['ids']:
            if isMaster:
                yield self.getItem(id, isMaster)
            else:
                yield self.getItem(id)
