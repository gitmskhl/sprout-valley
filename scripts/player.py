import pygame

from .entity import PhysicEntity

class Player(PhysicEntity):
    def __init__(self, pos, vel):
        super().__init__(pos, vel)
        self.surf = pygame.Surface((64, 64))
        self.surf.fill("green")
        
    def render(self, surf, camera):
        surf.blit(self.surf, (self.pos[0] - camera[0], self.pos[1] - camera[1]))
    
    def update(self):
        self.make_move()

    def get_rect():
        pass