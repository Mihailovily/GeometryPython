import pygame
from cube import Cube
from actions import load_image, rotation
from drawing import backgroundDraw, groundDraw
from load_level import load_level
from create_obj import create_obj


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

        counterForLevel = 0

        self.level = pygame.sprite.Group()

        print(load_level("test-level.txt"))

        print(height - height // 4 - 70)

        for i in load_level("test-level.txt"):
            for obj in i:
                if obj == '.':
                    counterForLevel += 1
                else:

                    create_obj(obj, self.level, counterForLevel * 70, height - height // 4 - 70)
                    counterForLevel += 1

    def show(self):
        self.time = self.clock.tick() / 1000
        if self.time >= 0.25:
            self.time = 0.012

        self.field.draw(self.screen)
        self.level.draw(self.screen)

        if self.cube.rect[0] < self.width // 3:
            move = self.v_cube * self.time
            self.cube.rect = (self.cube.rect[0] + move, self.cube.rect[1])
            self.cube.x += move
        else:
            self.cube.rect = (self.width // 3, self.cube.rect[1])
            self.cube.moving = False

        # update jump cube
        if self.cube.get_cords()[1] < self.cube.height - self.cube.height // 4 - 70:
            self.cube.jump()
        elif self.cube.rect[1] >= self.cube.height - self.cube.height // 4 - 70 and abs(
                self.cube.v) != self.cube.v:
            self.cube.v = -self.cube.v
            self.cube.counter += 1
            self.cube.rect = (
                self.cube.rect[0], self.cube.height - self.cube.height // 4 - 70)
            self.cube.y = 0
            self.cube.shift = 0
            self.cube.for_rotate = 0
        else:
            if self.cube.counter % 2 == 0:
                self.cube.image = pygame.transform.scale(load_image('cube.png'), (70, 70))
            else:
                self.cube.image = pygame.transform.scale(rotation(load_image('cube.png'), 180),
                                                         (70, 70))
        # if self.cube.rect[0] < 350 and self.cube.rect[0] > 300:
        #     self.cube_jump()
        # move ground squares
        if not self.cube.moving:
            self.level.update(self.time)

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

    def cube_jump(self):
        self.cube.jump()
