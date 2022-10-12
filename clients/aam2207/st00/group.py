﻿import requests
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
    for i, title in res['sts']:
        print(i, title)


class group:
	def f(self):
		print("aam2207.st00.group.f()")
		getlist()
		res = DoRequest(requests.get, "st3/")
		print(res)
