import pygame
from settings import *
from support import *
from timer import Timer
from entity import Entity

class Player(Entity):
    def __init__(self, pos, group, create_attack, destroy_attack):
        super().__init__(group)

        self.import_assets()
        self.status = 'right'

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 300
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        # player img
        # self.height = 120
        # self.width = 120

        # weapon
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.create_attack = create_attack
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        # stats

        self.stats = {'health': 100, 'energy': 400, 'attack': 10, 'speed': 300, }
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']
        self.attack = self.stats['attack']
        self.attack_damage = 10

        # timer

        self.timers = {
           'sword use': Timer(600, self.attack_time)
        }

        # tools
        # self.selected_tool = 'sword'

    # def use_tool(self):
        # print(self.selected_tool)

    def import_assets(self):
        self.animations = {'left': [], 'right': [], 'right_idle': [], 'left_idle': [],
                           'right_attack': [], 'left_attack': []}

        for animation in self.animations.keys():
            full_path = '../Mori The Cat/animations/graphics/character/' + animation;
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        if self.status == 'right_attack' or self.status == 'left_attack':
            self.frame_index += 10 * dt
        else:
            self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        # if not self.timers['sword use'].active:
            # movement
        if keys[pygame.K_w] > 0:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # if self.pos.x < 0:
        #     self.pos.x = 0
        # if self.pos.x > SCREEN_WIDTH - self.width:
        #     self.pos.x = SCREEN_WIDTH - self.width

        # if self.pos.y < 0:
        #     self.pos.y = 0
        # if self.pos.y > SCREEN_HEIGHT - self.height:
        #     self.pos.y = SCREEN_HEIGHT - self.height

        # sword use
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks() # only calls ones
            self.create_attack()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0
            # FPS = 80

        # 2:57:00 change a weapon

    def get_status(self):
        # idle
        if self.direction.magnitude() == 0:
            # idle is the status
            if not 'idle' in self.status:
                self.status = self.status.split('_')[0] + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                self.status = self.status.split('_')[0] + '_attack'

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.cooldowns()
        self.move(dt)
        self.animate(dt)
