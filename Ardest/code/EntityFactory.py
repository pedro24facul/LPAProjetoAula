#!/usr/bin/python
#-*- coding: utf-8 -*-
from Ardest.code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1Bg0':
                return Background(f'level1Bg0', position)

