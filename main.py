import pygame
import sys
import time
from settings import *
from level import Level
from player import Player
from entity import Entity
from enemy import Enemy
from button import Button

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Mori The Cat')
        self.clock = pygame.time.Clock()
        self.level = Level()

        # enemies spawn
        self.allEnemies = pygame.sprite.Group()
        self.last_spawn_time = time.time()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # data time
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()