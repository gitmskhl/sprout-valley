import pygame

from .entity import PhysicEntity
from .animation import AnimationManager

class Player(PhysicEntity):
    def __init__(self, pos, vel):
        super().__init__(pos, vel)
        self.anim_manager = AnimationManager(
            folder_path='data/player',
            scales=1.5,
            periods=10,
            repeats=True
        )
        self.anim_manager.set_anim_prop(
            anim_pattern_func=lambda name: name[-4:] == 'idle',
            prop='period',
            val=15
        )
        self.state = 'down'

    def render(self, surf, camera):
        self.anim_manager.render(surf, self.pos[0] - camera[0], self.pos[1] - camera[1])
    
    def update(self):
        self.make_move()
        self.set_status()
        self.anim_manager.set_animation(self.state)
        self.anim_manager.update()

    def set_status(self):
        if self.move[0]: self.state = 'up'
        elif self.move[1]: self.state = 'right'
        elif self.move[2]: self.state = 'down'        
        elif self.move[3]: self.state = 'left'
        elif self.direction == PhysicEntity.DOWN: self.state = 'down_idle'
        elif self.direction == PhysicEntity.UP: self.state = 'up_idle'
        elif self.direction == PhysicEntity.LEFT: self.state = 'left_idle'
        elif self.direction == PhysicEntity.RIGHT: self.state = 'right_idle'


    def get_rect():
        pass