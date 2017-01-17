import pygame


def init(size = [1000, 700], color = [255, 255, 255]):
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(color)
    return screen


def loop_start(screen, color = [255 ,255, 255], size_x = 1000, size_y = 700, ):
    a = True
    pygame.draw.rect(screen, color, [0, 0, size_x, size_y], 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    return a

def loop_end(delay = 30, t = False, time = 0):
    pygame.display.flip()
    pygame.time.delay(delay)
    if t:
        time += 1
        return time
def key_pressed(k):
    key = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k:
                key = True
    return key