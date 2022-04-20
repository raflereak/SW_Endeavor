import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

import Function.AutoFileOrganize.program as organize
import Function.VersionManager.versionManager as verManage
import Function.Log as Log
# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("main.ui")[0]
form_class1 = uic.loadUiType("LogWindow.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()

    def getFloder(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Folder', 'C:\\', "All files (*)")
        
    def getOrganizeFloder(self):
        fileName = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       os.getcwd(), 
                       QFileDialog.ShowDirsOnly)
        self.targetOrganizePath.setText(fileName)

    def getTargetFloder(self):
        fileName = QFileDialog.getExistingDirectory(
                       #QtWidgets.QFileDialog,                  # ???
                       None,
                       "Open Directory",
                       os.getcwd(), 
                       QFileDialog.ShowDirsOnly)
        self.targetFolderPath.setText(fileName)

    def processOrganize(self):
        Log.organizeLog(organize.process(self.targetOrganizePath.text(), self.targetFolderPath.text()))
        
    def verMake(self):
        verManage.makeVersionFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text())
        self.refreshItemList()

    def initUI(self):
        self.setupUi(self)
        self.buttonOrganize.clicked.connect(self.processOrganize)
        self.targetOrganizeTool.clicked.connect(self.getOrganizeFloder)
        self.targetFloderTool.clicked.connect(self.getTargetFloder)
        self.buttonSelectFile.clicked.connect(self.getTargetVerFile)
        self.buttonVersion.clicked.connect(self.verMake)
        self.buttonChangeVersion.clicked.connect(self.changeVer)
        self.buttonLog.clicked.connect(self.openLogWindow)

    def getTargetVerFile(self):
        fileName = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='',
            initialFilter=''
        )
        self.buttonSelectFile.setText(os.path.basename(fileName[0]))
        self.lineSelectFilePath.setText(os.path.dirname(fileName[0]))
        self.refreshItemList()
    
    def refreshItemList(self):
        self.listVersionFile.clear()
        addlist = verManage.checkHowManyFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text())
        for i in addlist:
            self.listVersionFile.addItem(i)
            

    def changeVer(self):
        verManage.changeHiddenFile(self.lineSelectFilePath.text(), self.buttonSelectFile.text(), self.listVersionFile.currentRow())

    def openLogWindow(self):
        self.window1 = LogWindow()


class LogWindow(QMainWindow, form_class1):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()

    def initUI(self):
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()