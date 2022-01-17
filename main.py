import pygame
from tkinter import *
from level_field import LevelField
import loading_screen
from menu import Menu
from menu import Levels
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
# antipirate.no_license_alarm()
running = True

# менюшка
menu = Menu(screen, width, height)
# выбор уровня
levels = Levels(screen, width, height)

# preloader
loading = loading_screen.Loading(width, height, screen)

# поле
field = LevelField(width, height, screen)
game = False
level = False
MENU = False
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
        if level is True and game is False:
            levels.show()
        if game is True and level is False:
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
                    field.create_level(700)

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
                    and level is False and game is False:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - ((width - 350) // 2 + 175)) ** 2 + (
                    event.pos[1] - ((height - 350) // 2 + 175)) ** 2 < 175 ** 2 \
                    and game is False:
                level = True
                MENU = False
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[1] - 60) ** 2 < 50 ** 2 \
                    and level is True and game is False:
                level = False
            elif event.type == pygame.MOUSEBUTTONDOWN and 200 < event.pos[1] < 470 and (width - 350) // 2 - 280 < \
                    event.pos[0] < (width - 350) // 2 + 642 \
                    and level is True and game is False:
                level = False
                game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and 482 < event.pos[1] < 756 and (width - 350) // 2 - 280 < \
                    event.pos[0] < (width - 350) // 2 + 642 \
                    and level is True and game is False:
                level = False
                game = True

    pygame.display.flip()

# if os.path.exists("screenshot.jpg"):
#     os.remove("screenshot.jpg")
# подчистка следов
if os.path.exists("screenshot.jpg"):
    os.remove("screenshot.jpg")
# выход
pygame.quit()
