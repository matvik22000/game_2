import pygame, pygame_init, random, crash, writer, easygui, music
def shooter(rocket, delay):
    def game(rocket, delay):
        col_5 = 0
        col_change_5 = 30
        regarmor =False
        reghp = False
        music.play("Counter-strike_1.6-Zak_Belica_(glavnaya_tema_-_fonovaya_muzyka_v_nachale_igry).mp3")
        tick = 0
        col_1 = 0
        col_2 = 0
        col_3 = 255
        col4 = 0
        col5 = 0
        col6 = 255
        move = True
        time_dron = 0
        health = 5
        portal_range = 150
        portal_reload = 200
        pause = True
        p = False
        try:
            file = open("score_shooter")
        except IOError:
            f = open("score_shooter", "w")
            f.write("0")
            f.close()
        else:
            file.close()
        score = 0
        screen = pygame.display.set_mode([500, 700])
        screen.fill([255, 255, 255])
        left = False
        right = False
        a = True
        time = 10
        reloading = 0
        enemies = []
        ammo_list = []
        enemy_ammo_list = []
        ammo = 5
        armor = 20
        spell = "shield"
        spell_time = 60
        spell_reload = 500
        spell_used = False
        spell_ready = False
        up = False
        portal = 200
        lightning = pygame.image.load("lightning.png")
        ammo_p = pygame.image.load("ammo.png")
        space_ship_p = pygame.image.load("space_ship.png")
        speed_nr = 7
        if rocket == "rocket":
            ammo = 5
            armor = 30
            speed_nr = 8
            spell = "shield"
            spell_time = 150
            space_ship_p = pygame.image.load("space_ship.png")
        if rocket == "rocket_2":
            ammo = 15
            armor = 15
            speed_nr = 10
            spell = "gun"
            space_ship_p = pygame.image.load("space_ship_2.png")
            spell_time = 100
        if rocket == "rocket_3":
            ammo = 10
            armor = 15
            speed_nr = 15
            spell = "speed"
            spell_time = 150
            space_ship_p = pygame.image.load("space_shhip_3.png")
        if rocket == "rocket_4":
            ammo = 10
            armor = 20
            speed_nr = 15
            spell = "electronic"
            spell_time = 100
            lightning = pygame.image.load("lightning.png")
            space_ship_p = pygame.image.load("space_ship_4.png")
        if rocket == "rocket_5":
            ammo = 10
            armor = 25
            speed_nr = 10
            spell = "dron"
            spell_time = 200
            dron_p = pygame.image.load("dron.png")
            space_ship_p = pygame.image.load("space_ship_5.png")
        enemy_p = pygame.image.load("enemy.png")
        ammo_enemy = pygame.image.load("ammo_enemy.png")
        txt_1 = writer.read_file("motor")
        if writer.str2bool(txt_1):
            speed_nr += 5
        txt_2 = writer.read_file("armor")
        if writer.str2bool(txt_2):
            armor += 5
        txt_3 = writer.read_file("ammo")
        if writer.str2bool(txt_3):
            ammo += 5
        txt_3 = writer.read_file("hp")
        if writer.str2bool(txt_3):
            health += 5
        txt_3 = writer.read_file("portal")
        if writer.str2bool(txt_3):
            portal_range +=50
            portal_reload -= 50
        txt_3 = writer.read_file("reghp")
        if writer.str2bool(txt_3):
            reghp = True
        txt_3 = writer.read_file("regarmor")
        if writer.str2bool(txt_3):
            regarmor = True

        speed = speed_nr
        col = 0
        spell_time_r = spell_time
        used = False
        col_change = 50

        col_change2 = 30
        col_change3 = 10
        bl_1 = 0
        bl_2 = 255
        class Dron():
            def __init__(self):
                self.x = ship.x
                self.y = ship.y
                self.max_move = 10
                self.ammo = 1
            def move(self):
                for i in enemies:
                    self.x_w = i.x
                self.dx = self.x_w - self.x
                if self.dx > 0:
                    dx = min(self.dx, self.max_move)
                    self.x += dx
                elif self.dx < 0:
                    self.dx = max(self.dx, -self.max_move)
                    self.x += self.dx
                if self.dx == 0:
                    self.shoot()
                screen.blit(dron_p, [self.x, self.y])
            def shoot(self):
                if self.ammo > 0:
                    ammo_d = AmmoDron()
                    ammo_list.append(ammo_d)
                    self.ammo -= 1
                    time_dron = 0
                if self.ammo <= 0:
                    global time_dron
                    time_dron += 1
                if time_dron >= 20:
                    self. ammo = 1
        class AmmoDron():
            def __init__(self):
                self.x = dron.x + 10
                self.y = dron.y
                self.x_size = 5
                self.y_size = 15

            def shoot(self):
                self.y -= 10
                screen.blit(ammo_p, [self.x, self.y])

        class SpaceShip():
            def __init__(self):
                self.x = 230
                self.y = 600
                self.x_size = 40
                self.y_size = 81
                self.ammo = ammo
            def fly_right(self):
                if self.x <= 494:
                    self.x += speed
                screen.blit(space_ship_p, [self.x, self.y])
            def fly_left(self):
                if self.x >= 6:
                    self.x -= speed
                screen.blit(space_ship_p, [self.x, self.y])
            def draw(self):
                screen.blit(space_ship_p, [self.x, self.y])

        class Ammo():
            def __init__(self):
                self.x = ship.x + 10
                self.y = ship.y
                self.x_size = 20
                self.y_size = 15
            def shoot(self):
                self.y -= 15
            def draw(self):
                screen.blit(ammo_p, [self.x, self.y])
        class Enemy():
            def __init__(self):
                self.x = random.randint(0, 460)
                self.y = 0
                self.x_size = 40
                self.y_size = 40
                self.shoot_time = tick - 50
            def move(self):
                self.y += 7
            def draw(self):
                screen.blit(enemy_p, [self.x, self.y])
            def shoot(self):
                if self.shoot_time + 50 <= tick:
                    self.shoot_time = tick
                    enemy_ammo_list.append([self.x, self.y, 5, 15])

        col3 = 0
        col2 = 0
        ship = SpaceShip()
        dron = Dron()
        while a:
            p = False
            if regarmor:
                armor += 0.001
            if reghp:
                health += 0.001
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 500, 700], 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    a = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        right = True
                    if event.key == pygame.K_LEFT:
                        left = True
                    if event.key == pygame.K_d and portal <= 0:

                        pygame.draw.circle(screen, [0, 0, 255], [ship.x + 100, ship.y], 20)
                        ship.x += portal_range
                        portal = portal_reload
                    if event.key == pygame.K_a and portal <= 0:

                        pygame.draw.circle(screen, [0, 0, 255], [ship.x - 100, ship.y], 20)
                        ship.x -= portal_range
                        portal = portal_reload
                    if event.key == pygame.K_SPACE:
                        pause = True
                        if ship.ammo > 0:
                            ship.ammo -= 1
                            ammo_P = Ammo()
                            ammo_list.append(ammo_P)
                    if event.key == pygame.K_p:
                        p = True
                    if event.key == pygame.K_UP:
                        up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        right = False
                    if event.key == pygame.K_LEFT:
                        left = False
                    if event.key == pygame.K_UP:
                       up = False



            #end of events
            #events line
            #if left:
             #   pause = True
            if p:
               pause = not pause
            if not pause:

                writer.write("paused", screen, 250, 350, color = [col_5, col_5, col_5])
                col_5 += col_change_5
                if col_5 >= 255:
                    col_5 = 255
                    col_change_5 = -col_change_5
                if col_5 <= 0:
                    col_5 = 0
                    col_change_5 = -col_change_5

            if pause:
                portal -= 1
                if portal <= 0:
                    portal = 0
                if time >= 30:
                    enemy = Enemy()
                    enemies.append(enemy)
                    time = 0
                index = -1
                for i in enemies:
                    ammo_index = -1
                    index += 1
                    if move:
                        i.move()
                        i.shoot()

                    if i.y >= 600:
                        health -= 1
                        enemies.pop(index)
                    for j in ammo_list:
                        ammo_index += 1
                        crash_c = crash.intersect_classes(i, j)
                        if j.y <= 0:
                            ammo_list.pop(ammo_index)
                        if crash_c:
                            enemies.pop(index)
                            ammo_list.pop(ammo_index)
                            pygame.draw.circle(screen, [255, 0, 0], [j.x, j.y], 20, 0)
                            score += 1

                rem = -1
                for i in enemy_ammo_list:
                    rem += 1
                    i[1] += 10
                    screen.blit(ammo_enemy, [i[0], i[1]])
                    if i[1] >= 590:
                        enemy_ammo_list.pop(rem)

                remove = -1
                for l in enemy_ammo_list:
                    q = crash.intersect_class(ship, l[0], l[1], l[2], l[3])
                    remove += 1
                    if q:
                        armor -= 1
                        pygame.draw.circle(screen, [255, 0, 0], [l[0], l[1]], 30, 0)
                        enemy_ammo_list.pop(remove)
                for i in ammo_list:
                    i.shoot()
                if spell_used:
                    spell_time_r -= 1
                if spell_time_r <= 0:
                    spell_used = False
                    spell_ready = False
                    used = False
                    spell_time_r = spell_time
                    spell_reload = 500
                    move = True

                else:
                    spell_reload -= 1
                    if spell_reload <= 0:
                        spell_ready = True






