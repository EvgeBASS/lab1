from flask import render_template, request

class ConsoleInputOutput:
    def Input(self, field):
        return input(f"{field}:")

    def Output(self, item):
        print(item)


class FlaskInputOutput:
    def __init__(self, request):
        self.form = request.form

    def Input(self, field):
        return self.form.get(field)

    def Output(self, item):
        return render_template('asm2205//st25//init_form.tpl', it=item, selfurl='/'+request.url_rule.rule.split('/')[1])