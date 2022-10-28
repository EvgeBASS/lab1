from flask import Blueprint
from flask import g, request

bp = Blueprint('st0506', __name__)

if __name__ == '__init__':
    from Staff import Staff
else:
    from .Staff import Staff


def staff():
    if 'staff' not in g:
        g.staff = Staff()
    return g.staff


@bp.route("/")
def showStaff():
    return staff().showStaff()


@bp.route("/form/<int:id>")
def form(id):
    return staff().form(id)


@bp.route("/delete/<int:id>")
def delete(id):
    return staff().delete(id)


@bp.route("/clear")
def clear():
    return staff().clear()


@bp.route("/add", methods=['POST'])
def add():
    grade = request.form.get('grade')
    if grade == '':
        return staff().add(False)
    else:
        return staff().add(True)


@bp.teardown_request
def teardown_group(ctx):
    staff().storage.store()


@bp.route("/api/", methods=['GET'])
def apiStaff():
    return staff().apiStaff()


@bp.route("/api/<int:isMaster>", methods=['POST'])
def apiAdd(isMaster):
    return staff().apiAdd(isMaster)


@bp.route("/api/<int:id>/<int:isMaster>", methods=['GET'])
def apiGet(id, isMaster):
    return staff().apiGet(id, isMaster)


@bp.route("/api/<int:id>", methods=['PUT'])
def apiSet(id):
    return staff().apiSet(id)


@bp.route("/api/<int:id>", methods=['DELETE'])
def apiDelete(id):
    if id == 0:
        return staff().apiClear()
    else:
        return staff().apiDelete(id)