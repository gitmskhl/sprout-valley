import pygame

from .entity import PhysicEntity
from .animation import AnimationManager

class Player(PhysicEntity):
    def __init__(self, pos, vel):
        super().__init__(pos, vel)
        # set up animations
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
        self.anim_manager.set_anim_prop(
            anim_pattern_func=lambda name: name[-3:] in ('axe', 'hoe') or name[-5:] == 'water',
            prop='repeat',
            val=False
        )

        self.state = 'down'

        # tools
        self.tool_using = False     # If True then the player is using a tool
        self.tools = ('axe', 'hoe', 'water')
        self.current_tool = 'hoe'

        # seeds
        self.seeds = ('corn', 'tomato')
        self.current_seed_idx = 0


    def render(self, surf, camera):
        self.anim_manager.render(surf, self.pos[0] - camera[0], self.pos[1] - camera[1])
    
    def update(self):
        if not self.tool_using: self.make_move() # the player can not move if he uses a tool 
        self.set_status()
        self.anim_manager.set_animation(self.state)
        self.anim_manager.update()

    def set_status(self):
        if self.tool_using:
            if self.anim_manager.finished:  self.tool_using = False
            else:                           return
        if self.move[0]: self.state = 'up'
        elif self.move[1]: self.state = 'right'
        elif self.move[2]: self.state = 'down'        
        elif self.move[3]: self.state = 'left'
        elif self.direction == PhysicEntity.DOWN: self.state = 'down_idle'
        elif self.direction == PhysicEntity.UP: self.state = 'up_idle'
        elif self.direction == PhysicEntity.LEFT: self.state = 'left_idle'
        elif self.direction == PhysicEntity.RIGHT: self.state = 'right_idle'

    def use_tool(self):
        if not self.tool_using:
            self.tool_using = True
            if self.direction == PhysicEntity.DOWN: self.state = 'down'
            elif self.direction == PhysicEntity.UP: self.state = 'up'
            elif self.direction == PhysicEntity.LEFT: self.state = 'left'
            elif self.direction == PhysicEntity.RIGHT: self.state = 'right'
            self.state = '%s_%s' % (self.state, self.current_tool)

    def switch_tool(self):
        if not self.tool_using:
            idx = (self.tools.index(self.current_tool) + 1) % len(self.tools)
            self.current_tool = self.tools[idx]

    def use_seed(self):
        raise NotImplementedError

    def switch_seed(self):
        self.current_seed_idx = (self.current_seed_idx + 1) % len(self.seeds)

    def get_rect():
        pass