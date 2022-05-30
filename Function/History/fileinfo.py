import os, datetime
import pandas as pd

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def dataGet(_path):
    try:
        csv = pd.read_csv('dataset.csv')#csv파일이 있는지 확인하기 위해서 사용
    except:
        f = open("dataset.csv", "a", encoding='cp949')#없으면 생성 및 헤더 자동 작성
        f.write("파일명,작성시간,수정시간,확장자,용량" + "\n")

    filename = _path#경로나 같은 폴더의 파일명으로 이용가능

    f = open("dataset.csv", "a", encoding='cp949')
    # 만든시간을 타임 스탬프로 출력
    ctime = os.path.getctime(filename)#path or filename
    # 수정시간을 타임 스탬프로 출력
    mtime = os.path.getmtime(filename)#path or filename
    # 파일크기
    size = os.path.getsize(filename)#path or filename
    size_count = 0
    if(size > 1024):
        size = round((size / 1024),2)
        round(size,2)
        size_count += 1
        if(size > 1024):
            size = round((size / 1024),2)
            size_count += 1
            if(size > 1024):
                size = round((size / 1024),2)
                round(size,2)
                size_count += 1
    
    if(size_count == 0):
        size = str(size)+"B"
    elif(size_count == 1):
        size = str(size)+"K"
    elif(size_count == 2):
        size = str(size)+"M"
    elif(size_count == 3):
        size = str(size)+"G"

    filenames = filename.split('\\')
    names = filenames[-1]#파일 이름+확장자
    exttype = names.split('.')
    name = exttype[0]
    ext = exttype[-1]#확장자
    if (ext == names):
        ext = "폴더"
    c = datetime.datetime.fromtimestamp(ctime)
    m = datetime.datetime.fromtimestamp(mtime)
    
    f.write("%s,%s,%s,%s,%s" % (name,c,m,ext,size) + "\n")
    f.close()
