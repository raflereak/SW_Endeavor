import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


import datetime

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("E:\\Nas Cloud\Develope\\For VsCode\\대학교\\2022년 1학기\\SW_Endeavor\\Function\\FileToDoList\\calendar.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 연결한 Ui를 준비한다.
        self.initUI()
        self.setWindowOpacity(0.7)
        # 화면을 보여준다.
        self.makeCalendar()
        self.show()
        self.url = ""
        self.setAcceptDrops(True)

    def initUI(self):
        self.setupUi(self)
        

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.tableWidget.setCurrentItem(self.tableWidget.itemAt(event.pos()))
        for i in self.tableWidget.selectedItems():
            print(i.text())
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)

    def makeCalendar(self):
        now = datetime.datetime.today()
        
        dateDict = {0: 1, 1:2, 2:3, 3:4, 4:5, 5:7, 6:0}
        startPos = dateDict[now.weekday()]
        for weeks in range(20):
            for date in range(7):
                newItem = QTableWidgetItem(str(now.strftime("%m-%d")))
                newItem.setTextAlignment(4)
                if(date == 6):
                    newItem.setBackground(QtGui.QColor(56,119,214))
                if(date == 0):
                    newItem.setBackground(QtGui.QColor(236,75,69))
                if(weeks == 0 and date >= startPos):
                    self.tableWidget.setItem(weeks, date, newItem)
                    now += datetime.timedelta(days=1)
                elif(weeks != 0):
                    self.tableWidget.setItem(weeks, date, newItem)
                    now += datetime.timedelta(days=1)    
        
                

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()