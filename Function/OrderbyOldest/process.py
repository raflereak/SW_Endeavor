import os
from datetime import datetime
import pandas as pd
import sys
import io
import traceback

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def orderByList(_data, _rootPath, _select): #_rootPath : 대상 경로 _select : 정렬 방식(칼럼 내용) ex> ['Date', 'Time']
    _data = _data.sort_values(by=_select)
    _data.to_csv(_rootPath, index=False, encoding='utf-8')
    return _data

def makePath(_input):
    return _input 

def makeFileData(_loadPath):
    temp = []
    for rootPath in _loadPath:
        dir_path = makePath(rootPath)
        print("Now Reading : " + dir_path)
        
        for (root, directories, files) in os.walk(dir_path):
            for d in directories:
                d_path = os.path.join(root, d)
            for file in files:
                file_path = os.path.join(root, file)
                tempTime = os.path.getatime(file_path)
                temp.append([datetime.fromtimestamp(tempTime).strftime('%Y%m%d'), datetime.fromtimestamp(tempTime).strftime('%H%M%S'), file, file_path, os.path.getsize(file_path)])
        df = pd.DataFrame(temp, columns=['Date', 'Time', 'FileName', 'Path', 'Size'])
    return df

def mainProcess():
    print("Input Path : ", end="")
    LoadPath = input()
    orderByList(makeFileData(LoadPath), LoadPath + ".csv", ['Date', 'Time'])

mainProcess()
