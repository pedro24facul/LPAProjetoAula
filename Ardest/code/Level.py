import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Ardest.code.Const import COLOR_WHITE, MENU_OPTION_LIST, EVENT_ENEMY
from Ardest.code.Entity import Entity
from Ardest.code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_op):
        self.window: Surface = window
        self.name = name
        self.menu_op = menu_op
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('player1nav'))
        if menu_op in [MENU_OPTION_LIST[1]]:
            self.entity_list.append(EntityFactory.get_entity('player2nav'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)


    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenho das entidades
                self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1nav', 'enemy2nav'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
