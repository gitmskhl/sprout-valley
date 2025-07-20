import pygame
import os

from .utils import get_path
from .image_loader import ImageLoader
from .exceptions import AnimationManagerAmountError

class Animation:
    def __init__(self, images: list[pygame.Surface], period: int, repeat: bool=True):
        self.images = images
        self.period = period
        self.repeat = repeat
        self.reset()
    
    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = self.period
            self.current_idx += 1
            if self.current_idx == len(self.images):
                if self.repeat:
                    self.current_idx = 0
                else:
                    self.current_idx -= 1
                    self.finished = True

    def render(self, surf, x, y, position='topleft'):
        img = self.images[self.current_idx]
        if position == 'center':
            x -= img.get_width() // 2
            y -= img.get_height() // 2
        surf.blit(img, (x, y))
    
    def reset(self):
        self.current_idx = 0
        self.timer = self.period
        self.finished = False

    def get_current_image(self) -> pygame.Surface:
        return self.images[self.current_idx]


class FolderAnimation(Animation):
    def __init__(self, folder_path: str, scale: int, period: int, repeat: bool=True):
        images = ImageLoader.load_images(folder_path, scale)
        super().__init__(images, period, repeat)


class AnimationManager:
    def __init__(
            self,
             folder_path: str,
             scales: list[int] | int,
             periods: list[int] | int,
             repeats: list[bool] | bool
    ):
        self.animations = {}
        folder_path = get_path(folder_path)
        animation_names = os.listdir(folder_path)
        # check scales
        if isinstance(scales, list) and len(scales) != len(animation_names):
            raise AnimationManagerAmountError('scale', len(animation_names), len(scales))
        elif isinstance(scales, int) or isinstance(scales, float):
            scales = [scales] * len(animation_names)
        # check periods
        if isinstance(periods, list) and len(periods) != len(animation_names):
            raise AnimationManagerAmountError('period', len(animation_names), len(periods))
        elif isinstance(periods, int):
            periods = [periods] * len(animation_names)
        # check repeats
        if isinstance(repeats, list) and len(repeats) != len(animation_names):
            raise AnimationManagerAmountError('repeat', len(animation_names), len(repeats))
        elif isinstance(repeats, int):
            repeats = [repeats] * len(animation_names)
        for animation_name, scale, period, repeat in zip(animation_names, scales, periods, repeats):
            path = os.path.join(folder_path, animation_name)
            self.animations[animation_name] = FolderAnimation(path, scale, period, repeat)

        self.current_animation_name = list(self.animations.keys())[0]
    
    def __getattr__(self, attrname):
        return getattr(self.animations[self.current_animation_name], attrname)

    def set_anim_prop(self, anim_pattern_func, prop: str, val):
        for anim in self.animations:
            if anim_pattern_func(anim):
                setattr(self.animations[anim], prop, val)

    def set_animation(self, name: str) -> None:
        if self.current_animation_name != name:
            self.current_animation_name = name
            self.animations[name].reset() 
