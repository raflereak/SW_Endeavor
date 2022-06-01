import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QAbstractItemView

import Function.AutoFileOrganize.program_ver2 as organize
import Function.VersionManager.versionManager as verManage
import Function.Log as Log
import Function.forManageData as md
import Function.MakePackage.package as package
import Function.FileToDoList.fileToDoList as todo

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

import Function.AutoFileOrganize.program_ver2 as organize
import Function.VersionManager.versionManager as verManage
import Function.Log as Log
import Function.forManageData as md
import Function.MakePackage.package as package

from multiprocessing import Process

import datetime

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("GUI\\main.ui")[0]
form_class1 = uic.loadUiType("GUI\\LogWindow.ui")[0]
form_class2 = uic.loadUiType("GUI/Setting.ui")[0]
form_class3 = uic.loadUiType("GUI/authorize.ui")[0]
form_class4 = uic.loadUiType("GUI\\calendar.ui")[0]


# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.AuthAccount = todo.todoList()
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()
        self.loadData = md.manageData("option.txt")
        self.packageClass = package.package("Package")
        self.refreshData()
        self.refreshItemList_ForPackage()
        self.loadlist = self.loadData.get_data()
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.openCalendar()
        self.window3.setMouseTracking(True)
        
    

    def getAddData(self):
        # for Orgazie
        self.loadlist[0] = self.targetOrganizePath.text()
        self.loadlist[1] = self.targetFolderPath.text()
        self.loadlist[2] = str(self.radioShortCut.isChecked())
        
        # Version
        self.loadlist[3] = self.buttonSelectFile.text()
        self.loadlist[4] = self.targetFolderPath.text()
        
        # Package
        self.loadlist[5] = self.packageClass.pathPackage
        
        # Order by List
        # self.loadlist[5] = forInput_List[5]
        # self.loadlist[6] = forInput_List[6]
        # self.loadlist[7] = self.tab.split(",")

    def refreshData(self):
        self.targetOrganizePath.setText(self.loadData.organize_Path)
        self.targetFolderPath.setText(self.loadData.targetFolder_Path)
        #self.buttonSelectFile.setText(self.loadData.file)
        #self.lineSelectFilePath.setText(self.loadData.file_Path)

    def getFolder(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Folder', 'C:\\', "All files (*)")
        
    def getOrganizeFolder(self):
        fileName = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       self.targetOrganizePath.text(), 
                       QFileDialog.ShowDirsOnly)
        self.targetOrganizePath.setText(fileName)

    def getTargetFolder(self):
        fileName = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       self.targetFolderPath.text(), 
                       QFileDialog.ShowDirsOnly)
        self.targetFolderPath.setText(fileName)
        
    def OpenExplore(self):
        fileName = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       self.targetFolderPath.text(), 
                       QFileDialog.ShowDirsOnly)
        self.targetFolderPath.setText(fileName)    

    def processOrganize(self):
        if (self.targetOrganizePath.text() != "" and self.targetFolderPath.text() != ""):
            Log.organizeLog(organize.process(self.targetOrganizePath.text(), self.targetFolderPath.text(), self.radioShortCut.isChecked()))
        
    def verMake(self):
        if(self.lineSelectFilePath.text() != "" and self.buttonSelectFile.text() != ""):
            verManage.makeVersionFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text())
            self.refreshItemList()

    def initUI(self):
        self.setupUi(self)
        self.buttonOrganize.clicked.connect(self.processOrganize)
        self.targetOrganizeTool.clicked.connect(self.getOrganizeFolder)
        self.targetFolderTool.clicked.connect(self.getTargetFolder)
        self.buttonSelectFile.clicked.connect(self.getTargetVerFile)
        self.buttonVersion.clicked.connect(self.verMake)
        self.buttonChangeVersion.clicked.connect(self.changeVer)
        self.buttonLog.clicked.connect(self.openLogWindow)
        self.buttonMakePackage.clicked.connect(self.makePackage)
        self.buttonOpenExplorer.clicked.connect(self.OpenExplore)
        self.buttonCancel.clicked.connect(self.cancel)
        self.buttonSetting.clicked.connect(self.openSettingWindow)
        self.buttonHistory.clicked.connect(self.openCalendar)

    def getTargetVerFile(self):
        fileName = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.path.join(self.buttonSelectFile.text(), self.lineSelectFilePath.text()),
            filter='',
            initialFilter=''
        )
        if(os.path.basename(fileName[0]) != "" and os.path.dirname(fileName[0]) != ""):
            self.buttonSelectFile.setText(os.path.basename(fileName[0]))
            self.lineSelectFilePath.setText(os.path.dirname(fileName[0]))
            self.refreshItemList()
    
    def refreshItemList(self):
        self.listVersionFile.clear()
        addlist = verManage.checkHowManyFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text())
        for i in addlist:
            self.listVersionFile.addItem(i)
            
    def refreshItemList_ForPackage(self):
        self.listPackage.clear()
        for i in self.packageClass.fileList:
            self.listPackage.addItem(i)

    def makePackage(self):
        where = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       os.getcwd(), 
                       QFileDialog.ShowDirsOnly)
        # if(self.PackageName.text() == ""):
        #     self.packageClass.copyAndPaste_File_noneName(self.listVersionFile.currentRow(), where)
        # else: 
        #     self.packageClass.copyAndPaste_File(self.listVersionFile.currentRow(), where, self.PackageName.text())
        # self.packageClass.refreshList()
        if (self.PackageName.text() != "" and self.PackageName.text() != ""):
            Log.organizeLog(organize.process(self.PackageName.text(), self.PackageName.text(), self.radioShortCut.isChecked()))

    def changeVer(self):
        if(self.lineSelectFilePath.text() != "" and self.buttonSelectFile.text() != ""):
            verManage.changeHiddenFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text(), self.listVersionFile.currentRow())

    def openLogWindow(self):
        self.window1 = LogWindow()

    def cancel(self):
        self.exit
        LogWindow().exit

    def openSettingWindow(self):
        self.window2 = SettingWindow()

    def openCalendar(self):
        self.window3 = CalendarWidget()

