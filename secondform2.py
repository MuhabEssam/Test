from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from os import path,mkdir
import sys
from  Last_window import mainapp
Form_class2,_=loadUiType(path.join(path.dirname(__file__),"secondform.ui"))
class Second(QWidget,Form_class2):
    def __init__(self,parent=None):
        super(Second,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.objPath=""
        self.objName=""
        self.F_cpu=""
        self.microSelect=""
        self.ErrorBox=QMessageBox()
        self.Error_handle()
        self.handle_button()
        self.events()
    def events(self):
        self.lineEdit.textEdited.connect(self.editPname)
        self.lineEdit_2.textEdited.connect(self.editPname)
        self.lineEdit_3.textEdited.connect(self.editFreq)
        self.comboBox.currentTextChanged.connect(self.editMicro)
    def editPname(self):
        self.objName=self.lineEdit.text()
    def editPaname(self):
        self.objPath=self.lineEdit_2.text()
    def editFreq(self):
        self.F_cpu=self.lineEdit_3.text()
    def editMicro(self):
        self.microSelect=self.comboBox.currentText()
    def Show_files(self):
        self.objName = self.lineEdit.text()
        self.objPath=QFileDialog.getExistingDirectory(self,'Save At','.')
        self.lineEdit_2.setText(self.objPath)
    def Error_handle(self):
        self.ErrorBox.setWindowTitle( "Error")
        self.ErrorBox.setStandardButtons(QMessageBox.Ok)
        self.ErrorBox.setIcon(QMessageBox.Warning)
    def Create_folder(self):
        mkdir(path.join(self.objPath,self.objName))
    def openWin3(self):
        if(self.objName==""):
            self.ErrorBox.setText("Please write project name")
            self.ErrorBox.exec()
        elif(self.objPath==""):
            self.ErrorBox.setText("Please choose path to save project ")
            self.ErrorBox.exec()
        elif(self.comboBox.currentText()==""):
            self.ErrorBox.setText("Please select a microcontroller ")
            self.ErrorBox.exec()
        elif (self.lineEdit_3.text() == ""):
            self.ErrorBox.setText("Please write frequency  ")
            self.ErrorBox.exec()
        else:
            self.Create_folder()
            self.window2=mainapp(self.Folder_path(),self.microSelect,self.F_cpu)
            self.window2.show()
    def handle_button(self):
        self.pushButton.clicked.connect(self.Show_files)
        self.pushButton_2.clicked.connect(self.openWin3)
    def Folder_path(self):
        return path.join(self.objPath,self.objName)

def main():
    app=QApplication(sys.argv)
    window=Second()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()