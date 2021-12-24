import actions
import pygame
import random


class Loading:
    def __init__(self, width, height, screen):
        self.clock = pygame.time.Clock()
        self.rand_ = random.random()
        self.screen = screen
        self.time = 0
        self.counter = 1
        self.height = height
        self.all_screen = pygame.sprite.Group()
        self.loading = True

        groove = actions.load_image("groove.png")
        bg = actions.load_image("bg.png")
        logo_img = actions.load_image("logo.png")

        self.bg = pygame.sprite.Sprite(self.all_screen)
        self.bg.image = bg
        self.bg.rect = self.bg.image.get_rect()
        self.bg.rect.x = -80
        self.bg.rect.y = -(1670 - height)

        self.groove = pygame.sprite.Sprite(self.all_screen)
        self.groove.image = groove
        self.groove.rect = self.groove.image.get_rect()
        self.groove.rect.x = 540
        self.groove.rect.y = height - height // 3

        self.logo = pygame.sprite.Sprite(self.all_screen)
        self.logo.image = logo_img
        self.logo.image = pygame.transform.scale(logo_img, (self.logo.image.get_rect()[2] * 0.8,
                                                            self.logo.image.get_rect()[3] * 0.8))
        self.logo.rect = self.logo.image.get_rect()
        self.logo.rect.x = (width - self.logo.image.get_rect()[2]) // 2
        self.logo.rect.y = 450

    def rand(self):
        self.rand_ = random.random() / 20

    def show(self):
        bar = actions.load_image("bar.png")
        groove = actions.load_image("groove.png")
        self.time += self.clock.tick() / 1000
        self.all_screen.draw(self.screen)
        if self.time >= self.rand_:
            self.rand()
            if self.counter == 1:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 550
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 2:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 678
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 3:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 806
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 4:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 934
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 5:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 1062
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 6:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = bar
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 1190
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0
                self.counter += 1

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
            elif self.counter == 7:
                self.bar = pygame.sprite.Sprite(self.all_screen)
                self.bar.image = actions.load_image("endBar.png")
                self.bar.rect = self.bar.image.get_rect()
                self.bar.rect.x = 1318
                self.bar.rect.y = self.height - self.height // 3 + 16
                self.time = 0

                self.groove = pygame.sprite.Sprite(self.all_screen)
                self.groove.image = groove
                self.groove.rect = self.groove.image.get_rect()
                self.groove.rect.x = 540
                self.groove.rect.y = self.height - self.height // 3
                self.loading = False

