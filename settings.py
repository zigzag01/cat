from pygame.math import Vector2

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
FPS = 60

# ui

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT_SIZE = 18
UI_FONT = '../Mori The Cat/animations/graphics/font/joystix.ttf'

# general colors

UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'gold'
UI_BORDER_COLOR_ACTIVE = 'olive'

# weapon
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../Mori The Cat/animations/graphics/character/weapon/'}
}

# enemy
monster_data = {
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw',
                'attack_sound': '../Mori The Cat/animations/audio/sounds/Monster_Attack.wav', 'speed': 300,
                'resistance': 3, 'attack_radius': 120, 'notice_radius': 400}
}
