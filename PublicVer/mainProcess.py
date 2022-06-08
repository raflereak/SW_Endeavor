
import sys, os
import fileToDoList as todo

from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *

import OrganizeFile as organize
import versionManager as verManage
import Log as Log
import forManageData as md
import package as package
import OrderByOldest as obo

import datetime

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("main.ui")[0]
form_class1 = uic.loadUiType("LogWindow.ui")[0]
form_class2 = uic.loadUiType("Setting.ui")[0]
form_class3 = uic.loadUiType("authorize.ui")[0]
form_class4 = uic.loadUiType("calendar.ui")[0]


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
        self.TabTableList = []
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.openCalendar()
        self.window3.setMouseTracking(True)
        self.setTab()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        show_action = QAction("보이기", self)
        quit_action = QAction("종료", self)
        hide_action = QAction("숨기기", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.FunctionActivate()
        self.tray_icon.show()
        self.hide()
        self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000
            )

    def FunctionActivate(self):
        # Organize
        if self.loadData.checkOrganize:
            self.targetOrganizePath.setEnabled(True)
            self.targetFolderPath.setEnabled(True)
            self.radioShortCut.setEnabled(True)
            self.radio_move.setEnabled(True)
            self.targetOrganizeTool.setEnabled(True)
            self.targetFolderTool.setEnabled(True)
            self.buttonOrganize.setEnabled(True)
        else:
            self.targetOrganizePath.setDisabled(True)
            self.targetFolderPath.setDisabled(True)
            self.radioShortCut.setDisabled(True)
            self.radio_move.setDisabled(True)
            self.targetOrganizeTool.setDisabled(True)
            self.targetFolderTool.setDisabled(True)
            self.buttonOrganize.setDisabled(True)
        # Version
        if self.loadData.checkVersion:
            self.buttonVersion.setEnabled(True)
            self.buttonChangeVersion.setEnabled(True)
            self.buttonSelectFile.setEnabled(True)
            self.listVersionFile.setEnabled(True)
        else:
            self.buttonVersion.setDisabled(True)
            self.buttonChangeVersion.setDisabled(True)
            self.buttonSelectFile.setDisabled(True)
            self.listVersionFile.setDisabled(True)
        # Package
        if self.loadData.checkPackage:
            self.buttonMakePackage.setEnabled(True)
            self.PackageName.setEnabled(True)
            self.listPackage.setEnabled(True)
        else:
            self.buttonMakePackage.setDisabled(True)
            self.PackageName.setDisabled(True)
            self.listPackage.setDisabled(True)
            
        # OBO
        if self.loadData.checkOrderByOldest:
            self.ButtonAdd.setEnabled(True)
            self.buttonOpenExplorer.setEnabled(True)
            self.buttonDelete.setEnabled(True)
            self.orderbyListTab.setEnabled(True)
            self.ButtonTabDelete.setEnabled(True)
        else:
            self.ButtonAdd.setDisabled(True)
            self.buttonOpenExplorer.setDisabled(True)
            self.buttonDelete.setDisabled(True)
            self.orderbyListTab.setDisabled(True)
            self.ButtonTabDelete.setDisabled(True)

        # Calendar
        if self.loadData.checkCalendar:
            self.openCalendar()
            
        else:
            self.window3.close()



    def getAddData(self):
        # for Orgazie
        self.loadlist[0] = self.targetOrganizePath.text()
        self.loadlist[1] = self.targetFolderPath.text()
        self.loadlist[2] = str(self.radioShortCut.isChecked())
        
        # Version
        self.loadlist[3] = self.buttonSelectFile.text()
        self.loadlist[4] = self.lineSelectFilePath.text()
        
        # Package
        self.loadlist[5] = self.packageClass.pathPackage
        
        # Order by List
        self.loadlist[6] = str(self.orderbyListTab.count())
        tempList = []
        for i in range(self.orderbyListTab.count()):
            tempList.append(self.orderbyListTab.tabText(i))
        self.loadlist[7] = tempList

    def getDataSetting(self, _input):
        for i in range(len(_input)):
            self.loadlist[8+i] = _input[i]



    def refreshData(self):
        self.targetOrganizePath.setText(self.loadData.organize_Path)
        self.targetFolderPath.setText(self.loadData.targetFolder_Path)
        # self.buttonSelectFile.setText(self.loadData.file)
        # self.lineSelectFilePath.setText(self.loadData.file_Path)

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
        self.buttonOpenExplorer.clicked.connect(self.selectItemOpen_OBO)
        self.buttonDelete.clicked.connect(self.selectItemDelete_OBO)
        self.buttonCancel.clicked.connect(self.cancel)
        self.buttonSetting.clicked.connect(self.openSettingWindow)
        self.ButtonAdd.clicked.connect(self.addTab)
        self.ButtonTabDelete.clicked.connect(self.tabDelete)

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
        if(self.PackageName.text() == ""):
            self.packageClass.copyAndPaste_File_noneName(self.listVersionFile.currentRow(), where)
        else: 
            self.packageClass.copyAndPaste_File(self.listVersionFile.currentRow(), where, self.PackageName.text())
        self.packageClass.refreshList()

    def changeVer(self):
        if(self.lineSelectFilePath.text() != "" and self.buttonSelectFile.text() != ""):
            verManage.changeHiddenFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text(), self.listVersionFile.currentRow())

    def setTab(self):
        if(self.orderbyListTab.tabText(0) == "Tab 1"):
            self.orderbyListTab.removeTab(0)
        if(self.orderbyListTab.tabText(0) == "Tab 2"):
            self.orderbyListTab.removeTab(0)
        
        for i in range(int(self.loadData.tabSize)):
            self.TabTableList.append(QTableWidget())
            self.TabTableList[len(self.TabTableList)-1].setMaximumWidth(761)
            self.TabTableList[len(self.TabTableList)-1].setMinimumWidth(761)
            self.TabTableList[len(self.TabTableList)-1].setMaximumHeight(761)
            self.TabTableList[len(self.TabTableList)-1].setMinimumHeight(331)
            self.TabTableList[len(self.TabTableList)-1].setSelectionBehavior(QAbstractItemView.SelectRows)
            self.TabTableList[len(self.TabTableList)-1].horizontalHeader().setStretchLastSection(True)
            self.TabTableList[len(self.TabTableList)-1].insertRow(4) # for문을 써야하나? => 생성을 하기 때문에 생성 단계에서 준비해놔야함
            obo.orderByList(obo.makeFileData(self.loadData.tabList[i]), os.path.basename(self.loadData.tabList[i])+".csv", ['Date', 'Time'])
            self.TabTableList[len(self.TabTableList)-1] = self.readCSV(os.path.basename(self.loadData.tabList[i])+".csv", self.TabTableList[len(self.TabTableList)-1])
            self.orderbyListTab.addTab(self.TabTableList[len(self.TabTableList)-1], self.loadData.tabList[i])
            
    

    def readCSV(self, file, _table):
        log = open(file, 'r', encoding="utf-8")
        lineCnt = 0
        _table.insertColumn(0)
        _table.insertColumn(1)
        for i in log.readlines(): 
            _table.insertRow(lineCnt)
            i = i.split(",")
            newItem1 = QTableWidgetItem(i[0])
            newItem2 = QTableWidgetItem(i[3])
            _table.setItem(lineCnt, 0, newItem1)
            _table.setItem(lineCnt, 1, newItem2)
            lineCnt += 1
        return _table

    def addTab(self):
        if(self.orderbyListTab.tabText(0) == "Tab 1"):
            self.orderbyListTab.removeTab(0)
        if(self.orderbyListTab.tabText(0) == "Tab 2"):
            self.orderbyListTab.removeTab(0)

        self.TabTableList.append(QTableWidget())
        self.TabTableList[len(self.TabTableList)-1].setMaximumWidth(761)
        self.TabTableList[len(self.TabTableList)-1].setMinimumWidth(761)
        self.TabTableList[len(self.TabTableList)-1].setMaximumHeight(761)
        self.TabTableList[len(self.TabTableList)-1].setMinimumHeight(331)
        self.TabTableList[len(self.TabTableList)-1].horizontalHeader().setStretchLastSection(True)
        self.TabTableList[len(self.TabTableList)-1].setSelectionBehavior(QAbstractItemView.SelectRows)
        where = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       os.getcwd(), 
                       QFileDialog.ShowDirsOnly)
        if (where):
            obo.orderByList(obo.makeFileData(where), os.path.basename(where)+".csv", ['Date', 'Time'])
            self.TabTableList[len(self.TabTableList)-1] = self.readCSV(os.path.basename(self.loadData.tabList[len(self.TabTableList)-1])+".csv", self.TabTableList[len(self.TabTableList)-1])
            self.orderbyListTab.addTab(self.TabTableList[len(self.TabTableList)-1], where)
        
    def selectItemDelete_OBO(self):
        obo.removeSelect(self.TabTableList[self.orderbyListTab.currentIndex()].selectedItems()[1].text())
        self.TabTableList[self.orderbyListTab.currentIndex()].removeRow(self.TabTableList[self.orderbyListTab.currentIndex()].currentRow())

    def selectItemOpen_OBO(self):
        obo.openDirSelect(os.path.dirname(self.TabTableList[self.orderbyListTab.currentIndex()].selectedItems()[1].text()))
        
    def tabDelete(self):
        self.orderbyListTab.removeTab(self.orderbyListTab.currentIndex())

    def openLogWindow(self):
        self.window1 = LogWindow()

    def cancel(self):
        self.close()
        LogWindow().close()

    def openSettingWindow(self):
        self.window2 = SettingWindow()

    def openCalendar(self):
        self.window3 = CalendarWidget()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000
            )
            

