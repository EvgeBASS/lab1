from flask import render_template, request


class WebIO:
    def __init__(self, io):
        self.io = io

    def input(self, item, value=None):
        return self.io.form.get(item, value)

    def output(self, item):
        return render_template('asm2205/st06/form.tpl', it=item, selfurl='/'+request.url_rule.rule.split('/')[1])