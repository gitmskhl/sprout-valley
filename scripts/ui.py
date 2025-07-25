import pygame

from .utils import load_image
from . import settings
from main import App

class UI:
    def __init__(self, app: App):
        self.app = app
        self.main_player = app.main_player
        # cache
        self._init_display_sizes()
        # tools
        self._init_tools()
        # seeds
        self._init_seeds()


    def _init_display_sizes(self):
        self.last_screen_size = self.app.display.get_size()
        self.tool_position = (
            self.app.display.get_width() * settings.TOOL_POSITION[0] + 20,
            self.app.display.get_height() * settings.TOOL_POSITION[1] - 30
        )
    

    def _init_tools(self):
        scale = settings.TOOL_SCALE
        self.tools = {
            'water':    load_image('data/tools/icons/water.png', scale=scale),
            'axe':      load_image('data/tools/icons/axe.png', scale=scale),
            'hoe':      load_image('data/tools/icons/hoe.png', scale=scale),
        }


    def _init_seeds(self):
        pass


    def display(self):
        tool_img = self.tools[self.main_player.current_tool]
        if self.app.display.get_size() != self.last_screen_size:
            self._init_display_sizes()
        tool_pos = (self.tool_position[0] - tool_img.get_width() // 2, self.tool_position[1] - tool_img.get_height() // 2)
        self.app.display.blit(tool_img, tool_pos)


