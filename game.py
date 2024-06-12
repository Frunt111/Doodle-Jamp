import pygame
import os
class Game():

      def __init__(self):
            path = os.path.join('assets', 'images', 'background.png')
            self.background = pygame.image.load(path)


      def render_object(self, window):
            window.blit(self.background, (0, 0))
