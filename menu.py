from drawing import backgroundDraw, groundDraw
from actions import load_image
import pygame

playing_music = False


def play_music(a):
    if a == 'menu':
        pygame.mixer.music.load("music/menu.mp3")
    elif a == '1':
        pygame.mixer.music.load("music/1.mp3")
    elif a == '2':
        pygame.mixer.music.load("music/2.mp3")
    pygame.mixer.music.play(-1)


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
        btnExit_img = load_image("btnExit.png")
        logo_img = load_image("logo.png")

        self.bg1, self.bg2 = backgroundDraw(height, bg, self.menu)

        self.ground_square1, self.ground_square2, self.ground_square3, self.ground_square4, self.ground_square5, \
        self.ground_square6, self.ground_square7 = groundDraw(height, ground, self.menu)

        btnPlay = pygame.sprite.Sprite(self.menu)
        btnPlay.image = pygame.transform.scale(btnPlay_img, (350, 350))
        btnPlay.rect = btnPlay.image.get_rect()
        btnPlay.rect.x = (width - 350) // 2
        btnPlay.rect.y = (height - 350) // 2

        logo = pygame.sprite.Sprite(self.menu)
        logo.image = logo_img
        logo.image = pygame.transform.scale(logo_img, (logo.image.get_rect()[2] * 0.9,
                                                       logo.image.get_rect()[3] * 0.9))
        logo.rect = logo.image.get_rect()
        logo.rect.x = (width - logo.image.get_rect()[2]) // 2
        logo.rect.y = 100

        btnCreate = pygame.sprite.Sprite(self.menu)
        btnCreate.image = pygame.transform.scale(btnCreate_img, (220, 220))
        btnCreate.rect = btnCreate.image.get_rect()
        btnCreate.rect.x = btnPlay.rect.x + 350 + 100
        btnCreate.rect.y = (height - 220) // 2

        #btnIcon = pygame.sprite.Sprite(self.menu)
        #btnIcon.image = pygame.transform.scale(btnIcon_img, (220, 220))
        #btnIcon.rect = btnIcon.image.get_rect()
        #btnIcon.rect.x = btnPlay.rect.x - 100 - 220
        #btnIcon.rect.y = (height - 220) // 2

        btnExit = pygame.sprite.Sprite(self.menu)
        btnExit.image = pygame.transform.scale(btnExit_img, (100, 100))
        btnExit.rect = btnExit.image.get_rect()
        btnExit.rect.x = 10
        btnExit.rect.y = 10

        self.width = width
        self.height = height

    def showExit(self):
        quit_img = load_image("quit.png")

        quit = pygame.sprite.Sprite(self.menu)
        quit.image = quit_img
        quit.image = pygame.transform.scale(quit_img,
                                            (quit.image.get_rect()[2] * 1.3 + 30, quit.image.get_rect()[3] * 1.3))
        quit.rect = quit.image.get_rect()
        quit.rect.x = (self.width - 907) // 2
        quit.rect.y = (self.height - 529) // 2

    def show(self):
        global playing_music
        if not playing_music:
            play_music('menu')
            playing_music = True

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


class Levels:
    def __init__(self, screen, width, height):
        self.rects_ground_squares = []
        self.rects_bg = []
        self.move_bg = 0
        self.v_ground = 770
        self.v_bg = 55

        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = pygame.sprite.Group()

        bg = load_image("bg.png")
        ground = load_image("ground.png")
        logo_img = load_image("LEVELS.png")

        self.bg1, self.bg2 = backgroundDraw(height, bg, self.menu)

        self.ground_square1, self.ground_square2, self.ground_square3, self.ground_square4, self.ground_square5, \
        self.ground_square6, self.ground_square7 = groundDraw(height, ground, self.menu)

        logo = pygame.sprite.Sprite(self.menu)
        logo.image = logo_img
        logo.image = pygame.transform.scale(logo_img, (logo.image.get_rect()[2] * 1,
                                                       logo.image.get_rect()[3] * 1))
        logo.rect = logo.image.get_rect()
        logo.rect.x = (width - logo.image.get_rect()[2]) // 2
        logo.rect.y = 90

        sprite_1_img = load_image("bar4.png")
        sprite1 = pygame.sprite.Sprite(self.menu)
        sprite1.image = sprite_1_img
        sprite1.image = pygame.transform.scale(sprite_1_img, (sprite1.image.get_rect()[2] * 0.7,
                                                              sprite1.image.get_rect()[3] * 0.7))
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = (width - sprite1.image.get_rect()[2]) // 2
        sprite1.rect.y = 0

        sprite_2_img = load_image("bar3.png")
        sprite2 = pygame.sprite.Sprite(self.menu)
        sprite2.image = sprite_2_img
        sprite2.image = pygame.transform.scale(sprite_2_img, (sprite2.image.get_rect()[2] * 0.7,
                                                              sprite2.image.get_rect()[3] * 0.7))
        sprite2.rect = sprite1.image.get_rect()
        sprite2.rect.x = 0
        sprite2.rect.y = height - 190

        sprite_3_img = load_image("bar2.png")
        sprite3 = pygame.sprite.Sprite(self.menu)
        sprite3.image = sprite_3_img
        sprite3.image = pygame.transform.scale(sprite_3_img, (sprite3.image.get_rect()[2] * 0.7,
                                                              sprite3.image.get_rect()[3] * 0.7))
        sprite3.rect = sprite1.image.get_rect()
        sprite3.rect.x = width - 190
        sprite3.rect.y = height - 190

        btnExit_img = load_image("bntExitmenu.png")
        btnExit = pygame.sprite.Sprite(self.menu)
        btnExit.image = pygame.transform.scale(btnExit_img, (90, 100))
        btnExit.rect = btnExit.image.get_rect()
        btnExit.rect.x = 10
        btnExit.rect.y = 10

        level_1_img = load_image("RUSSIAN_ROADS_LEVEL.png")
        level_1 = pygame.sprite.Sprite(self.menu)
        level_1.image = level_1_img
        level_1.image = pygame.transform.scale(level_1_img, (level_1.image.get_rect()[2] * 0.5,
                                                             level_1.image.get_rect()[3] * 0.5))
        level_1.rect = level_1.image.get_rect()
        print(level_1.image.get_rect()[2])
        level_1.rect.x = (width - 350) // 2 - 370
        level_1.rect.y = 460

        level_2_img = load_image("INFERNAL_MASTURBATION_LEVEL.png")
        level_2 = pygame.sprite.Sprite(self.menu)
        level_2.image = level_2_img
        level_2.image = pygame.transform.scale(level_2_img, (level_2.image.get_rect()[2] * 0.5,
                                                             level_2.image.get_rect()[3] * 0.5))
        level_2.rect = level_2.image.get_rect()
        print(level_2.image.get_rect()[2])
        level_2.rect.x = (width - 350) // 2 - 395
        level_2.rect.y = 120

        self.width = width
        self.height = height

    def show(self):
        global playing_music
        if not playing_music:
            play_music('menu')
            playing_music = True

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


