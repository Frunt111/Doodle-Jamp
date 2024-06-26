import pygame
import os
from scripts.sprite import Sprite
from scripts.functions import *
from scripts.player import Player
from scripts.constants import display_size


class Game():
      def __init__(self):
            
            self.background = load_image('assets', 'images', 'background.png')
            self.platforms = [
                  Sprite((240, 700), load_image('assets', 'images', 'platform.png')),
                  Sprite((100, 450),load_image('assets', 'images', 'platform.png')),
                  Sprite((380, 250),load_image('assets', 'images', 'platform.png')),
            ]
            self.player = Player((240, 600), load_image('assets', 'images', 'player.png'), 5, 20, 0.75)
      
            self.offset_y = 0



      def render_object(self, window):
            window.blit(self.background, (0, 0))
            for platform in self.platforms:
                  platform.render(window, self.offset_y)
            self.player.render(window, self.offset_y)
                  
            
      


      def handle_key_down_event(self, key):
            if key == pygame.K_a:
                  self.player.is_walking_left = True
            if key == pygame.K_d:
                  self.player.is_walking_right = True
      def handle_key_up_event(self, key):
            if key == pygame.K_a:
                  self.player.is_walking_left = False
            if key == pygame.K_d:
                  self.player.is_walking_right = False


      def update_objects(self):
            self.player.update()

            for platform in self.platforms:
                  if self.player.collide(platform.rect):
                        self.player.on_platform = True

            if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
                  self.offset_y = self.player.rect.bottom - display_size[1] / 3



