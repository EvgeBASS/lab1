from .team_member import TeamMember
from dataclasses import dataclass



@dataclass
class Analyst(TeamMember):
    experience_level: int = 0

    def read(self, flag):
        super().read(flag)
        if flag:
            self.experience_level = self.io.input('experience_level')
        else:
            self.experience_level = self.io.input('experience_level_edit'+str(self.id))

    def write(self):
        super().write()
        self.io.output('Стаж', self.experience_level)
