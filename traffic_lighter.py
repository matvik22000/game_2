import pygame, pygame_init, random, easygui
def game():
    def game():
        easygui.msgbox("Hello. I think you know to do. Good luck!", "accession")
        game = False
        def intersect_classes(car_1, car_2):
            x1 = car_1.x
            x2 = car_2.x
            y1 = car_1.y
            y2 = car_2.y
            x1_size = car_1.x_size
            x2_size = car_2.x_size
            y1_size = car_1.y_size
            y2_size = car_2.y_size
            result = intersect(x1, x2, y1, y2, x1_size, x2_size, y1_size, y2_size)
            return result


        def intersect(s1_x, s2_x, s1_y, s2_y, s1_size_x, s1_size_y, s2_size_x, s2_size_y):
            if ((s1_x > s2_x - s1_size_x) and (s1_x < s2_x + s2_size_x)) and (s1_y > s2_y - s1_size_y) and (s1_y < s2_y + s2_size_y):
                return True
            else:
                return False
        screen = pygame_init.init()
        a = True
        color = False
        green = [0, 255, 0]
        red = [255, 0, 0]
        car_right = pygame.image.load("car_right.png")
        car_left = pygame.image.load("car_left.png")
        car_top = pygame.image.load("car_top.png")
        car_bot = pygame.image.load("car_bot.png")
        score = 0
        time = 0
        class Car_right:
            def __init__(self):
                self.x = 0
                self.y = 380
                self.x_size = 90
                self.y_size = 50
                self.work = True
            def move(self):
                screen.blit(car_right, [self.x, self.y])

                if race:
                    self.x += 5
                if self.x > 400:
                    if not race:
                        self.x += 5
                if not race:
                    if self.x <= 300:
                        self.x += 5
                if self.x > 400 and self.work:
                    self.work = False
                    return True
        class Car_left:
            def __init__(self):
                self.x = 1000
                self.y = 280
                self.x_size = 90
                self.y_size = 50
                self.work = True
            def move(self):
                screen.blit(car_left, [self.x, self.y])
                if self.x >= 600:
                    self.x -= 5
                else:
                    if race:
                        self.x -= 5
                if not race:
                    if self.x <= 500:
                        self.x -= 5
                if self.x < 600 and self.work:
                    self.work = False
                    return True

        class Car_top:
            def __init__(self):
                self.x = 530
                self.y = 700
                self.x_size = 50
                self.y_size = 97
                self.work = True
            def move(self):
                screen.blit(car_top, [self.x, self.y])
                if self.y >= 470:
                    self.y -= 5
                else:
                    if not race:
                        self.y -= 5
                if race:
                    if self.y <= 370:
                        self.y -= 5
                if self.y < 370 and self.work:
                    self.work = False
                    return True

        class Car_bot:
            def __init__(self):
                self.x = 420
                self.y = 0
                self.x_size = 50
                self.y_size = 97
                self.work = True
            def move(self):
                screen.blit(car_bot, [self.x, self.y])
                if self.y <= 150:
                    self.y += 5
                else:
                    if not race:
                        self.y += 5
                if race:
                    if self.y >= 250:
                        self.y += 5
                if self.y > 250 and self.work :
                    self.work = False
                    return True

        car_1 = Car_right()
        car_2 = Car_left()
        cars = [car_1, car_2]

        while a:
                pygame.draw.rect(screen, [255, 255, 255], [0, 0, 1000, 700], 0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        a = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            color = not color
                    if time >= 20:
                        random1 = random.randint(0, 0)
                        if random1 == 0:
                            time = 0
                            random_2 = random.randint(0, 3)
                            if random_2 == 0:
                                car_1 = Car_right()
                                cars.append(car_1)

                            if random_2 == 1:
                                car_2 = Car_left()
                                cars.append(car_2)

                            if random_2 == 2:
                                car_3 = Car_bot()
                                cars.append(car_3)

                            if random_2 == 3:
                                car_4 = Car_top()
                                cars.append(car_4)
                if not color:
                    race = False
                    pygame.draw.rect(screen, red, [400, 340, 20, 20], 0)
                    pygame.draw.rect(screen, red, [600, 340, 20, 20], 0)
                    pygame.draw.rect(screen, green, [495, 450, 20, 20], 0)
                    pygame.draw.rect(screen, green, [495, 250, 20, 20], 0)


                else:
                    race = True
                    pygame.draw.rect(screen, green, [400, 340, 20, 20], 0)
                    pygame.draw.rect(screen, green, [600, 340, 20, 20], 0)
                    pygame.draw.rect(screen, red, [495, 450, 20, 20], 0)
                    pygame.draw.rect(screen, red, [495, 250, 20, 20], 0)
                pygame.draw.rect(screen, [0, 0, 0], [400, 0, 2, 1000], 0)
                pygame.draw.rect(screen, [0, 0, 0], [600, 0, 2, 1000], 0)
                pygame.draw.rect(screen, [0, 0, 0], [0, 450, 1000, 2], 0)
                pygame.draw.rect(screen, [0, 0, 0], [0, 250, 1000, 2], 0)
                for i in cars:
                    q = i.move()
                    if q:
                        score += 1
                    for j in cars:
                        if i != j:
                            if intersect_classes(j, i):
                                choice = easygui.buttonbox("Game over. Your score was: "  + str(score)  + " Would you like to play again?", ["play again", "exit to main menu"], title= "Game over")
                                q = open("score", "w")
                                q.write(str(score))
                                q.close()
                                if choice == "play again":
                                    game = True
                                else:
                                    game = False
                                a = False
                pygame.display.flip()
                time += 1
                pygame.time.delay(30)
        pygame.quit()
        return game
    a = True
    while a:
        a = game()

