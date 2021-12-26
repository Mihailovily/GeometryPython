import pygame
import actions


class Cube(pygame.sprite.Sprite):
    def __init__(self, width, height, screen, *group):
        super().__init__(*group)
        self.v2 = 410
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
        self.cube = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.moving = True

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
            self.for_rotate += int(self.shift) - self.for_rotate

            if self.counter % 2 == 0:
                self.image = self.cube
            else:
                self.image = actions.rotation(self.cube, 180)

            self.image = actions.rotation(self.image, -self.for_rotate)

        if self.moving:
            self.x -= (self.image.get_rect()[2] - 70) // 2
            self.x += self.time * 770
        else:
            self.x = self.width // 3 - (self.image.get_rect()[2] - 70) // 2
        self.y = self.height - self.height // 4 - 70 - self.move_vertical - self.floor
        self.y -= (self.image.get_rect()[2] - 70) // 2
        self.rect = (self.x, self.y)

    def update(self):
        if self.move_vertical == 0 and abs(
                self.v) != self.v:
            self.v = -self.v
            self.counter += 1
            self.y = self.height - self.height // 4 - 70 - self.floor
            self.move_vertical = 0
            self.shift = 0
            self.for_rotate = 0
            if self.counter % 2 == 0:
                self.image = self.cube
            else:
                self.image = actions.rotation(self.cube, 180)

        if self.x < self.width // 3:
            move = 770 * self.time
            self.x += move
        else:
            self.moving = False
        self.rect = (self.x, self.y)
