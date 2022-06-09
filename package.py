import os
import shutil


class package: # 클래스를 생성해야합니다. 매개변수는 패키지 폴더를 저장할 공간입니다.
    def __init__(self, _path_Package):
        self.pathPackage = os.path.abspath(_path_Package)
        self.fileList = os.listdir(_path_Package)

    def setPackagePath(self, _path):
        self.pathPackage = _path

    def getPackagePath(self):
        return self.pathPackage

    def refreshList(self):
        self.fileList = os.listdir(self.pathPackage)

    def makePackage(self, _name): # 패키지 폴더를 저장할 공간에 이름을 지정하여 폴더를 만듭니다.
        os.makedirs(os.path.join(self.pathPackage, "forPackage_" + _name))

    def copyAndPaste_File_noneName(self, _what, _path_target): # 패키지 폴더를 저장한 곳에서 몇번째 파일인지 지정하고, 어디로 옮길 것인지 지정하여 실행합니다.
        shutil.copytree(os.path.join(self.pathPackage, self.fileList[_what]), os.path.join(_path_target, "package_" + self.fileList[_what]))
        return self.pathPackage, _path_target

    def copyAndPaste_File(self, _what, _path_target, _name): # 패키지 폴더를 저장한 곳에서 몇번째 파일인지 지정하고, 어디로 옮길 것인지 지정하여 실행합니다.
        shutil.copytree(os.path.join(self.pathPackage, self.fileList[_what]), os.path.join(_path_target, _name))
        return self.pathPackage, _name, _path_target
