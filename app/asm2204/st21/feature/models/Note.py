from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy


class Note:
    id: int = 0
    type: str = 'NOTE'
    title: str = ''
    description: str = ''
    strategy: SimpleStrategy

    def __init__(self, strategy):
        self.type = 'NOTE'
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def set_note(self):
        self.id = self.strategy.read_param('int', 'id')
        self.title = self.strategy.read_param('str', 'title')
        self.description = self.strategy.read_param('str', 'description')

    def print_note(self):
        self.strategy.write_params(['title', 'description'])

    def __str__(self):
        return '\n Заголовок: {0} \n Описание: {1} \n'.format(self.title, self.description)