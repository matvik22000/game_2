import easygui, sys, shoter, writer, music, pygame
from PyQt4 import QtGui, uic, QtCore
form_class = uic.loadUiType("shoter.ui")[0]
inf = uic.loadUiType("information.ui")[0]
roc_shop = uic.loadUiType("rocket_shop.ui")[0]
module_shop_1 = uic.loadUiType("modules.ui")[0]
reset = True
writer.file_availability("rocket_2", "False")
writer.file_availability("rocket_3", "False")
writer.file_availability("rocket", "rocket")
writer.file_availability("rocket_4", "False")
writer.file_availability("rocket_5", "False")
writer.file_availability("ammo", "False")
writer.file_availability("motor", "False")
writer.file_availability("armor", "False")
roc = uic.loadUiType("new_rockets.ui")[0]
writer.file_availability("score_shooter", "0")
mod = uic.loadUiType("modules_2.ui")[0]
game_speed = 1
def music_change():
    global track_num
    if track_num == 0:
        return "DLYa_IGRY_-Fonovaya_muzyka.mp3"
    if track_num == 1:
        return "Counter-strike_1.6-Zak_Belica_(glavnaya_tema_-_fonovaya_muzyka_v_nachale_igry).mp3"
    if track_num == 2:
        return "Counter-Strike-_Condition_Zero-Zak_Belica_(glavnaya_tema_-_fonovaya_muzyka_v_nachale_igry).mp3"
track_num = 0

import sys
from PyQt4 import QtGui, QtCore