################################################################################################################
            for i in enemy_ammo_list:
                screen.blit(ammo_enemy, [i[0], i[1]])
            for l in ammo_list:
                l.draw()
            if up:
                if spell_ready:
                    used = True

            if used:
                if spell_ready:
                    if spell == "shield":
                        spell_used = True
                        pygame.draw.rect(screen, [255, 0, 0], [ship.x - 20, 570, 80, 20])
                        ind = -1
                        for l in enemy_ammo_list:
                            ind += 1
                            cr = crash.intersect(l[0], ship.x - 20, l[1], 570, l[2], l[3], 80, 20)
                            if cr:
                                pygame.draw.circle(screen, [0, 0, 255], [l[0], l[1]], 20)
                                enemy_ammo_list.pop(ind)
                        ind = -1
                        for l in enemies:
                            ind += 1
                            cr = crash.intersect(l.x, ship.x - 20, l.y, 570, l.x_size, l.y_size, 80, 20)
                            if cr:
                                pygame.draw.circle(screen, [0, 0, 255], [l.x, l.y], 20)
                                enemies.pop(ind)

                    if spell == "gun":
                        screen.blit(ammo_p, [20, 200])
                        spell_used = True
                        ammo_s = Ammo()
                        ammo_list.append(ammo_s)
                    if spell == "speed":
                        spell_used = True
                        armor += 0.03
                        health += 0.01
                        bl_1 += bl_2
                        if bl_1 >= 255:
                            bl_2 = -bl_2
                        if bl_1 <= 0:
                            bl_2 = -bl_2
                        pygame.draw.rect(screen, [bl_1, 255, bl_1], [230, 320, 40, 10])
                        pygame.draw.rect(screen, [bl_1, 255, bl_1], [245, 305, 10, 40])
                    if spell == "electronic":
                        spell_used = True
                        rand_x = random.randint(60, 400)
                        rand_y = random.randint(0, 700)
                        screen.blit(lightning, [rand_x, rand_y])
                        move = False
                        ship.ammo = 1
                    if spell == "dron":
                        spell_used = True
                        dron.move()

            if spell_ready:
                if col_1 > 10:
                    col_1 -= 10
                if col_1 <= 10:
                    col_1 = 255
                if col_2 > 10:
                    col_2 -= 10
                if col_2 >= 10:
                    col_2 = 255
                if col_3 > 10:
                    col_3 -= 10
                if col_3 <= 10:
                    col_3 = 255
                pygame.draw.rect(screen, [col_1, col_2, col_3], [10, 80, 20, spell_time_r])
                pygame.draw.rect(screen, [col_1, col_2, col_3], [10, 80, 20, spell_time], 1)
                writer.write("ready", screen, 35, 80, color=[col2, col2, col2])

                col2 += col_change2
                if col2 >= 255:
                    col_change2 = -col_change2
                    col2 = 255
                if col2 <= 0:
                    col_change2 = -col_change2
                    col2 = 0

            elif not spell_ready:
                pygame.draw.rect(screen, [0, 0, 0], [10, 80, 20, spell_reload / 5])
                pygame.draw.rect(screen, [0, 0, 0], [10, 80, 20, 500 / 5], 1)
                writer.write("reloading", screen, 35, 80, color=[col3, col3, col3])

                col3 += col_change3
                if col3 >= 255:
                    col_change3 = -col_change3
                    col3 = 255
                if col3 <= 0:
                    col_change3 = -col_change3
                    col3 = 0
            pygame.draw.rect(screen, [0, 0, 255], [460, 100, 20, portal_reload], 1)
            pygame.draw.rect(screen, [0, 0, 255, ], [460, 100, 20, portal])
            writer.write("portal:", screen, 440, 50, color=[0, 0, 255])

            if portal > 0:
                if col4 > 10:
                    col4 -= 10
                if col4 <= 10:
                    col4 = 255
                if col5 > 10:
                    col5 -= 10
                if col5 >= 10:
                    col5 = 255
                if col6 > 10:
                    col6 -= 10
                if col6 <= 10:
                    col6 = 255
                portal_2 = portal / 30
                writer.write("reloading", screen, 415, 350, size=16, color=[0, 0, 255])
                writer.write("left: %i" % portal_2, screen=screen, x=415, y=370, color=[0, 0, 255])
            else:
                if col4 > 10:
                    col4 -= 10
                if col4 <= 10:
                    col4 = 255
                if col5 > 10:
                    col5 -= 10
                if col5 >= 10:
                    col5 = 255
                if col6 > 10:
                    col6 -= 10
                if col6 <= 10:
                    col6 = 255
                writer.write("ready", screen, 450, 350, color=[col4, col5, col6])
                writer.write("portal:", screen, 440, 50, color=[col4, col5, col6])
                pygame.draw.rect(screen, [col4, col5, col6], [460, 100, 20, 200], 1)
                pygame.draw.rect(screen, [col4, col5, col6], [460, 100, 20, 200])
            if left:
                ship.fly_left()
            if right:
                ship.fly_right()
            ship.draw()

            if ship.ammo <= 0:
                writer.write("reloading", screen, 200, 300, color=[col, col, col])
                col += col_change
                if col >= 255:
                    col_change = -col_change
                    col = 255
                if col <= 0:
                    col_change = -col_change
                    col = 0
                reloading += 1
            if reloading == 40:
                ship.ammo = ammo
                reloading = 0
            writer.write(txt="health: %i" % float(health), screen=screen, x=20, y=20)
            writer.write(txt="armor: %i" % float(armor), screen=screen, x=20, y=40)
            writer.write(txt="ammo: %i" % ship.ammo, screen=screen, x=20, y=60)

            for i in enemies:
                i.draw()

            time = pygame_init.loop_end(t=True, time=time, delay=delay)
            tick += 1

            if health <= 0 or armor <= 0:
                a = False
                t = open("score_shooter", "r")
                r = t.read()
                t.close()
                if r == '':
                    p = open("score_shooter", "w")
                    p.write("0000")
                    p.close()
                t = open("score_shooter", "r")
                r = t.read()
                t.close()
                t = open("score_shooter", "w")
                t.write(str(int(r) + int(score * 2)))
                t.close()

                choice = easygui.buttonbox(
                    "Game over. Your score was: " + str(score * 2) + ". Would you lake to play again?",
                    ["play again", "exit to main menu"])
                if choice == "play again":
                    return True
                else:
                    return False


    game_2 = True
    while game_2:
        game_2 = game(rocket, delay)
    pygame.display.quit()
    pygame.mixer.music.stop()




