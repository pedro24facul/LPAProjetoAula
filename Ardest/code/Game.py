import sys

import pygame as pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

from Ardest.code.Const import MENU_OPTION_LIST
from Ardest.code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            op_menu = menu.run()
            if op_menu in [MENU_OPTION_LIST[0], MENU_OPTION_LIST[1], MENU_OPTION_LIST[2]]:
                level = Level(self.window, 'Level 1', op_menu)
                level.run()
            else:
                pygame.quit()
                sys.exit()
