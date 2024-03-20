import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

MENU_OPTION_LIST = ('PLAY GAME 1P',
                    'PLAY GAME 2P - COOPERATIVE',
                    'PLAY GAME 2P - COMPETITIVE',
                    'EXIT GAME')

ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'player1nav': 4,
    'player2nav': 4,
    'enemy1nav': 3,
    'enemy2nav': 2,
}

EVENT_ENEMY = pygame.USEREVENT + 1

PLAYER_KEY_UP = {
    'player1nav': pygame.K_UP,
    'player2nav': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'player1nav': pygame.K_DOWN,
    'player2nav': pygame.K_s
}

PLAYER_KEY_LEFT = {
    'player1nav': pygame.K_LEFT,
    'player2nav': pygame.K_a
}

PLAYER_KEY_RIGHT = {
    'player1nav': pygame.K_RIGHT,
    'player2nav': pygame.K_d
}
