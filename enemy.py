import pygame
import random
from settings import *
from entity import Entity
from player import Player
from support import *


class Enemy(Entity):
    def __init__(self, pos, groups, player, game):
        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.import_assets()
        self.status = 'idle'
        self.player = player
        self.game = game

        # graphics setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.speed = 280

        # stats
        self.stats = {'health': 30, 'damage': 20, 'speed': 250, }
        self.health = self.stats['health']
        self.exp = 15
        self.energy = self.stats['speed']

    def import_graphics(self, name):
        self.animations = {'idle': [], 'run': [], 'attack': []}
        main_path = f'../Mori The Cat/animations/graphics/enemy/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder((main_path + animation))

    def import_assets(self):
        self.animations = {'run': [], 'attack': [], 'idle': []}

        for animation in self.animations.keys():
            full_path = '../Mori The Cat/animations/graphics/enemies/' + animation;
            self.animations[animation] = import_folder(full_path)

    def update(self, game, player=None, attack_damage=0):
        if player is None:
            player = self.player
        if self.rect.x < self.player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > self.player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < self.player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > self.player.rect.y:
            self.rect.y -= self.speed

        if self.game.check_collision(self, self.game.player):
            if self.player.attack:
                self.health -= 15
                if self.health <= 0:
                    self.kill()
            else:
                self.player.health -= 10
