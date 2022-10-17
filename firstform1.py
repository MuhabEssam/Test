from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from os import path
import sys
from secondform2 import Second
Form_class1,_=loadUiType(path.join(path.dirname(__file__),"firstform.ui"))
class First(QWidget,Form_class1):
    def __init__(self,parent=None):
        super(First,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.button_handle()
    def openWin(self):
        self.window1=Second()
        self.window1.show()
    def button_handle(self):
        self.pushButton.clicked.connect(self.openWin)
def main():
    app=QApplication(sys.argv)
    window=First()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()