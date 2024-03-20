import random

from Ardest.code.Background import Background
from Ardest.code.Const import WIN_WIDTH, WIN_HEIGHT
from Ardest.code.Enemy import Enemy
from Ardest.code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (576, 0)))
                return list_bg
            case 'player1nav':
                return Player('player1nav', (10, WIN_HEIGHT/2 - 30))
            case 'player2nav':
                return Player('player2nav', (10, WIN_HEIGHT/2 + 30))
            case 'enemy1nav':
                return Enemy('enemy1nav', (WIN_WIDTH+10, random.randint(0 + 40, WIN_HEIGHT - 40)))
            case 'enemy2nav':
                return Enemy('enemy2nav', (WIN_WIDTH+10, random.randint(0 + 40, WIN_HEIGHT - 40)))

