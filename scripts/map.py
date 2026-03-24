import pygame

from .image_loader import ImageLoader
from .animation import FolderAnimation

class Map:
    def __init__(self):
        self.water_animation = FolderAnimation(
            folder_path='data/background/water',
            scale=1,
            period=10,
            repeat=True,
        )
        self.background_img = ImageLoader.load_image('data/background.png', scale=1)
        self.delta_x = (self.water_animation.get_current_image().get_width() - self.background_img.get_width()) // 2
        self.delta_y = (self.water_animation.get_current_image().get_height() - self.background_img.get_height()) // 2

    def update(self):
        self.water_animation.update()

    def render(self, surf: pygame.Surface, camera: list[int]):
        self.water_animation.render(surf, -self.delta_x - camera[0], -self.delta_y - camera[1])
        surf.blit(self.background_img, (-camera[0], -camera[1]))
