import sys, traffic_lighter, easygui
from PyQt4 import QtGui, uic
form_class = uic.loadUiType("main_menu.ui")[0]
inf = uic.loadUiType("information.ui")[0]

class Information(QtGui.QDialog, inf):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
    def button_clicked(self):
        ap.hide()
class MainMenu(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.play.clicked.connect(self.button_clicked)
        self.exit.clicked.connect(self.button_clicked2)
        self.how_to_play.clicked.connect(self.button_clicked3)
        self.information_2.clicked.connect(self.button_clicked4)
        self.best_score.clicked.connect(self.button_clicked5)
    def closeEvent(self, event):
        choice = easygui.quit_question()
        if choice == "exit":
            event.accept()
            global reset
            reset = False
        else:
            event.ignore()
    def button_clicked(self):
        traffic_lighter.game()
        app.exit()
        global reset
        reset = True
    def button_clicked2(self):
        choice = easygui.quit_question()
        if choice == "exit":
            app.exit()
            global reset
            reset = False

    def button_clicked3(self):
        easygui.msgbox("In this game you control a traffic light. Press space button to change colors in traffic light and not let a crash. Good luck!", title= "How to play")
    def button_clicked4(self):
        ap.show()
    def button_clicked5(self):
        try:
            w = open("score", "r")
            e = w.read()
            w.close()
            if e == "":
                easygui.critical("You didn't play yet", "oops...")
            else:
                choice = easygui.inf_question("Your last score was " + str(e), title= "you score" ,choises= ["ok", "delete"])
                if choice == "ok":
                    easygui.waring("If you play again this score will be lost!")
                else:
                    easygui.del_question("score")

        except IOError:
            easygui.critical("I think you didn't play yet, file with your score wasn't found", "oops...")

reset = False
app = QtGui.QApplication(sys.argv)
menu = MainMenu()
menu.show()
ap = Information()
app.exec_()
while reset:
    menu = MainMenu()
    menu.show()
    app.exec_()
