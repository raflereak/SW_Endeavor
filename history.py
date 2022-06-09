import os, datetime
import pandas as pd

def orderByList(_data, _rootPath, _select): #_rootPath : 대상 경로 _select : 정렬 방식(칼럼 내용) ex> ['Date', 'Time']
    _data = _data.sort_values(by=_select)
    _data.to_csv(_rootPath, index=False, encoding='utf-8')
    return _data

def makePath(_input):
    return _input + ":\\"

def getFileData(file_path):
    path, file = os.path.split(file_path)
    filename, file_extension = os.path.splitext(file)
    temp = [filename, datetime.datetime.fromtimestamp(os.path.getctime(file_path)), datetime.datetime.fromtimestamp(os.path.getmtime(file_path)), file_extension, os.path.getsize(file_path), path]

def makeFileData(_loadPath):
    temp = []
    dir_path = _loadPath
    for (root, directories, files) in os.walk(dir_path):
        for d in directories:
            d_path = os.path.join(root, d)
        for file in files:
            file_path = os.path.join(root, file)
            filename, file_extension = os.path.splitext(file)
            temp.append([filename, datetime.datetime.fromtimestamp(os.path.getctime(file_path)), datetime.datetime.fromtimestamp(os.path.getmtime(file_path)), file_extension, os.path.getsize(file_path), file_path])
    df = pd.DataFrame(temp, columns=['File', 'Created', 'Date modified', 'Type', 'Size', 'Path'])
    return df
#이름, 확장자, 생성일자, 수정 날짜, 용량가 동일할 때 기록을 갱신할 것
#수정날짜의 경우 최신 날짜가 있으면 기존 과거 데이터 제거 후 추가하는 조건