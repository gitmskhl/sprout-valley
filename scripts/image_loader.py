import os

from . import utils

class ImageLoader:
    _cache = {}

    @staticmethod
    def load_image(path, scale):
        path = utils.get_path(path)
        if (path, scale) not in ImageLoader._cache:
            ImageLoader._cache[(path, scale)] = utils.load_image(path, scale)
        return ImageLoader._cache[(path, scale)]
    
    @staticmethod
    def load_images(folder_path, scale):
        images = []
        folder_path = utils.get_path(folder_path)
        paths = [os.path.join(folder_path, image_name) for image_name in sorted(os.listdir(folder_path))]
        for path in paths:
            img = ImageLoader.load_image(path, scale)
            images.append(img)
        return images
