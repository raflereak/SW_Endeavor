import shutil
import os
import win32file

# 버전 표기 포맷
# .FM_Ver1


def checkHowManyFile(_filePath, _fileName): # 해당 파일의 버전이 몇개 있는지 파악
    tempList = []
    filenames = os.listdir(_filePath)

    for filename in filenames:
        if (not filename.find(_fileName)):
            tempList.append(filename)

    return tempList

def makeVersionFile(_filePath, _fileName): # 해당 파일의 버전 생성
    cnt = 0
    eaFile = checkHowManyFile(_filePath, _fileName)

    if(len(eaFile) == 6):
        for tempFile in eaFile:
            if(".FM_Ver1" in tempFile):
                os.remove(_filePath + "\\" + eaFile[eaFile.index(tempFile)])

        for file in eaFile:
            cnt += 1
            if((".FM_Ver" in file) and not (".FM_Ver1" in file)):
                os.rename(os.path.join(_filePath, file), os.path.join(_filePath, file.strip(".FM_Ver" + str(cnt - 1)) + ".FM_Ver" + str((cnt - 2))))
                
        filepathforreturn = shutil.copy(os.path.join(_filePath, _fileName), os.path.join(_filePath, _fileName + ".FM_Ver5"))
        win32file.SetFileAttributes(filepathforreturn, 2)
        
    else:
        cnt = len(eaFile)
        filepathforreturn = shutil.copy(os.path.join(_filePath, _fileName), os.path.join(_filePath, _fileName + ".FM_Ver" + str(cnt)))
        win32file.SetFileAttributes(filepathforreturn, 2)

        return _filePath, _fileName, cnt

def changeHiddenFile(_filePath, _fileName, _targetVer): # 해당 파일과 특정 파일과의 이름 변경 및 숨김처리 변경
    os.rename(os.path.join(_filePath, _fileName), os.path.join(_filePath, "temp.FM_Ver"))
    os.rename(os.path.join(_filePath, _fileName + ".FM_Ver" + str(_targetVer)), os.path.join(_filePath, _fileName))
    os.rename(os.path.join(_filePath, "temp.FM_Ver"), os.path.join(_filePath, os.path.join(_filePath, _fileName + ".FM_Ver" + str(_targetVer))))
    
    win32file.SetFileAttributes(os.path.join(_filePath, _fileName + ".FM_Ver" + str(_targetVer)), 2)
    win32file.SetFileAttributes(os.path.join(_filePath, _fileName), 1)

    return _filePath, _fileName, _targetVer
