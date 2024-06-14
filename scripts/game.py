import pygame
import os
from scripts.sprite import Sprite
from scripts.functions import *

class Game():

      def __init__(self):
            path = os.path.join('assets', 'images', 'background.png')
            self.background = pygame.image.load(path)
            self.platforms = [
                  Sprite(load_image('assets', 'images', 'platform.png'),(240, 700)),
                  Sprite(load_image('assets', 'images', 'platform.png'),(100, 450)),
                  Sprite(load_image('assets', 'images', 'platform.png'),(380, 250)),
            ]


      def render_object(self, window):
            window.blit(self.background, (0, 0))
            for platform in self.platforms:
                  platform.render(window)
