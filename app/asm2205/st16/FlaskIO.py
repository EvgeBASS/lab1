from flask import render_template, request


class FlaskIO:
    def __init__(self, io):
        self.io = io

    def input(self, item, defval=None):
        return self.io.form.get(item, defval)

    def output(self, item):
        return render_template('asm2205/st16/form.tpl', it=item, selfurl='/'+request.url_rule.rule.split('/')[1])