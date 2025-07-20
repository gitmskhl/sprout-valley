import pygame
import os

def get_path(path: str) -> str:
    return path


def load_image(path: str, scale: float) -> pygame.Surface :
    path = get_path(path)
    img = pygame.image.load(path)
    if scale != 1:
        w, h = img.get_size()
        img = pygame.transform.scale(img, (w * scale, h * scale))
    return img


def load_images(path_dir: str, scale: float) -> list[pygame.Surface]:
    path_dir = get_path(path_dir)
    images = []
    for filename in sorted(os.listdir(path_dir)):
        path = os.path.join(path_dir, filename)
        images.append(load_image(path, scale))
    return images


