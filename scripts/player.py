import pygame
from scripts.sprite import Sprite
from scripts.constants import display_size
class Player(Sprite):
    def __init__(self, center, image, speed, jump_power, gravity):
        super().__init__(center, image)

        self.original_image = image.copy()
        self.speed = speed
        self.jump_power = jump_power
        self.gravity = gravity 
        self.is_walking_left = False
        self.is_walking_right = False
        self.velosity_y = 0
        self.on_platform = False



    def update(self):
        self.velosity_y = min(self.velosity_y + self.gravity, 15)
        self.rect.y += self.velosity_y

        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.rect.x -= self.speed
                self.image = pygame.transform.flip(self.original_image, True, False)
            else:
                self.rect.x += self.speed
                self.image = self.original_image.copy()
            
        if self.on_platform:
            self.velosity_y = - self.jump_power
            self.on_platform = False


        if self.rect.right < 0:
            self.rect.left = display_size[0]
        if self.rect.left > display_size[0]:
            self.rect.right = 0

                