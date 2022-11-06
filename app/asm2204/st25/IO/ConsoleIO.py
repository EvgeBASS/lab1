from .IOStrategy import IOStrategy
from flask import request

class ConsoleIO(IOStrategy):

    def input(self, item):
        return request.form.get(item)

    def output(self, title, field=""):
        print(f"{title}: {field}")
