from flask import render_template
from flask import request

class group:
	def f(self):
		return render_template("asm2204/st25/base.tpl", s="asm2204.st25.group.f()", selfurl='/'+request.url_rule.rule.split('/')[1])
