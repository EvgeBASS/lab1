
class RESTInputOutput:
    def __init__(self, io):
        self.io = io

    def input(self, field, defval=None):
        return self.io.json.get(field, defval)

    def output(self, item):
        print(item)