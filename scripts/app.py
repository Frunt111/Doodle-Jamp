from time import *
import os
import pygame
from scripts.game import Game
from scripts.functions import *
from scripts.constants import display_size


class App():
    def __init__(self):
        self.game = True
        self.maxFPS = 60

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((480, 720))

        self.game = Game()

        pygame.display.set_caption('Doodle Jamp')
        pygame.display.set_icon(load_image('assets', 'icons', 'icon.ico'))


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False
            if event.type == pygame.KEYDOWN:
                self.game.handle_key_down_event(event.key)
            if event.type == pygame.KEYUP:
                self.game.handle_key_up_event(event.key)


    def render(self):
        self.window.fill((0,0,0))
        self.game.render_object(self.window)
        pygame.display.update()

        

    def update(self):
        self.game.update_objects()
        


    def run(self):
        while self.game:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.maxFPS)
