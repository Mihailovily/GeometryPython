import pygame
from tkinter import *
from level_field import LevelField
import loading_screen
from menu import Menu
import cube
# import antipirate
import os

# antipirate.generate_license()
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

pygame.init()
size = width, height
screen = pygame.display.set_mode(size)
# running = antipirate.check_license()
running = True

menu = Menu(screen, width, height)

loading = loading_screen.Loading(width, height, screen)

field = LevelField(width, height, screen)

clock = pygame.time.Clock()
while running:
    events = pygame.event.get()
    screen.fill((0, 0, 0))
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if bool(events):
        events = [events[0]]
    if loading.loading:
        loading.show()
    else:
        menu.show()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - 60) ** 2 + (event.pos[0] - 60) ** 2 < 50 ** 2:
                menu.showExit()
        # field.show()
        # for event in events:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         field.cube_jump()
        #         field.show()
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             field.cube_jump()
        #             field.show()
    # pygame.draw.rect(screen, (0, 0, 0), (400, height - height // 4 - 70, 70, 70))
    # pygame.draw.rect(screen, (0, 0, 0), (470, height - height // 4 - 70, 70, 70))
    # pygame.draw.rect(screen, (0, 0, 0), (540, height - height // 4 - 70, 70, 70))
    pygame.display.flip()
# if os.path.exists("screenshot.jpg"):
#     os.remove("screenshot.jpg")
pygame.quit()
