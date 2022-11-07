from flask import Flask, Blueprint, render_template, request, jsonify, json
from app.aam2207.st26.chickenWorld import FlaskChickenWorld

bp = Blueprint('0726', __name__, static_folder='static', template_folder='templates')
# класс инициализируется позже
chicken_world = FlaskChickenWorld()

@bp.route('/')
def index():
    chicken_world.selfInit()
    return render_template("form.html", items = chicken_world.chickens, len = len(chicken_world.chickens), selfurl='/' + request.url_rule.rule.split('/')[1] )

@bp.route('/', methods = ["POST"])
def add():
    chicken_world.selfInit()
    if "addChicken" in request.form:
        chicken_world.add_kura(chicken_world.types[0][1])
    if "addSuperChicken" in request.form:
        chicken_world.add_kura(chicken_world.types[1][1])
    if "addBrolBoy" in request.form:
        chicken_world.add_kura(chicken_world.types[2][1])
    if "save" in request.form:
        for i, it in enumerate(chicken_world.chickens):
            for j in it.atrs:
                val = request.form[f"{i}{j}"]
                if val != "":
                    chicken_world.chickens[i].__setattr__(j, val)
        chicken_world.chikens_to_file()
    if "load" in request.form:
        chicken_world.chikens_from_file()
    for key in request.form:
        if 'delete' in key:
            index = int(key.removesuffix('delete') )
            del chicken_world.chickens[index]
    return render_template("form.html", items = chicken_world.chickens, len = len(chicken_world.chickens), selfurl='/' + request.url_rule.rule.split('/')[1])


# API
@bp.route("/api/", methods=['GET'])
def HTTPGetAirlines():
    chicken_world.selfInit()
    return jsonify(chicken_world.chickens)


@bp.route("/api/", methods=['POST'])
def HTTPPostAirlines():
    chicken_world.selfInit()
    chicken_world.send_for_sale()
    data = request.json
    for it in data:
        item = chicken_world.dictTypes[it['class_type']]()
        for key in it:
            item.__setattr__(key, it[key])
        chicken_world.chickens.append(item)
    return ''


@bp.teardown_request
def teardown_airlines(ctx):
    pass









