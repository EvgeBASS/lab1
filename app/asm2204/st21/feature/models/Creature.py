from app.asm2204.st21.feature.models.Note import Note


class Creature(Note):
    type: str = 'CREATURE'
    price: int = ''

    def set_note(self):
        super().set_note()
        self.type = 'CREATURE'
        self.price = self.strategy.read_param('int', 'price')

    def print_note(self):
        self.strategy.write_params(['title', 'description', 'price'])

    def __str__(self):
        return '\n Заголовок: {0} \n Описание: {1} \n Награда: {2}$ \n'.format(self.title, self.description, self.price)