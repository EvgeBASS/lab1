from dataclasses import dataclass
from flask import render_template, jsonify, request, Response
import sqlite3
import os

from app.asm2204.st25.IO.FileIO import FileIO
from app.asm2204.st25.IO.RestIO import RestIO
from app.asm2204.st25.IO.SQLIO import SQLIO
from app.asm2204.st25.models.analyst import Analyst
from app.asm2204.st25.models.developer import Developer


@dataclass
class Team:
    def __init__(self):
        self.members = dict()
        self.storage = FileIO(self)
        self.SQLStorage = SQLIO()
        self.RestIO = RestIO()

        self.loadMembersFromDB()


    def loadMembersFromDB(self):
        for i in self.SQLStorage.getAllMembers():
            self.members[i.id] = i

    def addMember(self, flag):
        if not flag:
            developer = Developer()
            developer.read(True)
            self.members[developer.id] = developer
            self.SQLStorage.addMember(developer)

        else:
            analyst = Analyst()
            analyst.read(True)
            self.members[analyst.id] = analyst
            self.SQLStorage.addMember(analyst)

    def showMembers(self):
        return render_template('team.tpl', object=object, members=self.members.values())

    def saveMembers(self):
        self.storage.input()

    def loadMembers(self):
        self.storage.output()
        db = sqlite3.connect(os.getcwd() + '/data/asm2204/st25/team.sqlite')
        cursor = db.cursor()
        cursor.execute("delete from team")
        db.close()
        for i in self.members:
            self.SQLStorage.addMember(self.members[i])


    def deleteMember(self, id: int):
        self.SQLStorage.deleteMember(id)
        return self.showMembers()

    def clearMembers(self):
        self.members = {}
        self.SQLStorage.clear()
        return self.showMembers()

    def edit(self, id):
        self.members[id].read(False)
        self.SQLStorage.editMember(self.members[id])
        return self.showMembers()

    def apiTeam(self):
        return jsonify(self.members)

    def apiTeamMember(self, id):
        return jsonify(self.SQLStorage.getMember(id))

    def apiAddMember(self, flag):
        if not flag:
            developer = Developer(
                id=self.RestIO.input("id"),
                first_name=self.RestIO.input("first_name"),
                surname=self.RestIO.input("surname"),
                salary=self.RestIO.input("salary"),
                activity_scope=self.RestIO.input("activity_scope"),
                skills_level=self.RestIO.input("skills_level"),
            )
            self.members[developer.id] = developer
            self.SQLStorage.addMember(developer)
        else:
            analyst = Analyst(
                id=self.RestIO.input("id"),
                first_name=self.RestIO.input("first_name"),
                surname=self.RestIO.input("surname"),
                salary=self.RestIO.input("salary"),
                activity_scope=self.RestIO.input("activity_scope"),
                experience_level=self.RestIO.input("experience_level"),
            )
            self.members[analyst.id] = analyst
            self.SQLStorage.addMember(analyst)
            return Response(status=200)

    def apiDelete(self, id):
        self.SQLStorage.deleteMember(id)
        return Response(status=200)

    def apiClear(self):
        self.SQLStorage.clear()
        return Response(status=200)

    def apiEdit(self, id):
        if type(self.SQLStorage.getMember(id)) == Analyst:
            member = Analyst(
                id=id,
                first_name=self.RestIO.input("first_name"),
                surname=self.RestIO.input("surname"),
                salary=self.RestIO.input("salary"),
                activity_scope=self.RestIO.input("activity_scope"),
                experience_level=self.RestIO.input("experience_level"),
            )
        else:
            member = Developer(
                id=id,
                first_name=self.RestIO.input("first_name"),
                surname=self.RestIO.input("surname"),
                salary=self.RestIO.input("salary"),
                activity_scope=self.RestIO.input("activity_scope"),
                skills_level=self.RestIO.input("skills_level"),
            )
        self.SQLStorage.editMember(member)
        return Response(status=200)