#############################################################################################################
#############################################################################################################
#############################################################################################################




import pygame, pygame_init, random, crash, writer, easygui, music, sys
from  PyQt4 import QtGui, QtCore
def tutorial(rocket, delay):
    def game(rocket, delay):
        tutorial = True
        col_5 = 0
        col_change_5 = 30
        regarmor =False
        reghp = False
        music.play("Counter-strike_1.6-Zak_Belica_(glavnaya_tema_-_fonovaya_muzyka_v_nachale_igry).mp3")
        tick = 0
        col_1 = 0
        col_2 = 0
        col_3 = 255
        col4 = 0
        col5 = 0
        col6 = 255
        move = True
        time_dron = 0
        health = 5
        portal_range = 150
        portal_reload = 200
        pause = True
        p = False
        try:
            file = open("score_shooter")
        except IOError:
            f = open("score_shooter", "w")
            f.write("0")
            f.close()
        else:
            file.close()
        score = 0
        screen = pygame.display.set_mode([500, 700])
        screen.fill([255, 255, 255])
        left = False
        right = False
        a = True
        time = 10
        reloading = 0
        enemies = []
        ammo_list = []
        enemy_ammo_list = []
        ammo = 5
        armor = 20
        spell = "shield"
        spell_time = 60
        spell_reload = 500
        spell_used = False
        spell_ready = False
        up = False
        portal = 200
        lightning = pygame.image.load("lightning.png")
        ammo_p = pygame.image.load("ammo.png")
        space_ship_p = pygame.image.load("space_ship.png")
        speed_nr = 7
        if rocket == "rocket":
            ammo = 5
            armor = 30
            speed_nr = 8
            spell = "shield"
            spell_time = 150
            space_ship_p = pygame.image.load("space_ship.png")
        if rocket == "rocket_2":
            ammo = 15
            armor = 15
            speed_nr = 10
            spell = "gun"
            space_ship_p = pygame.image.load("space_ship_2.png")
            spell_time = 100
        if rocket == "rocket_3":
            ammo = 10
            armor = 15
            speed_nr = 15
            spell = "speed"
            spell_time = 150
            space_ship_p = pygame.image.load("space_shhip_3.png")
        if rocket == "rocket_4":
            ammo = 10
            armor = 20
            speed_nr = 15
            spell = "electronic"
            spell_time = 100
            lightning = pygame.image.load("lightning.png")
            space_ship_p = pygame.image.load("space_ship_4.png")
        if rocket == "rocket_5":
            ammo = 10
            armor = 25
            speed_nr = 10
            spell = "dron"
            spell_time = 200
            dron_p = pygame.image.load("dron.png")
            space_ship_p = pygame.image.load("space_ship_5.png")
        enemy_p = pygame.image.load("enemy.png")
        ammo_enemy = pygame.image.load("ammo_enemy.png")



        speed = speed_nr
        col = 0
        spell_time_r = spell_time
        used = False
        col_change = 50

        col_change2 = 30
        col_change3 = 10
        bl_1 = 0
        bl_2 = 255
        class Dron():
            def __init__(self):
                self.x = ship.x
                self.y = ship.y
                self.max_move = 10
                self.ammo = 1
            def move(self):
                for i in enemies:
                    self.x_w = i.x
                self.dx = self.x_w - self.x
                if self.dx > 0:
                    dx = min(self.dx, self.max_move)
                    self.x += dx
                elif self.dx < 0:
                    self.dx = max(self.dx, -self.max_move)
                    self.x += self.dx
                if self.dx == 0:
                    self.shoot()
                screen.blit(dron_p, [self.x, self.y])
            def shoot(self):
                if self.ammo > 0:
                    ammo_d = AmmoDron()
                    ammo_list.append(ammo_d)
                    self.ammo -= 1
                    time_dron = 0
                if self.ammo <= 0:
                    global time_dron
                    time_dron += 1
                if time_dron >= 20:
                    self. ammo = 1
        class AmmoDron():
            def __init__(self):
                self.x = dron.x + 10
                self.y = dron.y
                self.x_size = 5
                self.y_size = 15

            def shoot(self):
                self.y -= 15
                screen.blit(ammo_p, [self.x, self.y])

        class SpaceShip():
            def __init__(self):
                self.x = 230
                self.y = 600
                self.x_size = 40
                self.y_size = 81
                self.ammo = ammo
            def fly_right(self):
                if self.x <= 494:
                    self.x += speed
                screen.blit(space_ship_p, [self.x, self.y])
            def fly_left(self):
                if self.x >= 6:
                    self.x -= speed
                screen.blit(space_ship_p, [self.x, self.y])
            def draw(self):
                screen.blit(space_ship_p, [self.x, self.y])

        class Ammo():
            def __init__(self):
                self.x = ship.x + 10
                self.y = ship.y
                self.x_size = 20
                self.y_size = 15
            def shoot(self):
                self.y -= 15
            def draw(self):
                screen.blit(ammo_p, [self.x, self.y])
        class Enemy():
            def __init__(self):
                self.x = random.randint(0, 460)
                self.y = 0
                self.x_size = 40
                self.y_size = 40
                self.shoot_time = tick - 50
            def move(self):
                self.y += 7
            def draw(self):
                screen.blit(enemy_p, [self.x, self.y])
            def shoot(self):
                if self.shoot_time + 50 <= tick:
                    self.shoot_time = tick
                    enemy_ammo_list.append([self.x, self.y, 5, 15])

        col3 = 0
        col2 = 0
        ship = SpaceShip()
        dron = Dron()
        while a:
            if tutorial:
                pause = False
                easygui.msgbox("Hello. Let start tutorial. In top left corner, You can see your health, armor and ammo, indicator and inscription, wich say ready your spell, or not. on right, you can see all about 'portal'. press 'p' to continue")
                tutorial = False
            p = False
            if regarmor:
                armor += 0.001
            if reghp:
                health += 0.001
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 500, 700], 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    a = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        right = True
                    if event.key == pygame.K_LEFT:
                        left = True
                    if event.key == pygame.K_d and portal <= 0:

                        pygame.draw.circle(screen, [0, 0, 255], [ship.x + 100, ship.y], 20)
                        ship.x += portal_range
                        portal = portal_reload
                    if event.key == pygame.K_a and portal <= 0:

                        pygame.draw.circle(screen, [0, 0, 255], [ship.x - 100, ship.y], 20)
                        ship.x -= portal_range
                        portal = portal_reload
                    if event.key == pygame.K_SPACE:
                        pause = True
                        if ship.ammo > 0:
                            ship.ammo -= 1
                            ammo_P = Ammo()
                            ammo_list.append(ammo_P)
                    if event.key == pygame.K_p:

                        p = True
                    if event.key == pygame.K_UP:
                        up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        right = False
                    if event.key == pygame.K_LEFT:
                        left = False
                    if event.key == pygame.K_UP:
                       up = False



            #end of events
            #events line
            #if left:
             #   pause = True
            if p:
               pause = not pause
            if not pause:

                writer.write("paused", screen, 250, 350, color = [col_5, col_5, col_5])
                col_5 += col_change_5
                if col_5 >= 255:
                    col_5 = 255
                    col_change_5 = -col_change_5
                if col_5 <= 0:
                    col_5 = 0
                    col_change_5 = -col_change_5

            if pause:
                portal -= 1
                if portal <= 0:
                    portal = 0
                if time >= 30:
                    enemy = Enemy()
                    enemies.append(enemy)
                    time = 0
                index = -1
                for i in enemies:
                    ammo_index = -1
                    index += 1
                    if move:
                        i.move()
                        i.shoot()

                    if i.y >= 600:
                        health -= 1
                        enemies.pop(index)
                    for j in ammo_list:
                        ammo_index += 1
                        crash_c = crash.intersect_classes(i, j)
                        if j.y <= 0:
                            ammo_list.pop(ammo_index)
                        if crash_c:
                            enemies.pop(index)
                            ammo_list.pop(ammo_index)
                            pygame.draw.circle(screen, [255, 0, 0], [j.x, j.y], 20, 0)
                            score += 1

                rem = -1
                for i in enemy_ammo_list:
                    rem += 1
                    i[1] += 10
                    screen.blit(ammo_enemy, [i[0], i[1]])
                    if i[1] >= 590:
                        enemy_ammo_list.pop(rem)

                remove = -1
                for l in enemy_ammo_list:
                    q = crash.intersect_class(ship, l[0], l[1], l[2], l[3])
                    remove += 1
                    if q:
                        armor -= 1
                        pygame.draw.circle(screen, [255, 0, 0], [l[0], l[1]], 30, 0)
                        enemy_ammo_list.pop(remove)
                for i in ammo_list:
                    i.shoot()
                if spell_used:
                    spell_time_r -= 1
                if spell_time_r <= 0:
                    spell_used = False
                    spell_ready = False
                    used = False
                    spell_time_r = spell_time
                    spell_reload = 500
                    move = True

                else:
                    spell_reload -= 1
                    if spell_reload <= 0:
                        spell_ready = True






