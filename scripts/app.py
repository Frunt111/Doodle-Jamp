from time import *
import os
import pygame

class App():
    def __init__(self):
        self.game = True
        self.maxFPS = 60

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((480, 720))

        pigame.display.set_caption('Doodle Jamp')
        image = pygame.image.load(os.path.join('assets', 'icons', 'icon.ico'))
        pygame.display.set_icon(image)

    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False


    def render(self):
        self.window.fill((0,0,0))

        pygame.display.upate()
        

    #def update(self):
        


    def Run(self):
        while self.game:
            self.handle_events()
            self.update()
            self.render()