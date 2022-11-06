import json

import requests

from clients.asm2204.st25.models.analyst import Analyst
from clients.asm2204.st25.models.developer import Developer


class RestIO:

    def __init__(self):
        self.st = getSt()

    def getTeam(self):
        return DoRequest(requests.get, self.st)

    def getMember(self, id):
        return DoRequest(requests.get, self.st, str(id))

    def addMember(self, member):
        if type(member) == Analyst:
            DoRequest(requests.post, self.st, str(1), member)
        else:
            DoRequest(requests.post, self.st, str(0), member)

    def deleteMember(self, id):
        DoRequest(requests.delete, self.st, str(id))

    def clearTeam(self):
        DoRequest(requests.delete, self.st)

    def editMember(self, member):
        DoRequest(requests.put, self.st, str(member["id"]), member)


def DoRequest(method, st="", content="", data=""):
    url = 'http://localhost:5000/' + st + 'api/'
    headers = None
    if len(data) != 0:
        headers = {"Content-type": 'application/json'}
    res = method(url + content, headers=headers, data=json.dumps(data))
    if res.status_code == 200:
        try:
            return json.loads(res.content)
        except:
            return ""


def getSt():
    res = DoRequest(requests.get)
    for i, title in res['sts']:
        if '[2204-25]' in title:
            st = 'st' + str(i) + '/'
            return st

def dictToModel(dict):
    try:
        if dict['experience_level']:
            member = Analyst(
                    id=dict["id"],
                    first_name=dict['first_name'],
                    surname=dict['surname'],
                    salary=dict['salary'],
                    activity_scope=dict['activity_scope'],
                    experience_level=dict['experience_level'],)
    except:
        if dict['skills_level']:
            member = Developer(
                    id=dict["id"],
                    first_name=dict['first_name'],
                    surname=dict['surname'],
                    salary=dict['salary'],
                    activity_scope=dict['activity_scope'],
                    skills_level=dict['skills_level'],)
    return member


def serializeMember(member):
    if type(member) == Developer:
        return {"id": member.id,
                "first_name": member.first_name,
                "surname": member.surname,
                 "salary": member.salary,
                 "activity_scope": member.activity_scope,
                 "skills_level": member.skills_level}
    else:
        return {"id": member.id,
                 "first_name": member.first_name,
                "surname": member.surname,
                "salary": member.salary,
                "activity_scope": member.activity_scope,
                "experience_level": member.experience_level}
