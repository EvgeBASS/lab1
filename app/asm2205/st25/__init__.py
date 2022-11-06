from flask import Blueprint
from flask import g, request, jsonify
from app.asm2205.st25.model import *
from app.asm2205.st25.hospital import Hospital

bp = Blueprint('0525', __name__)

def GetHospital():
    if 'hospital' not in g:
        g.hospital = Hospital()
    return g.hospital

@bp.route("/")
def hospitalindex():
    return GetHospital().FlaskAPI.ShowHospital()


@bp.route("/init_form/<int:id>")
def showform(id):
    return GetHospital().FlaskAPI.ShowForm(id)


@bp.route("/delete/<int:id>")
def deleteitem(id):
    return GetHospital().FlaskAPI.Delete(id)


@bp.route("/add", methods=['POST'])
def add():
    return GetHospital().FlaskAPI.Add()


@bp.teardown_request
def teardown_hospital(t):
    GetHospital().storage.Store()


# API
@bp.route("/api/", methods=['GET'])
def HTTPGetHospital():
    data = list(GetHospital().FlaskAPI.storage.GetItems())
    return jsonify(data)


@bp.route("/api/", methods=['POST'])
def HTTPPostHospital():
    data = request.json
    GetHospital().FlaskAPI.storage.DeleteAll()
    for it in data:
        type = it['class_type']
        if type == 2:
            item = HeadDoctor()
        elif type == 1:
            item = Doctor()
        else:
            item = Nurse()
        for key in it:
            item.__setattr__(key, it[key])
        GetHospital().FlaskAPI.storage.Add_2(item)
    return ''

if __name__ == "__main__":
    app.run(debug=True)
