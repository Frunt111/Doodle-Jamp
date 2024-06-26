import pygame
from scripts.functions import *
class Sprite():
    def __init__(self, coords, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = coords
    
    def render(self, window, offset_y):
        rect = self.rect.move(0, - offset_y)
        window.blit(self.image, rect)


    def collide(self, other_rect):
        rect = pygame.Rect(self.rect.bottomleft, (self.rect.width, 20))
        return self.velosity_y > 0 and other_rect.colliderect(rect)
 
