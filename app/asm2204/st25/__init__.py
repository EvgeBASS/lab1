from flask import Flask, request, render_template, redirect, Blueprint,g
from .group import group
import os

app = Flask(__name__)

if __name__ == '__init__':
    from containers.team import Team
else:
    from .containers.team import Team

bp = Blueprint('st0425', __name__, template_folder=os.getcwd()+"/app/templates/asm2204/st25/")


@bp.before_request
def preHandler():
    g.team = Team()
    g.team.SQLStorage.load()


@bp.route('/')
def index():
    return g.team.showMembers()


@bp.route('/add', methods=['POST'])
def add():
    submit = request.form['submit']
    if submit == 'Добавить разработчика':
        g.team.addMember(False)
        return g.team.showMembers()
    elif submit == 'Добавить аналитика':
        g.team.addMember(True)
        return g.team.showMembers()


@bp.route("/delete/<int:id>")
def delete(id):
    g.team.deleteMember(id)
    return g.team.showMembers()

@bp.route("/edit/<int:id>")
def edit(id):
    g.team.edit(id)
    return g.team.showMembers()

@bp.route("/load_from_file", methods=['POST'])
def load_from_file():
    g.team.loadMembers()
    return g.team.showMembers()

@bp.route("/load_to_file", methods=['POST'])
def load_to_file():
    g.team.saveMembers()
    return g.team.showMembers()


@bp.route("/api/", methods=['GET'])
def apiTeam():
    return g.team.apiTeam()

@bp.route("/api/<int:id>", methods=['GET'])
def apiTeamMember(id):
    return g.team.apiTeamMember(id)

@bp.route("/api/<int:flag>", methods=['POST'])
def apiAdd(flag):
    return g.team.apiAddMember(flag)

@bp.route("/api/<int:id>", methods=['DELETE'])
def apiDelete(id):
    return g.team.apiDelete(id)

@bp.route("/api/clear/", methods=['DELETE'])
def apiClear():
    return g.team.apiClear()

@bp.route("/api/<int:id>", methods=['PUT'])
def apiEdit(id):
    return g.team.apiEdit(id)