class LogWindow(QMainWindow, form_class1):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()

    def initUI(self):
        self.setupUi(self)


class SettingWindow(QDialog, form_class2):
    def __init__(self) :
        QDialog.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ButtonAuth.clicked.connect(self.openAuthWindow)

    def openAuthWindow(self):
        self.AuthWindow = AuthWindow()

class AuthWindow(QDialog, form_class3):
    def __init__(self):
        QDialog.__init__(self)
        window.AuthAccount.auth_one(scopes=['Calendars.ReadWrite'])
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ButtonAuth.clicked.connect(self.processAuth)

    def processAuth(self):
        test = window.AuthAccount.auth_two(self.lineEdit.text(), scopes=['Calendars.ReadWrite'])
        if test:
            self.lineEdit.setText("인증에 성공했습니다.")
            window.window2.lineEdit.setText("인증에 성공했습니다.")
            self.close()
        else:
            self.lineEdit.setText("인증에 실패하였습니다.")

class CalendarWidget(QMainWindow, form_class4):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        self.setWindowOpacity(0.01)
        # 화면을 보여준다.
        self.makeCalendar()
        self.changeSizeSmall()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.FramelessWindowHint)
        self.show()
        self.url = ""
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.location_on_the_screen()

    def initUI(self):
        self.setupUi(self)
        
    def changeSizeSmall(self):
        self.resize(30,30)

    def changeSizeBig(self):
        self.resize(490,565)
    
    def activate(self):
        self.setWindowOpacity(0.7)
        self.changeSizeBig()
        self.location_on_the_screen()

    def setOff(self):
        self.setWindowOpacity(0.01)
        self.changeSizeSmall()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.activate()
            event.accept()
        else:
            event.ignore()
            

    def mouseMoveEvent(self, event):
        Mouse = event.globalPos()
        print(Mouse.x())
        if(Mouse.x() >= 3800):
            self.activate()
        if(Mouse.x() < 3300):
            self.setOff()

    def dropEvent(self, event):
        self.tableWidget.setCurrentItem(self.tableWidget.itemAt(event.pos()))
        date = None
        format = "%Y-%m-%d"
        fileName = ""
        for i in self.tableWidget.selectedItems():
            date = "2022-" + i.text()
        date = datetime.datetime.strptime(date, format)
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            fileName = f.split("/")
            fileName = fileName[len(fileName) - 1]
        print(fileName)
        print(date)
        window.AuthAccount.makeSchedule(fileName, date)
        self.setOff()

    def location_on_the_screen(self):    
        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        y = 0 # (screen.height() - widget.height()) / 2
        self.move(x, y)

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
    window.getAddData()
    window.loadData.set_data(window.loadlist)
    window.loadData.save_Data()