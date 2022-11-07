from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

# добавить импорт своего модуля по шаблону
from app.asm2204.st00 import bp as bp0400
from app.asm2204.st08 import bp as bp0408
from app.asm2205.st00 import bp as bp0500
from app.aam2207.st00 import bp as bp0700
from app.asm2204.st21 import bp as bp0421
from app.asm2205.st16 import bp as bp0516
from app.asm2205.st06 import bp as bp0506
from app.asm2204.st25 import bp as bp0425
from app.asm2205.st24 import bp as bp0524
from app.asm2205.st25 import bp as bp0525
from app.aam2207.st26 import bp as bp0726

# добавить пункт меню для вызова своего модуля по шаблону:

bps = [
    ["[2204-00] Образец 2204", bp0400],
    ["[2204-08] Довиденков 2204", bp0408],
    ["[2205-00] Образец 2205", bp0500],
    ["[2207-00] Образец 2207", bp0700],
    ["[2204-21] Мельников 2204", bp0421],
    ["[2205-16] Матвеев 2205", bp0516],
    ["[2205-06] Емельянова 2205", bp0506],
    ["[2204-25] Селезнев 2204", bp0425],
    ["[2205-24] Халявина 2205", bp0524],
    ["[2205-25] Харисова 2205", bp0525],
    ["[2207-26] Юхацков 2207", bp0726],
]

for i, (title, bp) in enumerate(sorted(bps), start=1):
    app.register_blueprint(bp, url_prefix=f"/st{i}")


@app.route("/")
def index():
    return render_template("index.tpl", bps=sorted(bps))


@app.route("/api/", methods=['GET'])
def api():
    sts = []
    for i, (title, bp) in enumerate(sorted(bps), start=1):
        sts.append([i, title])
    return jsonify({'sts': sts})
