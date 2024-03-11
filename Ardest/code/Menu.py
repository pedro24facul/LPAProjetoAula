#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH

from Ardest.code.Const import COLOR_ORANGE, MENU_OPTION_LIST, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./assets/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # pygame.mixer_music.load('./assets/Menu.wav')
        # pygame.mixer_music.play(-1)

        #Variável para armazenar o valor da opção selecionada no menu principal
        menu_option = 0
        while True:
            #Desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Ardest", COLOR_ORANGE, (WIN_WIDTH/2, 70))
            self.menu_text(50, "Dash", COLOR_ORANGE, (WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION_LIST)): #Gerando as opções do menu
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION_LIST[i], COLOR_YELLOW, (WIN_WIDTH / 2, 180 + 30 * i))
                else:
                    self.menu_text(30, MENU_OPTION_LIST[i], COLOR_WHITE, (WIN_WIDTH / 2, 180 + 30 * i))
            pygame.display.flip()

            #Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION_LIST) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = 3
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION_LIST[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
