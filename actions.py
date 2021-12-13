import pygame
from tkinter import *

def jump(width, height, screen):
    expand = False
    rev = False
    run = True
    expand2 = False
    v3 = 250 / 2 - 10
    v2 = 250
    v = 500
    y = 0
    point1 = (width // 3, height - height // 4)
    point2 = (width // 3 + 70, height - height // 4)
    point3 = (width // 3 + 70, height - height // 4 - 70)
    point4 = (width // 3, height - height // 4 - 70)
    clock = pygame.time.Clock()
    while run:
        screen.fill((0, 0, 0))
        time = clock.tick()
        y += v * time / 1000  # v * t в секундах
        shift = v2 * time / 1000
        shift2 = v3 * time / 1000
        pygame.draw.line(screen, (255, 255, 255), (0, height - height // 4), (width, height - height // 4), 1)
        pygame.draw.polygon(screen, (255, 255, 255),
                            [(point1[0], point1[1] - y), (point2[0], point2[1] - y), (point3[0], point3[1] - y),
                             (point4[0], point4[1] - y)], 1)
        if not rev:
            point1 = (point1[0] - shift2, point1[1] - shift)
            point2 = (point2[0] - shift, point2[1] + shift2)
            point3 = (point3[0] + shift2, point3[1] + shift)
            point4 = (point4[0] + shift, point4[1] - shift2)
        else:
            pass
            point1 = (point1[0] + shift, point1[1] - shift2)
            point2 = (point2[0] - shift2, point2[1] - shift)
            point3 = (point3[0] - shift, point3[1] + shift2)
            point4 = (point4[0] + shift2, point4[1] + shift)
        pygame.display.flip()
        if y > 70 and not expand:
            v3 = -v3
            expand = True
        if y < 70 and expand2:
            v3 = -v3
            expand2 = False
            expand = False
        if y > 140 and not rev and abs(v) == v:
            rev = True
        if y > 140 and abs(v) == v:
            v = -v
            v3 = - v3
            expand2 = True
        if int(y) == 0 and abs(v) != v:
            break
