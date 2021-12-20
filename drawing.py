import pygame
from cube import Cube
from actions import load_image, rotation


def backgroundDraw(height, bg, field):
    bg1 = pygame.sprite.Sprite(field)
    bg1.image = bg
    bg1.rect = bg1.image.get_rect()
    bg1.rect.x = 0
    bg1.rect.y = -(2048 - height)
    bg2 = pygame.sprite.Sprite(field)
    bg2.image = bg
    bg2.rect = bg2.image.get_rect()
    bg2.rect.x = 2048
    bg2.rect.y = -(2048 - height)
    return bg1, bg2
