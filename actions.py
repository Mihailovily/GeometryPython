import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert().convert_alpha()
    return image


def rot_center(image, angle):
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image


def jump(width, height, screen):
    # expand = False
    # rev = False
    run = True
    # expand2 = False
    # v3 = 250 / 2 - 10
    v2 = 1
    # v = 0
    y = 0
    point1 = (width // 3, height - height // 4)
    point2 = (width // 3 + 70, height - height // 4)
    point3 = (width // 3 + 70, height - height // 4 - 70)
    point4 = (width // 3, height - height // 4 - 70)
    clock = pygame.time.Clock()
    cube = load_image('cube.png')
    cube = pygame.transform.scale(cube, (70, 70))
    rotate = 0
    while run:
        screen.fill((0, 0, 0))
        time = clock.tick()
        # y += v * time / 1000  # v * t в секундах
        shift = v2 * time / 1000
        rotate += shift
        cube = rot_center(cube, rotate)
        # shift2 = v3 * time / 1000
        pygame.draw.line(screen, (255, 255, 255), (0, height - height // 4), (width, height - height // 4), 1)
        screen.blit(cube, (width // 3, height - height // 4 - 70 - y))
        # if not rev:
        #     point1 = (point1[0] - shift2, point1[1] - shift)
        #     point2 = (point2[0] - shift, point2[1] + shift2)
        #     point3 = (point3[0] + shift2, point3[1] + shift)
        #     point4 = (point4[0] + shift, point4[1] - shift2)
        # else:
        #     pass
        #     point1 = (point1[0] + shift, point1[1] - shift2)
        #     point2 = (point2[0] - shift2, point2[1] - shift)
        #     point3 = (point3[0] - shift, point3[1] + shift2)
        #     point4 = (point4[0] + shift2, point4[1] + shift)
        pygame.display.flip()
        # if y > 70 and not expand:
        #     v3 = -v3
        #     expand = True
        # if y < 70 and expand2:
        #     v3 = -v3
        #     expand2 = False
        #     expand = False
        # if y > 140 and not rev and abs(v) == v:
        #     rev = True
        if y > 140 and abs(v) == v:
            v = -v
        if int(y) < 0 and abs(v) != v:
            break
