import pygame
import actions


class Cube:
    def __init__(self, width, height, screen):
        self.v2 = 390
        self.v = 600
        self.y = 0
        self.shift = 0
        self.cube = pygame.sprite.Sprite()
        self.cube.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
        self.for_rotate = 1
        self.cords = (width // 3, height - height // 4 - 70)
        self.test = 0
        self.time = 1
        self.width = width
        self.height = height
        self.screen = screen
        self.counter = 0
        self.clock = pygame.time.Clock()

    def jump(self):
        self.time = self.clock.tick() / 1000
        if self.time > 0.002:
            self.time = 0.002
        if self.cords[1] < self.height - self.height // 4 - 70 - 140 and abs(self.v) == self.v:
            self.v = -self.v
        self.y += self.v * self.time  # v * t в с/
        self.shift += self.v2 * self.time
        if int(self.shift) == self.for_rotate:
            self.for_rotate += 1
            self.cube = pygame.sprite.Sprite()
            if self.counter % 2 == 0:
                self.cube.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
            else:
                self.cube.image = pygame.transform.scale(actions.rot(actions.load_image('cube.png'), 180), (70, 70))
            self.cube.image = actions.rot(self.cube.image, -self.for_rotate)
        self.cords = (
            self.width // 3 - (self.cube.image.get_rect()[2] - 70) // 2,
            self.height - self.height // 4 - 70 - self.y - (self.cube.image.get_rect()[2] - 70) // 2)

    def show(self):
        if self.get_cords()[1] < self.height - self.height // 4 - 70:
            self.jump()
        elif self.cords[1] >= self.height - self.height // 4 - 70 and abs(self.v) != self.v:
            self.v = -self.v
            self.counter += 1
            self.cords = (self.width // 3, self.height - self.height // 4 - 70)
            self.y = 0
            self.shift = 0
            self.for_rotate = 0
        else:
            if self.counter % 2 == 0:
                self.cube.image = pygame.transform.scale(actions.load_image('cube.png'), (70, 70))
            else:
                self.cube.image = pygame.transform.scale(actions.rot(actions.load_image('cube.png'), 180), (70, 70))
        self.screen.blit(self.cube.image, self.cords)

    def get_cords(self):
        return self.cords
