import sys, pygame
from PyQt4 import QtGui, QtCore
pygame.init()
class Test(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("test")
        self.but = QtGui.QPushButton("test", self)
        self.connect(self.but, QtCore.SIGNAL("clicked()"), self.np_f)
    def np_f(self):
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)
        self.but.move(self.but.x() + 10, 0)
        pygame.time.delay(30)

app = QtGui.QApplication(sys.argv)
test = Test()
test.show()
app.exec_()

