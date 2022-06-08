import os, datetime
import pandas as pd

def makeCsv(_data, _rootPath): #_rootPath : 대상 경로 _select : 정렬 방식(칼럼 내용) ex> ['Date', 'Time']
    df = pd.DataFrame(_data, columns=['File', 'Created', 'Date modified', 'Type', 'Size', 'Path'])
    df.to_csv(_rootPath, index=False, encoding='utf-8')
    return df

def getFileData(file_path):
    path, file = os.path.split(file_path)
    filename, file_extension = os.path.splitext(file)
    temp = [filename, datetime.datetime.fromtimestamp(os.path.getctime(file_path)), datetime.datetime.fromtimestamp(os.path.getmtime(file_path)), file_extension, os.path.getsize(file_path), path]
    return temp

