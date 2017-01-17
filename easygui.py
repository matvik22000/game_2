
import sys, pygame
from PyQt4 import QtGui, QtCore


def buttonbox(question, choises, title = "question"):
    if len(choises) == 1:
        choise1 = choises[0]
        choise2 = ""
        choise3 = ""
    if len(choises) == 2:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = ""
    if len(choises) == 3:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = choises[2]

    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)
        def main(self):
            reply = QtGui.QMessageBox.question  (self, title, question, choise1, choise2, choise3 )
            if reply == 0:
                return choise1
            if reply == 1:
                return choise2
            if reply == 2:
                return choise3

    qb = MessageBox()
    q = qb.main()

    return q


def buttonbox_warning(question, choises, title="warning"):
    if len(choises) == 1:
        choise1 = choises[0]
        choise2 = ""
        choise3 = ""
    if len(choises) == 2:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = ""
    if len(choises) == 3:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = choises[2]

    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)

        def main(self):
            reply = QtGui.QMessageBox.warning(self, title, question, choise1, choise2, choise3)
            if reply == 0:
                return choise1
            if reply == 1:
                return choise2
            if reply == 2:
                return choise3

    qb = MessageBox()
    q = qb.main()

    return q


def buttonbox_critical(question, choises, title="critical"):
    if len(choises) == 1:
        choise1 = choises[0]
        choise2 = ""
        choise3 = ""
    if len(choises) == 2:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = ""
    if len(choises) == 3:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = choises[2]

    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)

        def main(self):
            reply = QtGui.QMessageBox.critical(self, title, question, choise1, choise2, choise3)
            if reply == 0:
                return choise1
            if reply == 1:
                return choise2
            if reply == 2:
                return choise3

    qb = MessageBox()
    q = qb.main()

    return q


def msgbox(text, title = "message"):
    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)

        def main(self):
            QtGui.QMessageBox.information(self, title, text )

    qb = MessageBox()
    qb.main()


def critical(text, title = "critical"):
    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)

        def main(self):
            QtGui.QMessageBox.critical(self, title, text)

    qb = MessageBox()
    qb.main()


def waring(text, title = "warning"):
    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)

        def main(self):
            QtGui.QMessageBox.warning(self, title, text)

    qb = MessageBox()
    qb.main()

def buttonbox_not_PyQt(question, choises, title = "question"):
    if len(choises) == 1:
        choise1 = choises[0]
        choise2 = ""
        choise3 = ""
    if len(choises) == 2:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = ""
    if len(choises) == 3:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = choises[2]

    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)
        def main(self):
            reply = QtGui.QMessageBox.question(self, title, question, choise1, choise2, choise3 )
            if reply == 0:
                return choise1
            if reply == 1:
                return choise2
            if reply == 2:
                return choise3

    app = QtGui.QApplication(sys.argv)
    qb = MessageBox()
    q = qb.main()
    app.exec_()
    return q
def quit_question(choices = ["exit", "cancel"]):
    q = buttonbox_warning("Are tou sure to quit?", choices)
    return q
def del_question(file_name):
    choice = buttonbox_warning("Are sure you want to remove this file?", ["delete", "cancel"], title="are you sure?")
    if choice == "delete":
        t = open(file_name, "w")
        del(t)
        msgbox("delete was successful!", "file deleted")


def inf_question(question, choises, title = "question"):
    if len(choises) == 1:
        choise1 = choises[0]
        choise2 = ""
        choise3 = ""
    if len(choises) == 2:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = ""
    if len(choises) == 3:
        choise1 = choises[0]
        choise2 = choises[1]
        choise3 = choises[2]

    class MessageBox(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QDialog.__init__(self, parent)
        def main(self):
            reply = QtGui.QMessageBox.information(self, title, question, choise1, choise2, choise3 )
            if reply == 0:
                return choise1
            if reply == 1:
                return choise2
            if reply == 2:
                return choise3

    qb = MessageBox()
    q = qb.main()

    return q

def again():
    choice = buttonbox_not_PyQt("Game over. Would you lake to play again?", ["play again", "exit to main menu"])
    if choice == "play again":
        return True
    else:
        return False

def exit(button,  orient, size = 700):
    x = 50
    a = 0
    while a <= size / 10:
        button.move(10, 0)
        pygame.time.delay(x)
        x -= 1
        a += 1

    
    
    
    
    
