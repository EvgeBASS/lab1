import os
from flask import Blueprint
from flask import g, request, redirect

bp = Blueprint('st0512', __name__, template_folder=os.getcwd() + "\\app\\templates\\asm2205\\st12\\", )

if __name__ == '__main__':
    from Depository import Depository
    from wolf import Wolf
    from dog import Dog
else:
    from .Depository import Depository
    from .wolf import Wolf
    from .dog import Dog

def getStorage():
    if 'storage' not in g:
        g.storage = Depository()
    return g.storage

@bp.route('/')
def index():
    return getStorage().showZoo()


@bp.route('/add', methods=['POST'])
def add():
    addClick = request.form['tap']
    if addClick == 'CREATE AS Wolf':
        getStorage().add(Wolf())
        return index()
    elif addClick == 'CREATE AS Dog':
        getStorage().add(Dog())
        return index()


@bp.route("/kill/<int:id>")
def kill(id):
    getStorage().killEntity(id)
    return index()

@bp.route("/edit/<int:id>")
def editFields(id):
    return getStorage().show(id)

@bp.route("/edit", methods=['POST'])
def edit():
    getStorage().edit()
    return index()
@bp.route("/killAll" , methods=['POST'])
def killAll():
    getStorage().killAll()
    return index()

@bp.teardown_request
def teardown_group(ctx):
    try:
        getStorage().dbStorage.store()
    except AttributeError:
        pass

@bp.route("/api/", methods=['GET'])
def apiStaff():
    return getStorage().apiStaff()


@bp.route("/api/<int:id>", methods=['PUT'])
def apiAdd(id):
    return getStorage().apiAdd(id)


@bp.route("/api/<int:id>", methods=['GET'])
def apiGet(id):
    return getStorage().apiGet(id)


@bp.route("/api/<int:id>", methods=['POST'])
def apiSet(id):
    return getStorage().apiSet(id)


@bp.route("/api/<int:id>", methods=['DELETE'])
def apiDelete(id):
    if id == 0:
        return getStorage().apiClear()
    else:
        return getStorage().apiDelete(id)
