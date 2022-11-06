from .team_member import TeamMember
from dataclasses import dataclass


@dataclass
class Developer(TeamMember):
    skills_level: str = ''

    def read(self, flag):
        super().read(flag)
        if flag:
            self.skills_level = self.io.input('skills_level')
        else:
            self.skills_level = self.io.input('skills_level_edit'+str(self.id))

    def write(self):
        super().write()
        self.io.output('Уровень навыков', self.skills_level)
