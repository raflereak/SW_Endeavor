import os
import shutil

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class package:
    def __init__(self, _path_Package):
        self.pathPackage = _path_Package
        self.fileList = os.listdir(_path_Package)


    def makePackage(self):
        print()

    def copyAndPaste_File(self, _what, _path_target):
        targetFile = shutil.copy(os.join(self.pathPackage, self.fileList[_what])
        shutil.paste(_path_target)