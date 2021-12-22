import pygame


def backgroundDraw(height, bg_img, field):
    bg1 = pygame.sprite.Sprite(field)
    bg1.image = bg_img
    bg1.rect = bg1.image.get_rect()
    bg1.rect.x = 0
    bg1.rect.y = -(2048 - height)
    bg2 = pygame.sprite.Sprite(field)
    bg2.image = bg_img
    bg2.rect = bg2.image.get_rect()
    bg2.rect.x = 2048
    bg2.rect.y = -(2048 - height)
    return bg1, bg2


def groundDraw(height, ground_img, field):
    ground_square1 = pygame.sprite.Sprite(field)
    ground_square1.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square1.rect = ground_square1.image.get_rect()
    ground_square1.rect.x = 0
    ground_square1.rect.y = height - height // 4

    ground_square2 = pygame.sprite.Sprite(field)
    ground_square2.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square2.rect = ground_square1.image.get_rect()
    ground_square2.rect.x = 350
    ground_square2.rect.y = height - height // 4

    ground_square3 = pygame.sprite.Sprite(field)
    ground_square3.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square3.rect = ground_square1.image.get_rect()
    ground_square3.rect.x = 700
    ground_square3.rect.y = height - height // 4

    ground_square4 = pygame.sprite.Sprite(field)
    ground_square4.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square4.rect = ground_square1.image.get_rect()
    ground_square4.rect.x = 1050
    ground_square4.rect.y = height - height // 4

    ground_square5 = pygame.sprite.Sprite(field)
    ground_square5.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square5.rect = ground_square1.image.get_rect()
    ground_square5.rect.x = 1400
    ground_square5.rect.y = height - height // 4

    ground_square6 = pygame.sprite.Sprite(field)
    ground_square6.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square6.rect = ground_square1.image.get_rect()
    ground_square6.rect.x = 1750
    ground_square6.rect.y = height - height // 4

    ground_square7 = pygame.sprite.Sprite(field)
    ground_square7.image = pygame.transform.scale(ground_img, (350, 350))
    ground_square7.rect = ground_square1.image.get_rect()
    ground_square7.rect.x = 2100
    ground_square7.rect.y = height - height // 4
    return ground_square1, ground_square2, ground_square3, ground_square4, ground_square5, ground_square6, \
           ground_square7
