from abc import abstractmethod, ABC

class PhysicEntity(ABC):
    UP      = 0
    RIGHT   = 1
    DOWN    = 2
    LEFT    = 3
    def __init__(self, pos, vel):
        self.pos = list(pos)
        self.vel = tuple(vel)
        vel_norm = (vel[0] ** 2 + vel[1] ** 2) ** .5
        max_ = max(abs(vel[0]), abs(vel[1]))
        self.diagonal_vel = (self.vel[0] / vel_norm * max_, self.vel[1] / vel_norm * max_)
        self.move = [False] * 4 # up, right, down, left
        self.direction = PhysicEntity.RIGHT

    def movex(self, vel):
        self.pos[0] += (self.move[1] - self.move[3]) * vel[0]
        if self.move[1]:
            self.direction = PhysicEntity.RIGHT
        elif self.move[3]:
            self.direction = PhysicEntity.LEFT

    def movey(self, vel):
        self.pos[1] += (self.move[2] - self.move[0]) * vel[1]
        if self.move[0]:
            self.direction = PhysicEntity.UP
        elif self.move[2]:
            self.direction = PhysicEntity.DOWN

    def make_move(self):
        if any(self.move[::2]) and any(self.move[1::2]): vel = self.diagonal_vel
        else: vel = self.vel
        self.movex(vel)
        self.movey(vel)

    @abstractmethod
    def get_rect(self):
        pass