################################################################################################################
            for i in enemy_ammo_list:
                screen.blit(ammo_enemy, [i[0], i[1]])
            for l in ammo_list:
                l.draw()
            if up:
                if spell_ready:
                    used = True

            if used:
                if spell_ready:
                    if spell == "shield":
                        spell_used = True
                        pygame.draw.rect(screen, [255, 0, 0], [ship.x - 20, 570, 80, 20])
                        ind = -1
                        for l in enemy_ammo_list:
                            ind += 1
                            cr = crash.intersect(l[0], ship.x - 20, l[1], 570, l[2], l[3], 80, 20)
                            if cr:
                                pygame.draw.circle(screen, [0, 0, 255], [l[0], l[1]], 20)
                                enemy_ammo_list.pop(ind)
                        ind = -1
                        for l in enemies:
                            ind += 1
                            cr = crash.intersect(l.x, ship.x - 20, l.y, 570, l.x_size, l.y_size, 80, 20)
                            if cr:
                                pygame.draw.circle(screen, [0, 0, 255], [l.x, l.y], 20)
                                enemies.pop(ind)



            if spell_ready:
                if col_1 > 10:
                    col_1 -= 10
                if col_1 <= 10:
                    col_1 = 255
                if col_2 > 10:
                    col_2 -= 10
                if col_2 >= 10:
                    col_2 = 255
                if col_3 > 10:
                    col_3 -= 10
                if col_3 <= 10:
                    col_3 = 255
                pygame.draw.rect(screen, [col_1, col_2, col_3], [10, 80, 20, spell_time_r])
                pygame.draw.rect(screen, [col_1, col_2, col_3], [10, 80, 20, spell_time], 1)
                writer.write("ready", screen, 35, 80, color=[col2, col2, col2])

                col2 += col_change2
                if col2 >= 255:
                    col_change2 = -col_change2
                    col2 = 255
                if col2 <= 0:
                    col_change2 = -col_change2
                    col2 = 0

            elif not spell_ready:
                pygame.draw.rect(screen, [0, 0, 0], [10, 80, 20, spell_reload / 5])
                pygame.draw.rect(screen, [0, 0, 0], [10, 80, 20, 500 / 5], 1)
                writer.write("reloading", screen, 35, 80, color=[col3, col3, col3])

                col3 += col_change3
                if col3 >= 255:
                    col_change3 = -col_change3
                    col3 = 255
                if col3 <= 0:
                    col_change3 = -col_change3
                    col3 = 0
            pygame.draw.rect(screen, [0, 0, 255], [460, 100, 20, portal_reload], 1)
            pygame.draw.rect(screen, [0, 0, 255, ], [460, 100, 20, portal])
            writer.write("portal:", screen, 440, 50, color=[0, 0, 255])

            if portal > 0:
                if col4 > 10:
                    col4 -= 10
                if col4 <= 10:
                    col4 = 255
                if col5 > 10:
                    col5 -= 10
                if col5 >= 10:
                    col5 = 255
                if col6 > 10:
                    col6 -= 10
                if col6 <= 10:
                    col6 = 255
                portal_2 = portal / 30
                writer.write("reloading", screen, 415, 350, size=16, color=[0, 0, 255])
                writer.write("left: %i" % portal_2, screen=screen, x=415, y=370, color=[0, 0, 255])
            else:
                if col4 > 10:
                    col4 -= 10
                if col4 <= 10:
                    col4 = 255
                if col5 > 10:
                    col5 -= 10
                if col5 >= 10:
                    col5 = 255
                if col6 > 10:
                    col6 -= 10
                if col6 <= 10:
                    col6 = 255
                writer.write("ready", screen, 450, 350, color=[col4, col5, col6])
                writer.write("portal:", screen, 440, 50, color=[col4, col5, col6])
                pygame.draw.rect(screen, [col4, col5, col6], [460, 100, 20, 200], 1)
                pygame.draw.rect(screen, [col4, col5, col6], [460, 100, 20, 200])
            if left:
                ship.fly_left()
            if right:
                ship.fly_right()
            ship.draw()

            if ship.ammo <= 0:
                writer.write("reloading", screen, 200, 300, color=[col, col, col])
                col += col_change
                if col >= 255:
                    col_change = -col_change
                    col = 255
                if col <= 0:
                    col_change = -col_change
                    col = 0
                reloading += 1
            if reloading == 40:
                ship.ammo = ammo
                reloading = 0
            writer.write(txt="health: %i" % float(health), screen=screen, x=20, y=20)
            writer.write(txt="armor: %i" % float(armor), screen=screen, x=20, y=40)
            writer.write(txt="ammo: %i" % ship.ammo, screen=screen, x=20, y=60)

            for i in enemies:
                i.draw()

            time = pygame_init.loop_end(t=True, time=time, delay=delay)
            tick += 1

            if health <= 0 or armor <= 0:

                choice = easygui.buttonbox(
                    "Game over. Your score was: " + str(score * 2) + ". Would you lake to play again?",
                    ["play again", "exit to main menu"])
                if choice == "play again":
                    return True
                else:
                    return False



    game_2 = True
    while game_2:
        game_2 = game(rocket, delay)
    pygame.display.quit()
    pygame.mixer.music.stop()
