import pygame
from actions import load_image


class Thorn(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.move = 0

        self.mask = pygame.mask.Mask((30, 40))
        self.mask.set_at((28, 21))

    def update(self, time, v):
        self.move = v * time
        self.rect.x -= self.move


class Block(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.move = 0

        self.mask = pygame.mask.Mask((60, 60))
        self.mask.set_at((5, 5))

    def update(self, time, v):
        self.move = v * time
        self.rect.x -= self.move


def create_obj(name, field, x, y):
    if name == 'b':
        obj_img = pygame.transform.scale(load_image("block.png"), (70, 70))
        obj = Block(field)
    elif name == 't':
        obj_img = pygame.transform.scale(load_image("thorn.png"), (70, 70))
        obj = Thorn(field)
    obj.image = obj_img
    obj.rect = obj.image.get_rect()
    obj.rect.x = x
    obj.rect.y = y

    return obj
