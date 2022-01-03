import sys                        # needed for the sys.argv passed to QApplication below (command line arguments)

from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog, QMainWindow
from PyQt5.QtGui import QColor, QPalette
from PyQt5.uic import loadUi      # special library to load .ui file directly

class MyForm(QMainWindow):
    # constructor for this MyForm class 
    def __init__(self):
        super().__init__()   # calls the constructor of the QDialog class that is inherited
        
        # Change 'gui_template.ui' to the .ui file you created with Qt Designer
        # or rename the provided gui_template.ui to your own file and change name
        # the .ui file MUST BE IN THE SAME FOLDER AS THIS .PY FILE
        self.ui = loadUi('pomoduro.ui', self)   #<======= this line must be changed to your .UI file!
        
        self.ui.actionColor.triggered.connect(self.menuBackgroundMethod)
        self.ui.actionExit.triggered.connect(self.exitMethod)
        self.ui.pushButton5.clicked.connect(self.fiveMinutes)
        self.ui.pushButton10.clicked.connect(self.tenMinutes)
        self.ui.pushButton15.clicked.connect(self.fifteenMinutes)
        # add code here to connect the pushButton widgets to your methods.
        # for this first project three empty methods are already created.
        # you are responsible for connecting the clicked signal from your widgets
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
        pass
    
    def tenMinutes(self):
        pass
    
    def fifteenMinutes(self):
        pass

    def exitMethod(self):
        QApplication.instance().quit()



# the code below should not be changed and is constant for all GUI programs
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    # w.show()            # not needed because constructor does .show()
    sys.exit(app.exec_())  # note - sys.exit causes traceback in some editors if it does in yours just use app.exec()