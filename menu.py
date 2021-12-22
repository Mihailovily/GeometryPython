from drawing import backgroundDraw, groundDraw
from actions import load_image
import pygame


class Menu:
    def __init__(self, screen, width, height):
        self.rects_ground_squares = []
        self.rects_bg = []
        self.move_bg = 0
        self.v_ground = 770
        self.v_bg = 55

        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = pygame.sprite.Group()

        btnPlay_img = load_image("btnPlay.png")
        bg = load_image("bg.png")
        ground = load_image("ground.png")
        btnCreate_img = load_image("btnCreate.png")
        btnIcon_img = load_image("btnIcon.png")

        self.bg1, self.bg2 = backgroundDraw(height, bg, self.menu)

        self.ground_square1, self.ground_square2, self.ground_square3, self.ground_square4, self.ground_square5, \
        self.ground_square6, self.ground_square7 = groundDraw(height, ground, self.menu)

        btnPlay = pygame.sprite.Sprite(self.menu)
        btnPlay.image = pygame.transform.scale(btnPlay_img, (350, 350))
        btnPlay.rect = btnPlay.image.get_rect()
        btnPlay.rect.x = (width - 350) // 2
        btnPlay.rect.y = (height - 350) // 2

        btnCreate = pygame.sprite.Sprite(self.menu)
        btnCreate.image = pygame.transform.scale(btnCreate_img, (220, 220))
        btnCreate.rect = btnCreate.image.get_rect()
        btnCreate.rect.x = btnPlay.rect.x + 350 + 100
        btnCreate.rect.y = (height - 220) // 2

        btnIcon = pygame.sprite.Sprite(self.menu)
        btnIcon.image = pygame.transform.scale(btnIcon_img, (220, 220))
        btnIcon.rect = btnIcon.image.get_rect()
        btnIcon.rect.x = btnPlay.rect.x - 100 - 220
        btnIcon.rect.y = (height - 220) // 2

    def show(self):
        self.time = self.clock.tick() / 1000

        self.menu.draw(self.screen)

        self.move = self.v_ground * self.time
        self.ground_square1.rect.x -= self.move
        self.ground_square2.rect.x -= self.move
        self.ground_square3.rect.x -= self.move
        self.ground_square4.rect.x -= self.move
        self.ground_square5.rect.x -= self.move
        self.ground_square6.rect.x -= self.move
        self.ground_square7.rect.x -= self.move
        self.rects_ground_squares.append(self.ground_square1.rect.x)
        self.rects_ground_squares.append(self.ground_square2.rect.x)
        self.rects_ground_squares.append(self.ground_square3.rect.x)
        self.rects_ground_squares.append(self.ground_square4.rect.x)
        self.rects_ground_squares.append(self.ground_square5.rect.x)
        self.rects_ground_squares.append(self.ground_square6.rect.x)
        self.rects_ground_squares.append(self.ground_square7.rect.x)

        for i in range(len(self.rects_ground_squares)):
            if self.rects_ground_squares[i] <= - 350:
                if i == 0:
                    self.ground_square1.rect.x = self.ground_square7.rect.x + 350
                elif i == 1:
                    self.ground_square2.rect.x = self.ground_square1.rect.x + 350
                elif i == 2:
                    self.ground_square3.rect.x = self.ground_square2.rect.x + 350
                elif i == 3:
                    self.ground_square4.rect.x = self.ground_square3.rect.x + 350
                elif i == 4:
                    self.ground_square5.rect.x = self.ground_square4.rect.x + 350
                elif i == 5:
                    self.ground_square6.rect.x = self.ground_square5.rect.x + 350
                elif i == 6:
                    self.ground_square7.rect.x = self.ground_square6.rect.x + 350
        self.rects_ground_squares.clear()

        # move bg squares
        self.move_bg = self.v_bg * self.time
        self.bg1.rect.x -= int(self.move_bg + 0.5)
        self.bg2.rect.x -= int(self.move_bg + 0.5)
        self.rects_bg.append(self.bg1.rect.x)
        self.rects_bg.append(self.bg2.rect.x)

        for i in range(len(self.rects_bg)):
            if self.rects_bg[i] <= - 2048:
                if i == 0:
                    self.bg1.rect.x = self.bg2.rect.x + 2048
                if i == 1:
                    self.bg2.rect.x = self.bg1.rect.x + 2048

        self.rects_bg.clear()
