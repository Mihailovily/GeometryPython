from cube import Cube
from drawing import backgroundDraw, groundDraw
from load_level import load_level
from create_obj import *


class LevelField:
    def __init__(self, width, height, screen):
        self.clock = pygame.time.Clock()
        self.field = pygame.sprite.Group()
        self.width = width
        self.height = height
        self.screen = screen
        self.v_ground = 770
        self.v_bg = 55
        self.move = 0
        self.rects_ground_squares = []
        self.rects_bg = []
        self.move_bg = 0
        self.v_cube = self.v_ground

        bg = load_image("bg.png")
        ground = load_image("ground.png")

        self.bg1, self.bg2 = backgroundDraw(height, bg, self.field)

        self.ground_square1, self.ground_square2, self.ground_square3, self.ground_square4, self.ground_square5, \
        self.ground_square6, self.ground_square7 = groundDraw(height, ground, self.field)

        self.cube = Cube(width, height, screen, self.field)

        self.time = 0

        self.level = pygame.sprite.Group()

        self.create_level(0)

    def create_level(self, length):
        self.level = pygame.sprite.Group()

        counterForLevel = 0

        for i in load_level("test-level.txt"):
            for obj in i:
                if obj == '.':
                    counterForLevel += 1
                else:

                    create_obj(obj, self.level, counterForLevel * 70 + 700 + length,
                               self.height - self.height // 4 - 70)
                    counterForLevel += 1

    def show(self):
        test = True
        for i in self.level:
            if pygame.sprite.collide_mask(self.cube, i) and isinstance(i, Thorn):
                self.cube.depth = True
                break
            elif pygame.sprite.collide_mask(self.cube, i) and isinstance(i, Block):
                if i.rect.y <= self.cube.y and not i.rect.y > self.cube.y:
                    self.cube.depth = True
                    break
                else:
                    self.cube.floor = self.height - self.height // 4 - i.rect.y
                    self.cube.move_vertical = 0

            elif self.cube.x <= i.rect.x + 70 and self.cube.x >= i.rect.x:
                test = False

        if test:
            self.cube.floor = 0
        if self.cube.depth:
            self.v_bg = 0
            self.v_cube = 0
            self.v_ground = 0
        else:
            self.v_bg = 55
            self.v_cube = 770
            self.v_ground = 770

        self.time = self.clock.tick() / 1000
        if self.time >= 0.25:
            self.time = 0.012

        self.cube.time = self.time

        self.field.draw(self.screen)
        self.level.draw(self.screen)
        self.cube.update()

        # update jump cube
        if self.cube.y < self.cube.height - self.cube.height // 4 - 70 - self.cube.floor:
            self.cube.jump()
        # move ground squares
        if not self.cube.moving:
            self.level.update(self.time, self.v_ground)

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
