from player import Player
from support import *
from settings import *
from random import choice
from weapon import Weapon
from UI import UI
from enemy import Enemy
import random


class Level:
    def __init__(self):
        # screen
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # user interface
        self.ui = UI()

        # enemy spawn timer
        self.enemy_spawn_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_spawn_timer, random.randint(3000, 7000))  # set timer for 3 to 7 seconds

        self.setup()

    def setup(self):
        self.player = Player((360, 360), [self.all_sprites], self.create_attack, self.destroy_attack)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.all_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def generate_enemy_position(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return (random.randint(0, SCREEN_WIDTH), -100)
        elif side == 'bottom':
            return (random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 100)
        elif side == 'left':
            return (-100, random.randint(0, SCREEN_HEIGHT))
        elif side == 'right':
            return (SCREEN_WIDTH + 100, random.randint(0, SCREEN_HEIGHT))

    def create_enemy(self):
        enemy_pos = self.generate_enemy_position()
        enemy = Enemy(enemy_pos, [self.all_sprites], self.player, self)
        self.all_sprites.add(enemy)

    def run(self, dt):
        self.display_surface.fill('olive')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        for sprite in self.all_sprites:
            if isinstance(sprite, Enemy):
                sprite.update(self, self.player, self.player.attack_damage if self.player.attack else 0)
        self.ui.display(self.player)
        for event in pygame.event.get():
            if event.type == self.enemy_spawn_timer:
                self.create_enemy()
