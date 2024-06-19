class Player(Sprite):
    def __init__(self, center, image, speed, jump_power, gravity):
        super().__init__(center, image)

        self.speed = speed
        self.jump_power = jump_power
        self.gravity = gravity 
        self.is_walking_left = False
        self.is_walking_right = False
        self.velosity_y = 0
    def update(self):
        self.velosity_y = min(self.velosity_y + self.gravity, 15)
        self.rect.y += self.velosity_y

        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
                