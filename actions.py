import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert().convert_alpha()
    return image


def rot(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)

    return rotated_image


def jump(width, height, screen):
    run = True
    v2 = 300
    v = 0
    y = 0
    shift = 0
    clock = pygame.time.Clock()
    cube = load_image('cube.png')
    cube = pygame.transform.scale(cube, (70, 70))
    for_rotate = 1
    while run:
        screen.fill((0, 0, 0))
        time = clock.tick()
        y += v * time / 1000  # v * t в с/
        shift += v2 * time / 1000
        if int(shift) == for_rotate:
            for_rotate += 1
            cube = load_image('cube.png')
            cube = pygame.transform.scale(cube, (70, 70))
            cube = rot(cube, -for_rotate)
        pygame.draw.line(screen, (255, 255, 255), (0, height - height // 4), (width, height - height // 4), 1)
        pygame.draw.line(screen, (255, 255, 255), (width // 3 + 35, 0), (width // 3 + 35, 600), 1)
        screen.blit(cube, (width // 3, height - height // 4 - 70 - y))
        pygame.display.flip()
        if y > 140 and abs(v) == v:
            v = -v
        if int(y) < 0 and abs(v) != v:
            break