class Settings:
    def __init__(self, screen, width, height):
        self.rects_ground_squares = []
        self.rects_bg = []
        self.move_bg = 0
        self.v_ground = 770
        self.v_bg = 55

        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = pygame.sprite.Group()

        bg = load_image("bg.png")
        ground = load_image("ground.png")
        logo_img = load_image("SETTINGS.png")
        logo_music_img = load_image("Music.png")
        OFF_img = load_image("OFF.png")
        ON_img = load_image("ON.png")

        self.bg1, self.bg2 = backgroundDraw(height, bg, self.menu)

        self.ground_square1, self.ground_square2, self.ground_square3, self.ground_square4, self.ground_square5, \
        self.ground_square6, self.ground_square7 = groundDraw(height, ground, self.menu)

        logo = pygame.sprite.Sprite(self.menu)
        logo.image = logo_img
        logo.image = pygame.transform.scale(logo_img, (logo.image.get_rect()[2] * 1,
                                                       logo.image.get_rect()[3] * 1))
        logo.rect = logo.image.get_rect()
        logo.rect.x = (width - logo.image.get_rect()[2]) // 2
        logo.rect.y = 90

        logo_music = pygame.sprite.Sprite(self.menu)
        logo_music.image = logo_music_img
        logo_music.image = pygame.transform.scale(logo_music_img, (logo_music.image.get_rect()[2] * 1,
                                                       logo_music.image.get_rect()[3] * 1))
        logo_music.rect = logo_music.image.get_rect()
        logo_music.rect.x = (width - logo_music.image.get_rect()[2]) // 2 - 500
        logo_music.rect.y = 300

        OFF = pygame.sprite.Sprite(self.menu)
        OFF.image = OFF_img
        OFF.image = pygame.transform.scale(OFF_img, (OFF.image.get_rect()[2] * 1,
                                                                   OFF.image.get_rect()[3] * 1))
        OFF.rect = OFF.image.get_rect()
        OFF.rect.x = (width - OFF.image.get_rect()[2]) // 2 - 200
        OFF.rect.y = 270

        ON = pygame.sprite.Sprite(self.menu)
        ON.image = ON_img
        ON.image = pygame.transform.scale(ON_img, (ON.image.get_rect()[2] * 1,
                                                     ON.image.get_rect()[3] * 1))
        ON.rect = ON.image.get_rect()
        ON.rect.x = (width - ON.image.get_rect()[2]) // 2 + 100
        ON.rect.y = 270

        sprite_1_img = load_image("bar4.png")
        sprite1 = pygame.sprite.Sprite(self.menu)
        sprite1.image = sprite_1_img
        sprite1.image = pygame.transform.scale(sprite_1_img, (sprite1.image.get_rect()[2] * 0.7,
                                                              sprite1.image.get_rect()[3] * 0.7))
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = (width - sprite1.image.get_rect()[2]) // 2
        sprite1.rect.y = 0

        sprite_2_img = load_image("bar3.png")
        sprite2 = pygame.sprite.Sprite(self.menu)
        sprite2.image = sprite_2_img
        sprite2.image = pygame.transform.scale(sprite_2_img, (sprite2.image.get_rect()[2] * 0.7,
                                                              sprite2.image.get_rect()[3] * 0.7))
        sprite2.rect = sprite1.image.get_rect()
        sprite2.rect.x = 0
        sprite2.rect.y = height - 190

        sprite_3_img = load_image("bar2.png")
        sprite3 = pygame.sprite.Sprite(self.menu)
        sprite3.image = sprite_3_img
        sprite3.image = pygame.transform.scale(sprite_3_img, (sprite3.image.get_rect()[2] * 0.7,
                                                              sprite3.image.get_rect()[3] * 0.7))
        sprite3.rect = sprite1.image.get_rect()
        sprite3.rect.x = width - 190
        sprite3.rect.y = height - 190

        btnExit_img = load_image("bntExitmenu.png")
        btnExit = pygame.sprite.Sprite(self.menu)
        btnExit.image = pygame.transform.scale(btnExit_img, (90, 100))
        btnExit.rect = btnExit.image.get_rect()
        btnExit.rect.x = 10
        btnExit.rect.y = 10


        self.width = width
        self.height = height


    def show(self):
        global playing_music
        if not playing_music:
            play_music('menu')
            playing_music = True

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