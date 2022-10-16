from dataclasses import dataclass

from app.asm2204.st21.feature.models.Creature import Creature
from app.asm2204.st21.feature.strategy.simple.JsonStrategy import JsonStrategy
from app.asm2204.st21.database.db_config import DBConfig
from app.asm2204.st21.feature.models.Note import Note
from app.asm2204.st21.feature.strategy.IO.PickleStrategy import PickleStrategy
from app.asm2204.st21.feature.strategy.simple.SimpleStrategy import SimpleStrategy


@dataclass
class Notebook:
    id = 0
    strategy: SimpleStrategy

    def __init__(self):
        self.id = 0
        self.__notes = []

    def set_strategy(self, strategy):
        self.strategy = strategy

    def init_notebook(self):
        self.id = self.strategy.read_param('int', 'id')

    def get_notes(self):
        notes_json, creatures_json = DBConfig.get_notes(self.id)

        notes = []

        for note_json in notes_json:
            note = Note(JsonStrategy(note_json))
            note.set_note()

            notes.append(note)

        for creature_json in creatures_json:
            creature = Creature(JsonStrategy(creature_json))
            creature.set_note()

            notes.append(creature)

        return notes

    def add_note(self, note):
        return DBConfig.add_to_notebook(self.id, note)

    def edit_note(self, note):
        return DBConfig.edit_notebook(note)

    def delete_note(self, id, type):
        return DBConfig.delete_from_notebook(id, type)

    def load_from_file(self):
        local_strategy = PickleStrategy([])

        notes = local_strategy.read()

        for note in notes:
            self.add_note(note)

        return notes
