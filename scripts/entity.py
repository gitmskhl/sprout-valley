from abc import abstractmethod, ABC

class PhysicEntity(ABC):
    def __init__(self, pos, vel):
        self.pos = list(pos)
        self.vel = tuple(vel)
        vel_norm = (vel[0] ** 2 + vel[1] ** 2) ** .5
        max_ = max(abs(vel[0]), abs(vel[1]))
        self.diagonal_vel = (self.vel[0] / vel_norm * max_, self.vel[1] / vel_norm * max_)
        self.move = [False] * 4 # up, right, down, left

    def movex(self, vel):
        self.pos[0] += (self.move[1] - self.move[3]) * vel[0]

    def movey(self, vel):
        self.pos[1] += (self.move[2] - self.move[0]) * vel[1]

    def make_move(self):
        if any(self.move[::2]) and any(self.move[1::2]): vel = self.diagonal_vel
        else: vel = self.vel
        self.movex(vel)
        self.movey(vel)

    @abstractmethod
    def get_rect(self):
        pass

