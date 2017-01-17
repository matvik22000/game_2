import pygame, easygui, sys
from PyQt4 import QtGui, QtCore
def get_fonts():
    a = pygame.font.get_fonts()
    return a
def write(txt, screen, x, y, size = 16, color = [0, 0, 0],  font = "freesansbold.ttf"):
    s_str = txt
    s_font = pygame.font.Font(font, size)
    s_surf = s_font.render(s_str, 1, color)
    screen.blit(s_surf, [x, y])
def str2bool(txt):
    if txt == "True":
        return True
    else:
        return False


def str2bool_file(file):
    file_name = open(file, "r")
    text = file_name.read()
    file_name.close()
    result = str2bool(text)
    return result

def write_file(file_name, txt):
    open1 = open(file_name, "w")
    open1.write(txt)
    open1.close()

def read_file(file_name):
    open1 = open(file_name)
    txt = open1.read()
    open1.close()
    return  txt

def fill_file_int(file_name):
    ro = open(file_name)
    qe = ro.read()
    ro.close()
    if qe == "":
        to = open(file_name, "w")
        to.write("0")
        to.close()

def file_availability(file_name, txt = ""):
    try:
        file = open(file_name)
    except IOError:
        f = open(file_name, "w")
        f.write(txt)
        f.close()
    else:
        file.close()

def buy(file_oblect, cost, txt,  file_money = "score_shooter", dop_file = "rocket"):
    txt_1 = read_file(file_oblect)
    if str2bool(txt_1):
        easygui.msgbox("You already have this module")

    else:
        score_1 = read_file("score_shooter")
        if int(score_1) >= 1000:
            write_file(file_oblect, "True")
            write_file(file_money, str(int(score_1) - cost))
            easygui.msgbox("the buy was successful!")
        else:
            easygui.critical("not enough money!")


def restart(app):
    reset = True
    app.exit()
    return reset




