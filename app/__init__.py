from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

# добавить импорт своего модуля по шаблону
from app.asm2204.st00 import bp as bp0400
from app.asm2204.st08 import bp as bp0408
from app.asm2205.st00 import bp as bp0500
from app.aam2207.st00 import bp as bp0700
# добавить пункт меню для вызова своего модуля по шаблону:


bps = [
	["[2204-00] Образец 2204", bp0400],
	["[2204-08] Довиденков 2204", bp0408],
	["[2205-00] Образец 2205", bp0500],
	["[2207-00] Образец 2207", bp0700],
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
