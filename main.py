import pygame
from tkinter import *
import actions
import loading_screen
import cube

root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
running = True
loading = loading_screen.Loading()
cube = cube.Cube(width, height, screen)
while running:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    if bool(events):
        events = [events[0]]
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cube.jump()
            cube.show()
    # loading.show(screen)
    cube.show()
    pygame.display.flip()

pygame.quit()
