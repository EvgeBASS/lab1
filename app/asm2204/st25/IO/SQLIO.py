import os
import sqlite3
from app.asm2204.st25.models.analyst import Analyst
from app.asm2204.st25.models.developer import Developer

path = 'data/asm2204/st25/'


class SQLIO:

    def __init__(self):
        self.load()

    def load(self):
        if not os.path.exists(path):
            os.mkdir(path)
        self.db = sqlite3.connect(path + 'team.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
    				   create table if not exists team(
    					   id integer primary key autoincrement,
    					   first_name text,
    					   surname text,
    					   salary float,
    					   activity_scope text,
    					   experience_level integer,
    					   skills_level str,
    					   role str
    					   )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def addMember(self, member):
        if type(member) == Developer:
            self.db.execute("insert into team (first_name, surname, salary, activity_scope,  skills_level, role) values(?, ?, ?, ?, ?, ?)",
                           (member.first_name, member.surname, member.salary, member.activity_scope, member.skills_level,"developer"))
        elif type(member) == Analyst:
            self.db.execute("insert into team (first_name, surname, salary, activity_scope,  experience_level, role) values(?, ?, ?, ?, ?, ?)",
                           (member.first_name, member.surname, member.salary, member.activity_scope, member.experience_level,"analyst"))
        self.db.commit()

    def getMember(self, id):
        self.dbc.execute("select * from team where id=?", (id,))
        m = self.dbc.fetchone()
        if m['role'] == 'developer':
            member = Developer(
                    id=id,
                    first_name=m['first_name'],
                    surname=m['surname'],
                    salary=m['salary'],
                    activity_scope=m['activity_scope'],
                    skills_level=m['skills_level'],
            )
        elif m['role'] == 'analyst':
            member = Analyst(
                id=id,
                first_name=m['first_name'],
                surname=m['surname'],
                salary=m['salary'],
                activity_scope=m['activity_scope'],
                experience_level=m['experience_level'],)
        return member

    def getAllMembers(self):
        self.dbc.execute("select * from team order by id desc")
        members = []
        for m in self.dbc:
            if m['role'] == 'analyst':
                member = Analyst(
                id = m['id'],
                first_name=m['first_name'],
                surname=m['surname'],
                salary=m['salary'],
                activity_scope=m['activity_scope'],
                experience_level=m['experience_level'],
            )
                members.append(member)
            elif m['role'] == 'developer':
                member = Developer(
                    id=m['id'],
                    first_name=m['first_name'],
                    surname=m['surname'],
                    salary=m['salary'],
                    activity_scope=m['activity_scope'],
                    skills_level=m['skills_level'], )
                members.append(member)
        return members

    def deleteMember(self, id):
        self.db.execute("delete from team where id=?", (id,))
        self.db.commit()

    def editMember(self, member):
        if type(member) == Developer:
            self.db.execute(
                "update team set first_name = ?, surname = ?, salary = ?, activity_scope = ?, skills_level = ? where id=?",
                (member.first_name, member.surname, member.salary, member.activity_scope, member.skills_level,
                 member.id))
        elif type(member) == Analyst:
            self.db.execute(
                "update team set first_name = ?, surname = ?, salary = ?, activity_scope = ?, experience_level = ? where id=?",
                (member.first_name, member.surname, member.salary, member.activity_scope, member.experience_level,
                 member.id))
        self.db.commit()

    def clear(self):
        self.db.execute("delete from team ")
        self.db.commit()