class LogWindow(QMainWindow, form_class1):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.Tool)
        # 연결한 Ui를 준비한다.
        self.initUI()
        self.readLog()
        # 화면을 보여준다.
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ButtonSearch.clicked.connect(self.searchLog)
        self.ButtonOkay.clicked.connect(self.okayButton)

    def readLog(self):
        log = open('debug.log', encoding="UTF-8")
        lineCnt = 0

        for i in log.readlines(): 
            self.tableWidget.insertRow(lineCnt)
            newItem1 = QTableWidgetItem(i[:25])
            newItem2 = QTableWidgetItem(i[25:])
            self.tableWidget.setItem(lineCnt, 0, newItem1)
            self.tableWidget.setItem(lineCnt, 1, newItem2)
            lineCnt += 1

    def okayButton(self):
        self.close()

    def searchLog(self):
        self.tableWidget.setRowCount(0)
        log = open('debug.log', encoding='UTF-8')
        lineCnt = 0
        for i in log.readlines():
            if self.lineSearch.text() in i:
                self.tableWidget.insertRow(lineCnt)
                newItem1 = QTableWidgetItem(i[:25])
                newItem2 = QTableWidgetItem(i[25:])
                self.tableWidget.setItem(lineCnt, 0, newItem1)
                self.tableWidget.setItem(lineCnt, 1, newItem2)
                lineCnt += 1

