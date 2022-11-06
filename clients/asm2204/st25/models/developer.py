from dataclasses import dataclass

from clients.asm2204.st25.models.team_member import TeamMember


@dataclass
class Developer(TeamMember):
    skills_level: str = ''

    def read(self):
        super().read()
        self.skills_level = self.io.input('уровень навыков \n', 'string')

    def write(self):
        super().write()
        self.io.output('Уровень навыков', self.skills_level)

