import pygame
import actions


class Cube(pygame.sprite.Sprite):
    def __init__(self, width, height, screen, *group):
        super().__init__(*group)
        self.v2 = 1280 * 2
        self.v = 2300 * 2
        self.y = 0
        self.shift = 0
        self.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.for_rotate = 1
        self.rect = (-70, height - height // 4 - 70)
        self.x = -70
        self.test = 0
        self.time = 1
        self.width = width
        self.height = height
        self.screen = screen
        self.counter = 0
        self.clock = pygame.time.Clock()
        self.cube = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.moving = True

    def jump(self):
        self.time = self.clock.tick() / 1000
        if self.time > 0.002:
            self.time = 0.002
        if self.rect[1] < self.height - self.height // 4 - 70 - 155 and abs(self.v) == self.v:
            self.v = -self.v
        self.y += self.v * self.time  # v * t в с/
        self.shift += self.v2 * self.time
        if int(self.shift) >= self.for_rotate:
            self.for_rotate += int(self.shift) - self.for_rotate
            if self.counter % 2 == 0:
                self.image = self.cube
            else:
                self.image = actions.rotation(self.cube, 180)
            self.image = actions.rotation(self.image, -self.for_rotate)
        if self.moving:
            self.rect = (
                self.x - (self.image.get_rect()[2] - 70) // 2,
                self.height - self.height // 4 - 70 - self.y - (self.image.get_rect()[2] - 70) // 2)
        else:
            self.rect = (
                self.width // 3 - (self.image.get_rect()[2] - 70) // 2,
                self.height - self.height // 4 - 70 - self.y - (self.image.get_rect()[2] - 70) // 2)

    def get_cords(self):
        return self.rect