class SettingWindow(QDialog, form_class2):
    def __init__(self) :
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.Tool)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.loadSettingData()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ButtonAuth.clicked.connect(self.openAuthWindow)
        self.ButtonOkay.clicked.connect(self.okayButton)
        self.ButtonCancel.clicked.connect(self.cancelButton)

    def openAuthWindow(self):
        self.AuthWindow = AuthWindow()

    def loadSettingData(self):
        self.lineName.setText(window.loadData.name)
        self.lineBirthday.setText(window.loadData.birthday)
        self.lineJob.setText(window.loadData.job)
        self.lineField.setText(window.loadData.field)
        self.check_Organize.setChecked(bool(window.loadData.checkOrganize))
        self.check_Calendar.setChecked(bool(window.loadData.checkCalendar))
        self.check_SendData.setChecked(bool(window.loadData.checkSendData))
        self.check_OBO.setChecked(bool(window.loadData.checkOrderByOldest))
        self.check_Version.setChecked(bool(window.loadData.checkVersion))
        self.check_Package.setChecked(bool(window.loadData.checkPackage))

    def saveSettingData(self):
        temp = []
        temp.append(self.lineName.text())
        temp.append(self.lineBirthday.text())
        temp.append(self.lineJob.text())
        temp.append(self.lineField.text())
        temp.append("0")
        temp.append(str(self.check_Organize.isChecked()))
        temp.append(str(self.check_Calendar.isChecked()))
        temp.append(str(self.check_SendData.isChecked()))
        temp.append(str(self.check_OBO.isChecked()))
        temp.append(str(self.check_Version.isChecked()))
        temp.append(str(self.check_Package.isChecked()))
        
        return temp

    def okayButton(self):
        window.getDataSetting(self.saveSettingData())
        window.loadData.set_data(window.loadlist)
        window.FunctionActivate()
        self.close()

    def cancelButton(self):
        self.close()

class AuthWindow(QDialog, form_class3):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.Tool)
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
            window.window2.lineEdit.setDisabled(True)
            window.window2.ButtonAuth.setDisabled(True)
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
        self.setDisabledState()
        
        self.setWindowFlags(QtCore.Qt.Tool|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.FramelessWindowHint)
        self.show()
        self.url = ""
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.location_on_the_screen()

    def initUI(self):
        self.setupUi(self)

    def setActiveState(self):
        self.setWindowOpacity(0.7)
        self.resize(490,565)
        self.location_on_the_screen()

    def setDisabledState(self):
        screen = QDesktopWidget().screenGeometry()
        self.setWindowOpacity(0.01)
        self.resize(1,screen.height())
        self.location_on_the_screen()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.setActiveState()
            event.accept()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event):
        self.setDisabledState()

    def mouseMoveEvent(self, event):
        screen = QDesktopWidget().screenGeometry()
        Mouse = event.globalPos()
        if(Mouse.x() >= screen.width() - 5):
            self.setActiveState()
        if(Mouse.x() < screen.width() - 5):
            self.setDisabledState()

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
        window.AuthAccount.makeSchedule(fileName, date)
        self.setDisabledState()

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