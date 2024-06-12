from time import *
import os
import pygame
from scripts.game import Game
from scripts.functions import *
class App():
    def __init__(self):
        self.game = True
        self.maxFPS = 60

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((480, 720))

        self.game = Game()

        pygame.display.set_caption('Doodle Jamp')
        pygame.display.set_icon(load_image('assets', 'icons', 'icon.ico'))

        fon = Game()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False


    def render(self):
        self.window.fill((0,0,0))
        self.game.render_object(self.window)
        pygame.display.update()
        

    #def update(self):
        


    def run(self):
        while self.game:
            self.handle_events()
           # self.update()
            self.render()
