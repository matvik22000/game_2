import  pygame, pygame_init, easygui, random
time = 0
screen = pygame_init.init()
a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
    key = pygame_init.key_pressed("K_SPACE")
    if key:
        print "key pressed"
    pygame_init.loop_end()
