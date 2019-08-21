# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_wit import Ui_MainWindow
from Tencent import WISG

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        
        print("test")
        pass
    
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        
        pn = self.LineEdit.text()
        pg = self.LineEdit_2.text()
        bn = self.LineEdit_3.text()
        lv = self.LineEdit_4.text()
        speed = self.LineEdit_5.text()
        time = self.LineEdit_6.text()
        call = self.LineEdit_7.text()
        print(pn)
        print(pg)
        print(bn)
        print(lv)
        print(speed)
        print(time)
        print(call)
        print("更新信息")
        pass
        
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        
        self.LineEdit.setText('')
        self.LineEdit_2.setText('')
        self.LineEdit_3.setText('')
        self.LineEdit_4.setText('')
        self.LineEdit_5.setText('')
        self.LineEdit_6.setText('')
        self.LineEdit_7.setText('')
        print("清除信息")
        
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    tencent = WISG()
    tencent.extract_data()
    ui.show()
    sys.exit(app.exec_())
    

