
from dataclasses import dataclass

from clients.asm2204.st25.models.team_member import TeamMember


@dataclass
class Analyst(TeamMember):
    experience_level: int = 0

    def read(self):
        super().read()
        self.experience_level = self.io.input( 'стаж \n', 'int')

    def write(self):
        super().write()
        self.io.output('Стаж', self.experience_level)

