"""

import sys,writer
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
        self.motor_t1 = QtGui.QLabel("motor", self)
        self.motor_t1.move(120, 230)
        self.motor_t2 = QtGui.QLabel("cost - 700", self)
        self.motor_t2.move(110, 310)
        self.line.move(190, 270)
        self.line_2 = QtGui.QLabel("_____________", self)
        self.line_2.move(200, 130)
        self.armor_t1 = QtGui.QLabel("armor", self)
        self.armor_t1.move(120, 80)
        self.armor_t2 = QtGui.QLabel("cost - 500", self)
        self.armor_t2.move(120, 180)
        self.label_armor.move(100, 100)
        self.label_s.move(200, -20)
        self.label_ammo.move(500, 80)
        self.line_3 = QtGui.QLabel("________________________", self)
        self.line_3.move(370, 100)
        self.ammo_t1 = QtGui.QLabel("ammo", self)
        self.ammo_t1.move(530, 65)
        self.ammo_t2 = QtGui.QLabel("cost - 600", self)
        self.ammo_t2.move(525, 160)
        self.label_motor.move(100, 250)
        self.label_ammo.setPixmap(QtGui.QPixmap("ammo_pyqt.png"))
        self.label_armor.setPixmap(QtGui.QPixmap("armor.png"))
        self.label_motor.setPixmap(QtGui.QPixmap("motor.png"))
        self.label_s.setPixmap(QtGui.QPixmap("sp_s_1.png"))
        self.button_1 = QtGui.QPushButton("back", self)
        self.button_1.setGeometry(0, 0,  100, 40)
        self.buy_1 = QtGui.QPushButton("buy", self)
        self.buy_1.setGeometry(110, 195, 80, 20)
        self.buy_2 = QtGui.QPushButton("buy", self)
        self.buy_2.setGeometry(110, 325, 80, 20)
        self.buy_3 = QtGui.QPushButton("buy", self)
        self.buy_3.setGeometry(510, 180, 80, 20)
        self.np = QtGui.QPushButton("next page", self)
        self.np.setGeometry(600, 0, 100, 40)
        self.connect(self.np, QtCore.SIGNAL("clicked()"), self.np_f)
        self.connect(self.buy_1, QtCore.SIGNAL("clicked()"), self.buy1)
        self.connect(self.buy_2, QtCore.SIGNAL("clicked()"), self.buy2)
        self.connect(self.buy_3, QtCore.SIGNAL("clicked()"), self.buy3)
        self.connect(self.button_1, QtCore.SIGNAL("clicked()"), self.close)
    def np_f(self):

    def buy1(self):
        writer.buy(file_oblect="hp", cost=2000, txt = "True")
    def buy2(self):
        writer.buy(file_oblect="portal", cost=1000, txt="True")
    def buy3(self):
        writer.buy(file_oblect="reghp", cost=6000, txt="True")
    def buy4(self):
        writer.buy(file_oblect="regarmor", cost=5000, txt="True")



app = QtGui.QApplication(sys.argv)
test = Label()
test.show()
app.exec_()
"""