import pygame

from .image_loader import ImageLoader

class Map:
    def __init__(self):
        self.background_img = ImageLoader.load_image('data/background.png', scale=1)

    def update(self):
        pass

    def render(self, surf: pygame.Surface, camera: list[int]):
        surf.blit(self.background_img, (-camera[0], -camera[1]))
