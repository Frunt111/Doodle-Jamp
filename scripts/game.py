import pygame
import os
from scripts.sprite import Sprite
from scripts.functions import *
from scripts.player import Player


class Game():
      def __init__(self):
            
            self.background = load_image(('assets', 'images', 'background.png'))
            self.platforms = [
                  Sprite(load_image('assets', 'images', 'platform.png'),(240, 700)),
                  Sprite(load_image('assets', 'images', 'platform.png'),(100, 450)),
                  Sprite(load_image('assets', 'images', 'platform.png'),(380, 250)),
            ]
            self.player = Player((240, 600), load_image('assets', 'images', 'player.png'), 5, 15, 0,75)



      def render_object(self, window):
            window.blit(self.background, (0, 0))
            for platform in self.platforms:
                  platform.render(window)
            self.player.render(window)
                  
            
      


      def prcess_key_down_event(self, key):
            if key == pygame.K_a:
                  self.is_walking_left = True
            if key == pygame.K_d:
                  self.is_walking_right = True
      def prcess_key_down_event(self, key):
            if key == pygame.K_a:
                  self.player.is_walking_left = False
            if key == pygame.K_d:
                  self.player.is_walking_right = False


      def update_objects(self):
            self.player.update()
