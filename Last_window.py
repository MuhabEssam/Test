from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from os import path
#import file_rc
form_class,_ =loadUiType(path.join(path.dirname(__file__),"CODE_gene.ui"))
class mainapp(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(mainapp, self).__init__(parent)  # i dont use it
        QMainWindow.__init__(self)
        self.setupUi(self)
        #any connection i want must be in function and the function have the connection
        self.initlization()
        self.Button_Connections()
    def initlization(self):
        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.groupBox_4.setVisible(False)
        self.groupBox_5.setVisible(False)
        self.listWidget_2.setVisible(False)
    def Button_Connections(self):
        self.pushButton.clicked.connect(lambda:self.Open_list(self.pushButton.text()))
        self.listWidget.currentRowChanged.connect(self.Clicked)
    def Open_list(self,PIN_name):
        self.listWidget_2.setVisible(True)
        self.listWidget_2.itemClicked.connect(lambda :self.getItem(PIN_name))
    def getItem(self,PIN_name):
        self.listWidget_2.setVisible(False)
        return PIN_name,self.listWidget_2.currentItem().text()
    def Clicked(self,idx=int):
        if idx==0:
            self.groupBox_2.setVisible(True)
            self.groupBox_3.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            #set the size and location of groupbox
            self.groupBox_2.setFixedWidth(321)
            self.groupBox_2.setFixedHeight(241)
            self.groupBox_2.move(220,60)
            
        if idx==1:
            self.groupBox_3.setVisible(True)
            self.groupBox_2.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_5.setVisible(False)
            #set the size and location of groupbox
            self.groupBox_3.setFixedWidth(321)
            self.groupBox_3.setFixedHeight(241)
            self.groupBox_3.move(220,60)
            
        if idx==2:
            self.groupBox_4.setVisible(True)
            self.groupBox_3.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox_5.setVisible(False)
            #set the size and location of groupbox
            self.groupBox_4.setFixedWidth(321)
            self.groupBox_4.setFixedHeight(241)
            self.groupBox_4.move(220,60)
        if idx==3:
            self.groupBox_5.setVisible(True)
            self.groupBox_3.setVisible(False)
            self.groupBox_4.setVisible(False)
            self.groupBox_2.setVisible(False)
            #set the size and location of groupbox
            self.groupBox_5.setFixedWidth(321)
            self.groupBox_5.setFixedHeight(241)
            self.groupBox_5.move(220,60)
def main():
    print('start')
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()  # infinite loop


    

if __name__=='__main__':
    main()
