import pygame
from actions import load_image


class Obj(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        image = None
        rect = pygame.rect
        self.move = 0
        self.v = 770

    def update(self, time):
        self.move = self.v * time
        self.rect.x -= self.move


def create_obj(name, field, x, y):
    obj_img = None
    if name == 'b':
        obj_img = pygame.transform.scale(load_image("block.png"), (70, 70))
    elif name == 't':
        obj_img = pygame.transform.scale(load_image("thorn.png"), (70, 70))

    obj = Obj(field)
    obj.image = obj_img
    obj.rect = obj.image.get_rect()
    obj.rect.x = x
    obj.rect.y = y

    return obj
