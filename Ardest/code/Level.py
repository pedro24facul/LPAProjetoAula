import pygame
from pygame import Surface

from Ardest.code.Entity import Entity
from Ardest.code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_op):
        self.window: Surface = window
        self.name = name
        self.menu_op = menu_op
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
