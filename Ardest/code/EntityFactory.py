#!/usr/bin/python
#-*- coding: utf-8 -*-
from Ardest.code.Background import Background
from Ardest.code.Const import WIN_WIDTH


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

