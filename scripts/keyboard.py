import pygame


def init_key_bindings():
    global KEY_BINDINGS
    KEY_BINDINGS = {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'up': pygame.K_UP,
        'down': pygame.K_DOWN
    }
