from flask import Blueprint
from flask import g, request, jsonify
from app.asm2205.st24.model import *
from app.asm2205.st24.airlines import Airlines

bp = Blueprint('0524', __name__)

def GetAirlines():
    if 'airlines' not in g:
        g.airlines = Airlines()
    return g.airlines


@bp.route("/")
def airlinesindex():
    return GetAirlines().FlaskAPI.ShowAirlines()


@bp.route("/showform/<int:id>")
def showform(id):
    return GetAirlines().FlaskAPI.ShowForm(id)


@bp.route("/delete/<int:id>")
def deleteitem(id):
    return GetAirlines().FlaskAPI.Delete(id)


@bp.route("/add", methods=['POST'])
def add():
    return GetAirlines().FlaskAPI.Add()


@bp.teardown_request
def teardown_airlines(t):
    GetAirlines().storage.Store()


# API
@bp.route("/api/", methods=['GET'])
def HTTPGetAirlines():
    data = list(GetAirlines().FlaskAPI.storage.GetItems())
    return jsonify(data)


@bp.route("/api/", methods=['POST'])
def HTTPPostAirlines():
    data = request.json
    GetAirlines().FlaskAPI.storage.DeleteAll()
    for it in data:
        item = Pilot() if it['class_type'] else Worker()
        for key in it:
            item.__setattr__(key, it[key])
        GetAirlines().FlaskAPI.storage.Add_2(item)
    return ''

if __name__ == "__main__":
    app.run(debug=True)
