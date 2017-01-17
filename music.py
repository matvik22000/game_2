import  pygame
def play(name):
    pygame.init()
    pygame.time.delay(1000)
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play(-1)
