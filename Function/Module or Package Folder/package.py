import os
import shutil

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class package: # 클래스를 생성해야합니다. 매개변수는 패키지 폴더를 저장할 공간입니다.
    def __init__(self, _path_Package):
        self.pathPackage = _path_Package
        self.fileList = os.listdir(_path_Package)


    def makePackage(self, _name): # 패키지 폴더를 저장할 공간에 이름을 지정하여 폴더를 만듭니다.
        os.makedirs(os.path.join(self.pathPackage, "forPackage_" + _name))

    def copyAndPaste_File(self, _what, _path_target): # 패키지 폴더를 저장한 곳에서 몇번째 파일인지 지정하고, 어디로 옮길 것인지 지정하여 실행합니다.
        shutil.copytree(os.path.join(self.pathPackage, self.fileList[_what]), os.path.join(_path_target, "package_" + self.fileList[_what]))
