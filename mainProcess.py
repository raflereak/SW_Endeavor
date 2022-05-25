import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

import Function.AutoFileOrganize.program_ver2 as organize
import Function.VersionManager.versionManager as verManage
import Function.Log as Log
import Function.forManageData as md
import Function.MakePackage.package as package

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("GUI\\main.ui")[0]
form_class1 = uic.loadUiType("GUI\\LogWindow.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.initUI()
        # 화면을 보여준다.
        self.show()
        self.loadData = md.manageData("option.txt")
        self.packageClass = package.package("Package")
        self.refreshData()
        self.refreshItemList_ForPackage()
        self.loadlist = self.loadData.get_data()

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
        self.buttonOpenExplore.clicked.connect(self.OpenExplore)

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
    window.getAddData()
    window.loadData.set_data(window.loadlist)
    window.loadData.save_Data()