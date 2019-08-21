# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_wit import Ui_MainWindow
from Tencent import WISG
from PyQt5.QtCore import QTimer

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
        self.data = {
            'pn':'null',
            'pg':'null',
            'bn':0,
            'time':0,
            'lv':0,
            'speed':0,
            'led':0,
            'beep':1,
            'sm':0,
            'call':0
        }
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        
        print("test")
        pass
    
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        self.data['pn'] = self.LineEdit.text()
        self.data['pg'] = self.LineEdit_2.text()
        self.data['bn'] = self.LineEdit_3.text()
        self.data['lv'] = self.LineEdit_4.text()
        self.data['speed'] = self.LineEdit_5.text()
        self.data['time'] = self.LineEdit_6.text()
        self.data['call'] = self.LineEdit_7.text()
        print(self.data)
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
        #self.show_tencent_data()
        print("清除信息")
        
        pass
        
    def show_tencent_data(self, show_data):
        print("-----------")
        print(show_data)
        print("-----------")
        self.update_data(show_data)
        
        pass
    
    def update_data(self, updata):
        self.data = updata
        self.LineEdit.setText(str(self.data['pn']))
        self.LineEdit_2.setText(str(self.data['pg']))
        self.LineEdit_3.setText(str(self.data['bn']))
        self.LineEdit_4.setText(str(self.data['lv']))
        self.LineEdit_5.setText(str(self.data['speed']))
        self.LineEdit_6.setText(str(self.data['time']))
        self.LineEdit_7.setText(str(self.data['call']))

        pass
        
        
    def timer_init(self):
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
        self.timer.start(6000) #设置计时间隔并启动
        pass
    
    
    def operate(self):
        data = tencent.extract_data()
        self.show_tencent_data(data)
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    tencent = WISG()
    ui.timer_init()
    ui.show()
    sys.exit(app.exec_())
    

