import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.5
        self.direction = pygame.math.Vector2()

    def move(self, dt):
        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y