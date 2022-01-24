import pygame
from tkinter import *
from level_field import LevelField
import loading_screen
from menu import Menu
from menu import Levels
from menu import Settings
from menu import playing_music
import antipirate
import os
import time

# потом убрать надо
# antipirate.generate_license()
# определение размеров экрана
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
# инициализация, антипиратство
pygame.init()
size = width, height
screen = pygame.display.set_mode(size)
try:
    if not antipirate.check_license():
        antipirate.no_license_alarm()
except Exception as E:
    print('Кажется, нет интернета')
running = True

# менюшка
menu = Menu(screen, width, height)
# выбор уровня
levels = Levels(screen, width, height)
# настройки
settings = Settings(screen, width, height)

# preloader
loading = loading_screen.Loading(width, height, screen)

# поле
field = LevelField(width, height, screen, 'levels/1.csv')
game = False
level = False
MENU = False
SETTINGS = False
levelnum = 1
# время
clock = pygame.time.Clock()
while running:
    events = pygame.event.get()
    screen.fill((0, 0, 0))
    for event in events:
        # выход по закрытию программы
        if event.type == pygame.QUIT:
            running = False
    if bool(events):
        # у Влада спросить надо
        events = [events[0]]
    if loading.loading:
        loading.show()
    else:
        if game is False and level is False:
            menu.show()
            MENU = True
        if level is True:
            levels.show()
        if SETTINGS is True:
            settings.show()
        if game is True:
            if MENU is False:
                field.show()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        field.cube.jump()
                        field.show()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        field.cube.jump()
                        field.show()

                if field.cube.depth:
                    if levelnum == 1:
                        field.create_level(700, 'levels/1.csv')
                    else:
                        field.create_level(700, 'levels/2.csv')

                    field.cube.depth = False
                    field.cube.counter = 0
                    field.cube.y = height - height // 4 - 70
                    field.cube.image = field.cube.cube
                    field.cube.shift = 0
                    field.cube.for_rotate = 0
                    field.cube.move_vertical = 0
                    field.cube.v = 770
                    field.cube.floor = 0

                    time.sleep(1)
        # for event in events:
        #    if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[1] - 60) ** 2 < 50 ** 2:
        #        menu.showExit()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[1] - 60) ** 2 < 50 ** 2 \
                    and level is False and game is False and SETTINGS is False:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - ((width - 350) // 2 + 175)) ** 2 + (
                    event.pos[1] - ((height - 350) // 2 + 175)) ** 2 < 175 ** 2 \
                    and game is False and level is False and SETTINGS is False:
                level = True
                MENU = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - ((width - 350) // 2 + 175) - 370) ** 2 + (
                    event.pos[1] - ((height - 350) // 2 + 175)) ** 2 < 120 ** 2 \
                    and game is False and level is False and MENU is True:
                SETTINGS = True
                MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[1] - 60) ** 2 < 50 ** 2 \
                    and level is True and game is False:
                level = False
                MENU = True
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[1] - 60) ** 2 < 50 ** 2 \
                    and SETTINGS is True and game is False:
                SETTINGS = False
                MENU = True
            if event.type == pygame.MOUSEBUTTONDOWN and 200 < event.pos[1] < 470 and (width - 350) // 2 - 280 < \
                    event.pos[0] < (width - 350) // 2 + 642 \
                    and level is False and game is False and SETTINGS is True:
                playing_music = False
            if event.type == pygame.MOUSEBUTTONDOWN and 200 < event.pos[1] < 470 and (width - 350) // 2 - 280 < \
                    event.pos[0] < (width - 350) // 2 + 642 \
                    and level is True and game is False and SETTINGS is False:
                level = False
                game = True
                levelnum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and 482 < event.pos[1] < 756 and (width - 350) // 2 - 280 < \
                    event.pos[0] < (width - 350) // 2 + 642 \
                    and level is True and game is False and SETTINGS is False:
                level = False
                game = True
                levelnum = 2

    pygame.display.flip()

# подчистка следов
if os.path.exists("screenshot.jpg"):
    os.remove("screenshot.jpg")
# выход
pygame.quit()
