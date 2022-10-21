from flask import Blueprint
from flask import g, request

# Изменить на свой код

bp = Blueprint('st16', __name__)

if __name__ == '__init__':
    from group import Group
else:
    from .group import Group


def getGroup():
    if 'group' not in g:
        g.group = Group()
    return g.group


@bp.route("/")
def showGroup():
    return getGroup().showGroup()

@bp.route("/showform/<int:id>")
def showform(id):
    return getGroup().showForm(id)

@bp.route("/delete/<int:id>")
def deleteitem(id):
    return getGroup().delete(id)

@bp.route("/deleteAll")
def deleteAllitem():
    return getGroup().deleteAll()

@bp.route("/add", methods=['POST'])
def add():
    phone = request.form.get('phone_number')
    if phone == '':
        return getGroup().add(False)
    else:
        print('ST')
        return getGroup().add(True)

@bp.teardown_request
def teardown_group(ctx):
    getGroup().storage.Store()


@bp.route("/api/", methods=['GET'])
def apibook():
    return getGroup().APIGroup()


@bp.route("/api/<int:flag>", methods=['POST'])
def apiadd(flag):
    return getGroup().APIAdd(flag)


@bp.route("/api/<int:id>/<int:flag>", methods=['GET'])
def apiget(id, flag):
    return getGroup().APIGet(id, flag)


@bp.route("/api/<int:id>", methods=['PUT'])
def apiset(id):
    return getGroup().APISet(id)


@bp.route("/api/<int:id>", methods=['DELETE'])
def apidelete(id):
    if id == 0:
        return getGroup().APIDeleteAll()
    else:
        return getGroup().APIDelete(id)