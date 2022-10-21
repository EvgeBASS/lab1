from flask import Flask
from flask import g, request


app = Flask(__name__)

if __name__ == '__main__':
    from group import Group
else:
    from .group import Group


def getGroup():
    if 'group' not in g:
        g.group = Group()
    return g.group


@app.route("/")
def showGroup():
    return getGroup().showGroup()

@app.route("/showform/<int:id>")
def showform(id):
    phone = request.form.get('phone_number')
    if phone == '':
        return getGroup().showForm(id)
    else:
        print('zashol')
        return getGroup().showForm(id, True)

@app.route("/delete/<int:id>")
def deleteitem(id):
    return getGroup().delete(id)

@app.route("/deleteAll")
def deleteAllitem():
    return getGroup().deleteAll()

@app.route("/add", methods=['POST'])
def add():
    phone = request.form.get('phone_number')
    if phone == '':
        return getGroup().add(False)
    else:
        return getGroup().add(True)

@app.teardown_appcontext
def teardown_group(ctx):
    getGroup().storage.store()


if __name__ == '__main__':
    app.run(debug=True)


