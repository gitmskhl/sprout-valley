from json import load

import pygame
import os

def get_path(path: str) -> str:
    return path


def load_image(path: str, scale: float) -> pygame.Surface :
    path = get_path(path)
    img = pygame.image.load(path).convert_alpha()
    if scale != 1:
        w, h = img.get_size()
        img = pygame.transform.scale(img, (w * scale, h * scale))
    return img


def load_bounding_image(path: str, scale: float) -> pygame.Surface:
    image = load_image(path, scale)
    rect = image.get_bounding_rect()
    bounding_image = image.subsurface(rect)
    return bounding_image


def load_images(path_dir: str, scale: float) -> list[pygame.Surface]:
    path_dir = get_path(path_dir)
    images = []
    for filename in sorted(os.listdir(path_dir)):
        path = os.path.join(path_dir, filename)
        images.append(load_image(path, scale))
    return images


def load_images_from_spritesheet(
        path: str,
        scale: int | float,
        ncols: int,
        nrows: int=1,
        colorkey: tuple[int, int, int]|None=None
    ) -> list[pygame.Surface]:
    path = get_path(path)
    sheet = load_image(path, scale)
    sheet_width, sheet_height = sheet.get_size()
    frame_width = sheet_width // ncols
    frame_height = sheet_height // nrows
    images = []
    for row in range(nrows):
        for col in range(ncols):
            frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame.blit(sheet, (0, 0), (col * frame_width, row * frame_height, frame_width, frame_height))
            if colorkey is not None:
                frame.set_colorkey(colorkey)
            images.append(frame)
    return images


def load_image_from_spritesheet(
        path: str,
        scale: int | float,
        cut_col: int,
        cut_row: int,
        cols: int,
        rows: int=1,
        colorkey: tuple[int, int, int]|None=None
    ) -> pygame.Surface:
    '''
    Load a single image from a spritesheet.
    col and row are 1-indexed.
    '''
    return load_images_from_spritesheet(path, scale, ncols=cols, nrows=rows, colorkey=colorkey)[cut_row * cols + cut_col]
