import json

from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy


class CustomEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, SimpleStrategy):
            return None

        return {'__{}__'.format(o.__class__.__name__): o.__dict__}
