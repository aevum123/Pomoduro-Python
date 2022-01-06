import sys                        # needed for the sys.argv passed to QApplication below (command line arguments)
import time
import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog, QMainWindow
from PyQt5.QtGui import *
from PyQt5.uic import loadUi      # special library to load .ui file directly

class MyForm(QMainWindow):
    # constructor for this MyForm class 
    def __init__(self):
        super().__init__()   # calls the constructor of the QDialog class that is inherited

        self.ui = loadUi('pomoduro.ui', self)
        
        self.my_qtimer = None
        self.start = False
        self.count = 0

        self.ui.actionColor.triggered.connect(self.menuBackgroundMethod)
        self.ui.actionExit.triggered.connect(self.exitMethod)
        self.ui.pushButton5.clicked.connect(self.fiveMinutes)
        self.ui.pushButton10.clicked.connect(self.tenMinutes)
        self.ui.pushButton15.clicked.connect(self.fifteenMinutes)

        self.show()   # this line shows the .ui file after all the Widget's signals are connected.

    def menuBackgroundMethod(self):
        intial_color = self.ui.menubar.palette().color(QPalette.Foreground)
        color = QColorDialog.getColor(intial_color, self, "Pick a color!")
        color1 = QColor("Red")

        if color.isValid():
            pal = self.palette()
            pal.setColor(self.ui.backgroundRole(), color)
            self.setPalette(pal)
    
    def fiveMinutes(self):
        #if self.start = True
            #set false?
            self.count = 300
            self.timer_start()
            self.showtime()
            
        #^put this in a method to be called by all buttons when it works
    
    def tenMinutes(self):
        self.count = 600
        self.timer_start()
        self.showtime()
    
    def fifteenMinutes(self):
        pass


    def timer_start(self):
        self.start = True
        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_action)
        self.my_qtimer.start(1000)
        
    def showtime(self):
        if self.start:
            self.count -= 1
            
        if self.count == 0:
            self.start = False
            self.labelprint.setText("Complete")
    
    def start_action(self):
        self.start = True
        
        if self.count == 0:
            self.start = False
    
    def timer_action(self):
        self.labelprint.setText(str(datetime.timedelta(seconds=self.count)))
        self.count -= 1
        
    def exitMethod(self):
        QApplication.instance().quit()


if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    # w.show()            # not needed because constructor does .show()
    sys.exit(app.exec_())  # note - sys.exit causes traceback in some editors if it does in yours just use app.exec()