class Label(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 50, 700, 600)
        self.setWindowTitle("modules  shop")
        self.label_s = QtGui.QLabel(self)
        self.label_ammo = QtGui.QLabel(self)
        self.label_armor = QtGui.QLabel(self)
        self.label_motor = QtGui.QLabel(self)
        self.line = QtGui.QLabel("_______________________", self)
        self.motor_t1 = QtGui.QLabel("engine - give +5 speed", self)
        self.motor_t1.move(70, 230)
        self.motor_t2 = QtGui.QLabel("cost - 700", self)
        self.motor_t2.move(80, 310)
        self.line.move(160, 270)
        self.line_2 = QtGui.QLabel("_____________", self)
        self.line_2.move(200, 130)
        self.armor_t1 = QtGui.QLabel("armor - give +5 armor", self)
        self.armor_t1.move(120, 80)
        self.armor_t2 = QtGui.QLabel("cost - 500", self)
        self.armor_t2.move(120, 180)
        self.label_armor.move(100, 100)
        self.label_s.move(200, -20)
        self.label_s.setPixmap(QtGui.QPixmap("sp_s_1.png"))

        txt = writer.read_file("rocket")
        if txt == "rocket":
            self.label_s.move(200, -20)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_1.png"))
        if txt == "rocket_4":
            self.label_s.move(200, 50)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_4.png"))
        if txt == "rocket_2":
            self.label_s.move(50, 0)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_2.png"))
        if txt == "rocket_5":
            self.label_s.move(200, 100)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_5.png"))
        if txt == "rocket_3":
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_3.png"))
            self.label_s.move(200, 100)
        self.label_ammo.move(500, 80)
        self.line_3 = QtGui.QLabel("________________________", self)
        self.line_3.move(370, 100)
        self.ammo_t1 = QtGui.QLabel("ammo - give +5 ammo", self)
        self.ammo_t1.move(530, 65)
        self.ammo_t2 = QtGui.QLabel("cost - 600", self)
        self.ammo_t2.move(525, 160)
        self.label_motor.move(60, 250)
        self.label_helth = QtGui.QLabel(self)
        self.label_helth.setPixmap(QtGui.QPixmap("health.png"))
        self.label_portal = QtGui.QLabel(self)
        self.label_portal.setPixmap(QtGui.QPixmap("portal.png"))
        self.label_portal.move(500, 250)
        self.portal_t1 = QtGui.QLabel("portal - +50 cast range, -2s reload time", self)
        self.portal_t1.move(510, 230)
        self.portal_t2 = QtGui.QLabel("cost - 2000", self)
        self.portal_t2.move(510, 300)
        self.buy_5 = QtGui.QPushButton("buy", self)
        self.label_helth.move(500, 360)
        self.health_t1 = QtGui.QLabel("medicine chest - give +5 health", self)
        self.health_t1.move(510, 345)
        self.label_t2 = QtGui.QLabel("cost - 2000", self)
        self.label_t2.move(510, 415)
        self.label_ammo.setPixmap(QtGui.QPixmap("ammo_pyqt.png"))
        self.label_armor.setPixmap(QtGui.QPixmap("armor.png"))
        self.label_motor.setPixmap(QtGui.QPixmap("motor.png"))
        self.line_4 = QtGui.QLabel("__________________", self)
        self.line_4.move(400, 270)
        self.line_4 = QtGui.QLabel("______________________", self)
        self.line_4.move(380, 390)
        self.button_1 = QtGui.QPushButton("back", self)
        self.button_1.setGeometry(0, 0, 100, 40)
        self.buy_1 = QtGui.QPushButton("buy", self)
        self.buy_1.setGeometry(110, 195, 80, 20)
        self.buy_1.setDisabled(writer.str2bool_file("armor"))
        self.buy_2 = QtGui.QPushButton("buy", self)
        self.buy_2.setGeometry(70, 325, 80, 20)
        self.buy_2.setDisabled(writer.str2bool_file("motor"))
        self.buy_3 = QtGui.QPushButton("buy", self)
        self.buy_3.setGeometry(510, 180, 80, 20)
        self.buy_3.setDisabled(writer.str2bool_file("ammo"))
        self.buy_4 = QtGui.QPushButton("buy", self)
        self.buy_4.setDisabled(writer.str2bool_file("portal"))
        self.buy_4.setGeometry(520, 430, 80, 20)
        self.buy_5.setGeometry(510, 320, 80, 20)
        self.buy_5.setDisabled(writer.str2bool_file("hp"))
        self.connect(self.buy_1, QtCore.SIGNAL("clicked()"), self.buy1)
        self.connect(self.buy_2, QtCore.SIGNAL("clicked()"), self.buy2)
        self.connect(self.buy_3, QtCore.SIGNAL("clicked()"), self.buy3)
        self.connect(self.button_1, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.buy_4, QtCore.SIGNAL("clicked()"), self.buy4)
        self.connect(self.buy_5, QtCore.SIGNAL("clicked()"), self.buy5)

    def show(self):
        txt = writer.read_file("rocket")
        if txt == "rocket":
            self.label_s.move(0 - self.label_s.x(), 0 - self.label_s.y())
            self.label_s.move(200, -20)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_1.png"))
        if txt == "rocket_4":
            self.label_s.move(0 - self.label_s.x(), 0 - self.label_s.y())
            self.label_s.move(200, 50)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_4.png"))
        if txt == "rocket_2":
            self.label_s.move(0 - self.label_s.x(), 0 - self.label_s.y())
            self.label_s.move(50, 0)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_2.png"))
        if txt == "rocket_5":
            self.label_s.move(0 - self.label_s.x(), 0 - self.label_s.y())
            self.label_s.move(200, 100)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_5.png"))
        if txt == "rocket_3":
            self.label_s.move(0 - self.label_s.x(), 0 - self.label_s.y())
            self.label_s.move(200, 100)
            self.label_s.setPixmap(QtGui.QPixmap("sp_s_3.png"))
        self.buy_5.setDisabled(writer.str2bool_file("portal"))
        self.buy_4.setDisabled(writer.str2bool_file("hp"))
        self.buy_1.setDisabled(writer.str2bool_file("armor"))
        self.buy_2.setDisabled(writer.str2bool_file("motor"))
        self.buy_3.setDisabled(writer.str2bool_file("ammo"))
        QtGui.QWidget.show(self)
    def buy5(self):
        writer.buy(file_oblect="portal", cost=2000, txt="True")
        self.buy_5.setDisabled(writer.str2bool_file("portal"))
    def buy4(self):
        writer.buy(file_oblect="hp", cost=2000, txt="True")
        self.buy_4.setDisabled(writer.str2bool_file("hp"))


    def buy1(self):
        writer.buy(file_oblect="armor", cost=2000, txt="True")
        self.buy_1.setDisabled(writer.str2bool_file("armor"))

    def buy2(self):
        writer.buy(file_oblect="motor", cost=1000, txt="True")
        self.buy_2.setDisabled(writer.str2bool_file("motor"))

    def buy3(self):
        writer.buy(file_oblect="ammo", cost=6000, txt="True")
        self.buy_3.setDisabled(writer.str2bool_file("ammo"))


