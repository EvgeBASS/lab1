from .headStudent import HeadStudent
from .student import Student
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
        if '[2205-16]' in title:
            myst = 'st' + str(i) + '/'
            print('My(st):', myst)
            return myst


class RESTStorage:
    def __init__(self, group):
        self.group = group
        self.st = getlist()

    def GetItem(self, id, flag=False):
        if flag:
            item = HeadStudent()
        else:
            item = Student()
        if id > 0:
            res = DoRequest(requests.get, self.st, str(id) +"/"+str(int(flag)))
            item.__dict__.update(res)
        return item

    def Add(self, item, flag=0):
        if item.id <= 0:
            DoRequest(requests.post, self.st, str(flag), item.__dict__)
        else:
            DoRequest(requests.put, self.st, str(item.id), item.__dict__)

    def Delete(self, id='0'):
        DoRequest(requests.delete, self.st, id)

    def GetItems(self):
        res = DoRequest(requests.get, self.st)
        for (id, flag) in res['ids']:
            if flag:
                yield self.GetItem(id, flag)
            else:
                yield self.GetItem(id)
