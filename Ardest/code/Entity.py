import pygame
from abc import ABC, abstractmethod
from pygame import Surface


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf: Surface = pygame.image.load('./assets/level_img/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[0])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass

