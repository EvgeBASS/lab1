from .IOStrategy import IOStrategy
from flask import request

class RestIO(IOStrategy):

    def input(self, field, value=None):
        value = request.json[field]
        return value

    def output(self, item):
        print(item)