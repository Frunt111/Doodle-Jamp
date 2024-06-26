from scripts.sprite import Sprite
from random import randint
import pygame
from scripts.functions import *

class PlatformGenerator:

    def __init__(self, step):
        self.step = step

    def create_start_configuration(self, center_y):
        image = load_image('assets', 'images', 'platform.png')
        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)
        platform = Sprite(image, [center_x, center_y])

    def create_platform(self):
        ...

    def update(self):
        ...