class Modules_2(QtGui.QMainWindow, mod):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.buy_3.setDisabled(writer.str2bool_file("reghp"))
        self.buy_4.setDisabled(writer.str2bool_file("regarmor"))
        self.buy_3.clicked.connect(self.buy3)
        self.buy_4.clicked.connect(self.buy4)
        self.back.clicked.connect(self.back_f)
    def buy3(self):
        self.buy_3.setDisabled(writer.str2bool_file("reghp"))
        writer.buy(file_oblect="reghp", cost=6000, txt="True")
    def buy4(self):
        writer.buy(file_oblect="regarmor", cost=5000, txt="True")
        self.buy_4.setDisabled(writer.str2bool_file("regarmor"))
    def back_f(self):
        shop_modules.show()
        self.hide()
class Volume(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(800, 200, 150, 100)
        self.setWindowTitle("settings")
        self.vol = 0.5
        self.sp_box = QtGui.QSpinBox(self)
        self.txt = QtGui.QLabel("game speed", self)
        self.txt_2 = QtGui.QLabel("volume:", self)
        self.txt.move(70, 0)
        self.sp_box.move(40, 0)
        self.sp_box.setMinimum(1)
        self.sp_box.setMaximum(3)
        self.txt_3 = QtGui.QLabel("music:", self)
        self.txt_3.move(100, 30)
        self.slider = QtGui.QSlider(self)
        self.slider.move(0, 15)
        self.pos = QtGui.QSlider.sliderPosition(self.slider)
        self.next_button = QtGui.QPushButton("next track", self)
        self.previous_button = QtGui.QPushButton("previous track", self)
        self.next_button.setGeometry(50, 70, 100, 20)
        self.previous_button.setGeometry(50, 50, 100, 20)
        self.slider.setSliderPosition(50)
        self.connect(self.slider, QtCore.SIGNAL("sliderReleased()"), self.console)
        self.connect(self.previous_button, QtCore.SIGNAL("clicked()"), self.previous_track)
        self.connect(self.next_button, QtCore.SIGNAL("clicked()"), self.next_track)
        self.sp_box.valueChanged.connect(self.g_s)
        cb = QtGui.QCheckBox("sounds", self)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        cb.move(25, 30)
    def g_s(self):
        global game_speed
        game_speed = self.sp_box.value()
    def changeTitle(self, state):
         if state == QtCore.Qt.Checked:
              self.console()
         else:
            pygame.mixer.music.set_volume(0)

    def console(self):
        self.vol = self.slider.sliderPosition()
        pygame.mixer.music.set_volume(self.vol / float(100))
    def next_track(self):
        global track_num
        track_num += 1
        if track_num > 2:
            track_num = 0
        a = music_change()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play(-1)

    def previous_track(self):
        global track_num
        track_num -= 1
        if track_num < 0:
            track_num = 2
        a = music_change()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play(-1)
class Console(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(700, 150, 280, 40)
        self.setWindowTitle("console")
        self.button_1 = QtGui.QPushButton("console", self)
        self.button_2 = QtGui.QPushButton("command list", self)
        self.button_3 = QtGui.QPushButton("exit", self)
        self.button_1.move(20, 10)
        self.button_2.move(100, 10)
        self.button_3.move(180, 10)
        self.connect(self.button_1, QtCore.SIGNAL("clicked()"), self.console)
        self.connect(self.button_2, QtCore.SIGNAL("clicked()"), self.command_list)
        self.connect(self.button_3, QtCore.SIGNAL("clicked()"), self.close)
    def close(self):

        QtGui.QWidget.close(self)

    def console(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input command', "Input command.", )
        if ok:
            if text == "matvik22000":
                text2, ok = QtGui.QInputDialog.getText(self, 'Input number', 'input number')
                if ok:
                    writer.write_file("score_shooter", text2)
            if text == "m03":
                writer.write_file("rocket_2", "True")
                writer.write_file("rocket_2", "True")
                writer.write_file("rocket_3", "True")
                writer.write_file("rocket_4", "True")
                writer.write_file("rocket_5", "True")
                easygui.msgbox("write code")
            if text == "clear":
                text3, ok = QtGui.QInputDialog.getText(self, 'clear', "input command")
                if ok:
                    if text3 == "rockets":
                        writer.write_file("rocket_2", "False")
                        writer.write_file("rocket_3", "False")
                        writer.write_file("rocket_4", "False")
                        writer.write_file("rocket_5", "False")
                        writer.write_file("rocket", "rocket")
                    if text3 == "money":
                        writer.write_file("score_shooter", "0")
                    if text3 == "all":
                        writer.write_file("rocket_2", "False")
                        writer.write_file("rocket_3", "False")
                        writer.write_file("rocket", "rocket")
                        writer.write_file("rocket_4", "False")
                        writer.write_file("rocket_5", "False")
                        writer.write_file("score_shooter", "0")
                        writer.write_file("motor", "False")
                        writer.write_file("armor", "False")
                        writer.write_file("ammo", "False")
                        writer.write_file("hp", "False")
                        writer.write_file("portal", "False")
                        writer.write_file("reghp", "False")
                        writer.write_file("regarmor", "False")
                    if text3 == "modules":
                        writer.write_file("motor", "False")
                        writer.write_file("armor", "False")
                        writer.write_file("ammo", "False")
                        writer.write_file("hp", "False")
                        writer.write_file("portal", "False")
                        writer.write_file("reghp", "False")
                        writer.write_file("regarmor", "False")
                    if text3 != "rockets" and text3 != "money" and text3 != "all" and text3 != "modules" :
                        easygui.critical("wrong command")

        if text != "matvik22000" and text != "clear" and text != "m03":
            easygui.critical("wrong command")

    def command_list(self):
        easygui.msgbox(
            "Use 'clear' command to delete information about score and rockets. If you use clear command, write 'rockets' to delete rockets, 'money' to delete score, 'modules' to delete all modules, 'all' to delete all. ")


class MainMenu(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.play.clicked.connect(self.button_clicked)
        self.exit.clicked.connect(self.button_clicked2)
        self.how.clicked.connect(self.button_clicked3)
        self.information.clicked.connect(self.button_clicked4)
        self.score.clicked.connect(self.button_clicked5)
        self.shop.clicked.connect(self.button_clicked6)
        self.pushButton.clicked.connect(self.showDialog)
        self.rockets.clicked.connect(self.rocket)
        self.pushButton_2.clicked.connect(self.volume)
        self.tutorial.clicked.connect(self.tutorial_f)
    def tutorial_f(self):
        shoter.tutorial("rocket", 30)
    def volume(self):
        test.show()

    def rocket(self):
        easygui.msgbox("You have standart rocket")
        txt = writer.read_file("rocket_2")
        if writer.str2bool(txt):
            easygui.msgbox("You have advanced rocket.")
        txt2 = writer.read_file("rocket_3")
        if writer.str2bool(txt2):
            easygui.msgbox("You have the best rocket.")
        txt3 = writer.read_file("rocket_4")
        if writer.str2bool(txt3):
            easygui.msgbox("You have RAB rocket.")
        txt4 = writer.read_file("rocket_5")
        if writer.str2bool(txt4):
            easygui.msgbox('You have exclusive rocket')
    def showDialog(self):
        console_show.show()

    def button_clicked(self):
        rocket = writer.read_file("rocket")
        if game_speed == 1:
            shoter.shooter(rocket, 30)
        if game_speed == 2:
            shoter.shooter(rocket, 15)
        if game_speed == 3:
            shoter.shooter(rocket, 10)
        global reset
        reset = True
        app.exit()


    def button_clicked2(self):
        choice = easygui.quit_question()
        if choice == "exit":
            global reset
            reset = False
            app.exit()
    def button_clicked3(self):
        easygui.msgbox("In this game you should control a spaceship. dodge enemy bullets and don't let enemy spaceships get to your spaceship. Use arrows to control rocket a and d buttons to teleport and key up to use spell and press space to shoot. Good luck.", "how to play")

    def button_clicked4(self):
        ap.show()
    def button_clicked5(self):
        r = open("score_shooter")
        u = r.read()
        r.close()
        easygui.msgbox("your score - " + u + " coin(s)")
    def button_clicked6(self):
        shop.show()

    def closeEvent(self, event):
        choice = easygui.quit_question()
        if choice == "exit":
            event.accept()
            global reset
            reset = False
        else:
            event.ignore()
class Information(QtGui.QDialog, inf):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        ap.hide()
class RocketShop(QtGui.QDialog, roc_shop):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.button_clicked2)
        self.pushButton_3.clicked.connect(self.button_clicked3)
        self.back.clicked.connect(self.button_clicked4)
        self.rocket.clicked.connect(self.new_rockets)
        self.pushButton_4.clicked.connect(self.button_clicked5)
        self.modules.clicked.connect(self.modul)
    def modul(self):
        shop_modules.show()
    def new_rockets(self):
        rocket.show()
    def button_clicked5(self):
        txt_1 = writer.read_file("rocket_4")
        if writer.str2bool(txt_1):
            easygui.msgbox("rocket used.")
            writer.write_file("rocket", "rocket_4")
        else:
            score_1 = writer.read_file("score_shooter")
            if int(score_1) >=  1000:
                writer.write_file("rocket_4", "True")
                writer.write_file("score_shooter", str(int(score_1) - 1000))
                easygui.msgbox("the buy was successful!")
            else:
                easygui.critical("not enough money!")


    def button_clicked(self):
        writer.fill_file_int("score_shooter")
        writer.write_file("rocket", "rocket")
        easygui.msgbox("rocket used")
    def button_clicked2(self):
        writer.fill_file_int("score_shooter")
        txt1 = writer.read_file("rocket_2")

        if not writer.str2bool(txt1):
            txt2 = writer.read_file("score_shooter")
            if int(txt2) >= 300:
                writer.write_file("score_shooter", str(int(txt2) - 300))
                writer.write_file("rocket_2", "True")
                easygui.msgbox("the buy was successful!","the buy was successful")
            else:
                easygui.critical("not enough money!", "not enough money")

        else:
            writer.write_file("rocket", "rocket_2")
            easygui.msgbox("rocket used.", "rocket used")
    def button_clicked3(self):
        writer.fill_file_int("score_shooter")
        txt1 = writer.read_file("rocket_3")

        if not writer.str2bool(txt1):
            txt2 = writer.read_file("score_shooter")
            if int(txt2) >= 600:
                writer.write_file("score_shooter", str(int(txt2) - 600))
                writer.write_file("rocket_3", "True")
                easygui.msgbox("the buy was successful!", "the buy was successful")
            else:
                easygui.critical("not enough money!", "not enough money")
        else:
            writer.write_file("rocket", "rocket_3")
            easygui.msgbox("rocket used.", "rocket used")
    def button_clicked4(self):
        shop.hide()
class NewRockets(QtGui.QDialog, roc):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.back.clicked.connect(self.back_e)
        self.input_button.clicked.connect(self.input)
        self.pushButton.clicked.connect(self.use)
    def use(self):
        txt = writer.read_file("rocket_5")
        if writer.str2bool(txt):
            writer.write_file("rocket", "rocket_5")
            easygui.msgbox("Rocket used")
        else:
            easygui.critical("You haven't got this rocket. Input secret code to get it.")
    def back_e(self):
        rocket.hide()
    def input(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input code', 'input code')
        if ok:
            if text == "parfen2011":
                writer.write_file("rocket_5", "True")
                easygui.msgbox("right code", "rocket used")
            else:
                easygui.critical("wrong code")




app = QtGui.QApplication(sys.argv)
console_show = Console()
shop = RocketShop()
menu = MainMenu()
ap = Information()
rocket = NewRockets()
shop_modules = Label()
test = Volume()
mod_shop_2 = Modules_2()
while reset:
    music.play("DLYa_IGRY_-Fonovaya_muzyka.mp3")
    pygame.mixer.music.set_volume(0.5)
    menu.show()
    app.exec_()

