﻿from flask import render_template
from flask import request
from flask import jsonify

class group:
	def f(self):
		return render_template("aam2207/st00/index.tpl", s="aam2207.st00.group.f()", selfurl='/'+request.url_rule.rule.split('/')[1])

	def api(self):
		return jsonify({'st': 'aam2207.st00'})
