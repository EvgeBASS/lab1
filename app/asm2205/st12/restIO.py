
class RestIO:
    def __init__(self, io):
        self.io = io

    def input(self, field, value=None):
        return self.io.json.get(field, value)

    def output(self, item):
        print(item)