import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert().convert_alpha()
    return image


def rot(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)

    return rotated_image


