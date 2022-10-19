from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from os import path
import sys,os
from  Last_window import mainapp
Form_class2,_=loadUiType(path.join(path.dirname(__file__),"secondform.ui"))
class Second(QWidget,Form_class2):
    def __init__(self,parent=None):
        super(Second,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.objPath=""
        self.objName=""
        self.handle_button()
    def Show_files(self):
        self.objPath=QFileDialog.getExistingDirectory(self,'Save At','C:\\')
        self.objName=self.lineEdit.text()
        self.lineEdit_2.setText(self.objPath)
    def Create_folder(self):
        os.mkdir(os.path.join(self.objPath,self.objName))
    def openWin2(self):
        self.Create_folder()
        self.window2=mainapp()
        self.window2.show()
    def handle_button(self):
        self.pushButton.clicked.connect(self.Show_files)
        self.pushButton_2.clicked.connect(self.openWin2)


def main():
    app=QApplication(sys.argv)
    window=Second()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()