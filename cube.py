import pygame
import actions


class Cube(pygame.sprite.Sprite):
    def __init__(self, width, height, screen, *group):
        super().__init__(*group)
        self.v2 = 380
        self.v = 770
        self.move_vertical = 0
        self.shift = 0
        self.for_rotate = 1
        self.floor = 0
        self.x = -70
        self.y = height - height // 4 - 70 - self.floor
        self.rect = (self.x, self.y)
        self.time = 1
        self.width = width
        self.height = height
        self.screen = screen
        self.counter = 0
        self.clock = pygame.time.Clock()
        self.img = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.cube = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.moving = True

        self.floorOld = self.floor
        self.jumping = False

        self.depth = False

        self.mask = pygame.mask.from_surface(pygame.Surface([70, 70]))

    def jump(self):
        self.move_vertical += self.v * self.time
        if self.move_vertical < 0:
            self.move_vertical = 0
        self.shift += self.v2 * self.time

        if self.move_vertical >= 175 and abs(self.v) == self.v:
            self.v = -self.v

        if int(self.shift) >= self.for_rotate:
            self.for_rotate = int(self.shift)

            self.image = actions.rotation(self.cube, -self.for_rotate)

        if self.moving:
            self.x -= (self.image.get_rect()[2] - 70) // 2
            self.x += self.time * 770
        else:
            self.x = self.width // 3 - (self.image.get_rect()[2] - 70) // 2
        self.y = self.height - self.height // 4 - 70 - self.move_vertical - self.floorOld
        self.y -= (self.image.get_rect()[2] - 70) // 2
        self.rect = (self.x, self.y)

    def update(self):
        if self.move_vertical == 0 and abs(
                self.v) != self.v:
            self.v = -self.v
            self.counter += 1
            self.y = self.height - self.height // 4 - 70 - self.floor
            self.move_vertical = 0

            print(self.shift)

            if self.for_rotate > 360:
                self.for_rotate -= 360
                self.shift -= 360

            if self.for_rotate > 270:
                if 360 - self.for_rotate < self.for_rotate - 270:
                    self.cube = self.img
                    self.for_rotate = self.shift = 0
                else:
                    self.cube = actions.rotation(self.img, 270)
                    self.for_rotate = self.shift = 270

            elif self.for_rotate > 180:
                if 270 - self.for_rotate < self.for_rotate - 180:
                    self.cube = actions.rotation(self.img, 270)
                    self.for_rotate = self.shift = 270
                else:
                    self.cube = actions.rotation(self.img, 180)
                    self.for_rotate = self.shift = 180

            elif self.for_rotate > 90:
                if 180 - self.for_rotate < self.for_rotate - 90:
                    self.cube = actions.rotation(self.img, 180)
                    self.for_rotate = self.shift = 180
                else:
                    self.cube = actions.rotation(self.img, 90)
                    self.for_rotate = self.shift = 90

            elif self.for_rotate > 0:
                if 90 - self.for_rotate < self.for_rotate - 0:
                    self.cube = actions.rotation(self.img, 90)
                    self.for_rotate = self.shift = 90
                else:
                    self.cube = self.img
                    self.for_rotate = self.shift = 0
            self.image = self.cube

        if self.x < self.width // 3:
            move = 770 * self.time
            self.x += move
        else:
            self.moving = False
        self.rect = (self.x, self.y)

    def down(self):
        self.move_vertical = self.v * self.time
        if self.move_vertical < 0:
            self.move_vertical = 0
        self.shift += self.v2 * self.time

        if int(self.shift) >= self.for_rotate:
            self.for_rotate = int(self.shift)

            self.image = actions.rotation(self.image, -self.for_rotate)

        self.y += self.move_vertical

        self.x = self.width // 3 - (self.image.get_rect()[2] - 70) // 2
        self.rect = (self.x, self.y)

