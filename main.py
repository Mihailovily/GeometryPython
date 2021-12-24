import pygame
from tkinter import *
from level_field import LevelField
import loading_screen
from menu import Menu
import antipirate
import os

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
antipirate.no_license_alarm()
running = True

# менюшка
menu = Menu(screen, width, height)

# preloader
loading = loading_screen.Loading(width, height, screen)

# поле
field = LevelField(width, height, screen)

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
        # menu.show()
        # for event in events:
        #     if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[0] - 60) ** 2 < 50 ** 2:
        #         menu.showExit()
        field.show()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                field.cube_jump()
                field.show()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    field.cube_jump()
                    field.show()
        for event in events:
            # выход по нажатию на крестик
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[0] - 60) ** 2 < 50 ** 2:
                running = False
        # игровой процесс, пока что заморожен
    pygame.display.flip()

# if os.path.exists("screenshot.jpg"):
#     os.remove("screenshot.jpg")
# подчистка следов
if os.path.exists("screenshot.jpg"):
    os.remove("screenshot.jpg")
# выход
pygame.quit()
