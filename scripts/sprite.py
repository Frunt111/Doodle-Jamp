import pygame
from scripts.functions import *
class Sprite():
    def __init__(self, coords, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = coords
    
    def render(self, surface):
        surface.blit(self.image, self.rect)

    def collide(self, other_rect):
        return self.rect.colliderect(other_rect)


